#this is module
#import prime
from prime import PrimesTo

PrimesTo(100)

#this is package
#import main.sub2.prime as mypr
from main.sub2.prime import PrimesTo as mypr

mypr(100)

#built in module
import copy

my_dictionaries = {'item': 'shirt', 'size': 'medium', 'price': 50}
my_dictionaries1 = copy.deepcopy(my_dictionaries)
my_dictionaries[1] = 1
print(my_dictionaries)
print(my_dictionaries1)

import math as m
import cmath as cm
import random as ran
import sys

print(dir(cm)) #will list all function cmath
print(cm.sqrt(2))

print(m.ceil(2.6))
