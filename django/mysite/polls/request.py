"""
Functions required for AES encryption
"""

from urlparse import urlparse
import base64

from Crypto import Random
from Crypto.Cipher import AES
from django.contrib.sites.shortcuts import get_current_site

from settings import AES_SECRET_KEY
import logging

from . import exceptions

# Get an instance of a logger
logger = logging.getLogger(__name__)


BS = 16

def pad(s): return s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
def unpad(s): return s[:-ord(s[len(s) - 1:])]

class Request(object):

    def get_base_url(self, request):
        return str(request.scheme) + '://' + str(get_current_site(request))

    def encrypt(self, raw, cipher_key=AES_SECRET_KEY):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(cipher_key, AES.MODE_CBC, iv)
        encoded_url = base64.b64encode(iv + cipher.encrypt(raw))
        return encoded_url

    def decrypt(self, enc, cipher_key=AES_SECRET_KEY):
        logger.debug(enc)
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(cipher_key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[16:]))

    def process_request_url(self, request):
        parsed_url = urlparse(request.build_absolute_uri())
        key_value_list = parsed_url.query.split("&")
        key_value_dict = {}
        for key_value in key_value_list:
            copy_key_value_list_item = key_value
            key_value_split_list = copy_key_value_list_item.split("=")
            try:
                key_value_dict[key_value_split_list[0]] = key_value_split_list[1]
            except Exception as e:
                logger.debug('Exception splitting key value in request URL. ' +
                          str(e) + ', key_value_list: ' + str(key_value_list))
        if "tk" not in key_value_dict:
            raise exceptions.SystemImproperlyConfigured()
        """
        Adding = in the end as it is removed when you execute the URL in browser. Max 2 = signs
        """
        global_param_value = key_value_dict['tk'] + '='
        try:
            url_params = self.decrypt(str(global_param_value))
        except Exception as e:
            global_param_value += '='
            url_params = self.decrypt(str(global_param_value))
            pass

        if len(url_params):
            key_value_list = url_params.split("&")
            key_value_dict = {}
            for key_value in key_value_list:
                key_value_split_list = key_value.split("=")
                key_value_dict[key_value_split_list[0]] = key_value_split_list[1]
        return key_value_dict

    def get_ip_address(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
            return ip
        remote_ip = request.META.get('REMOTE_ADDR')
        if remote_ip:
            return remote_ip
        return ''