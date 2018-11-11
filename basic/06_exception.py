try:
    sum = 0
    file = open('numbers.txt', 'r')
    for number in file:
        sum = sum + 1.0/int(number)
    print(sum)
except ZeroDivisionError:
    print("Number in file equal to zero!")
except IOError:
    print("File DNE")
finally:
    print(sum)
    #file.close()

#Exception Handling
a = 1
def RaiseException(a):
    if type(a) != type('a'):
        raise ValueError("This is not a string")

try:
    RaiseException(a)
except ValueError as e:
    print(e)

def TestCase(a , b):
    assert a < b, "there is an error expected a not greater than b"

try:
    TestCase(2,1)
except AssertionError as e:
    print(e)