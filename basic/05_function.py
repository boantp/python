#Functions

def function():
    print('hello boan tua pasaribu')

function() #call function

def returning():
    return 'hello boan tua pasaribu'

result = returning() #call function into variable
print(result)

def multiple_value():
    return 'hello boan tua pasaribu', 2

result = multiple_value()
print(result)
print(result[0])
print(result[1])

#passing arguments, and default paramaters
def add(a,b=3):
    return a + b

print(add(1))

#nested function
def outer(a):
    
    def nested(b):
        return b * a
    
    a = nested(a)
    return a

print(outer(4))

def f(a):
    def g(b):
        def h(c):
            return a * b * c
        return h
    return g

print(f(5)(2)(3))

#recursive function
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

#regular recursion
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

def tail_sum(n, accumulator = 0):
    if n == 0:
        return accumulator
    else:
        return tail_sum(n-1, accumulator+n)

print(sum(10))
print(tail_sum(10))

#lambda function
f = lambda a: lambda b: lambda c: a * b * c
print(f(5)(2)(3))

g = lambda c: lambda a, b:lambda d: (c * (a + b )) % d
print(g(2)(4,3)(11))