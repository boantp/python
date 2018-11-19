from django.http import HttpResponse
import json
from . import exceptions
from request import Request
from django.shortcuts import render
# Create your views here.

def index(request):
    return HttpResponse("Cintaku, Cicilan tanpa Kartu!")
def bupati(request):
    return HttpResponse("List of bupati")
def detail(request, poll_id = ''):
    requestObj = Request()
    try:
        query_string_dict = requestObj.process_request_url(request)
    except exceptions.SystemImproperlyConfigured as e:
        return render(request, 'polls/error.html', {'error': e.message})

    response_data = {}
    response_data["url"] = query_string_dict

    return HttpResponse(json.dumps(response_data), content_type="application/json")

    #return HttpResponse("List with param" + str(poll_id) + "number")

