#inheritance
class Vehicle:
    def __init__(self, VIN, weight, manufacture):
        self.VIN = VIN
        self.weight = weight
        self.manufacture = manufacture
    def GetWeight(self):
        return self.weight
    def GetManufacture(self):
        return self.manufacture

class Car(Vehicle):
    def __init__(self, VIN, weight, manufacture, seat):
        self.VIN = VIN
        self.weight = weight
        self.manufacture = manufacture
        self.seat = seat
    def NumberOfSeats(self):
        return self.seat
    def VehicleType(self):
        return 'CAR'

class Truck(Vehicle):
    def __init__(self, VIN, weight, manufacture, capacity):
        self.VIN = VIN
        self.weight = weight
        self.manufacture = manufacture
        self.capacity = capacity
    def TransportCapacity(self):
        return self.capacity
    def VehicleType(self):
        return 'Truck'

a = Car('ABC1', 1000, 'BMW', 4)
b = Truck('XYZ', 5000, 'HINO', 2)
c = Car('ABC2', 1100, 'TOYOTA', 7)
#rint(a.VIN, a.GetWeight(), a.GetManufacture(), a.NumberOfSeats())
for v in [a,b,c]:
    print(v.VehicleType(), v.GetManufacture())


#inheritance 2
class Complex(object):
    'this class simulates complex numbers'
    def __init__(self,real=0,imag=0):

        #self.__real = real
        #self.__imag = imag
        self.SetReal(real)
        self.SetImag(imag)

    def GetReal(self):
        return self._real
    def GetImag(self):
        return self._imag
    def SetReal(self, real):
        if type(real) not in (int, float):
            raise Exception("Real part must be a number!")
        self._real = real
    def SetImag(self, imag):
        if type(imag) not in (int, float):
            raise Exception("Imag part must be a number!")
        self._imag = imag
    real = property(GetReal, SetReal)
    imag = property(GetImag, SetImag)

c = Complex()
print(c.real, c.imag)

try:
    c.real = (1,2,3)
except Exception as e:
    print(e)


#extra notes oop
class Student(object):
    """Student"""
    number_of_students = 0

    def __init__(self, name, index):
        self.name = name
        self.index = index
        Student.number_of_students += 1

    def __del__(self):
        Student.number_of_students -= 1

s1 = Student('Boan', 1234)
s2 = Student('Tua', 5678)
s3 = Student('Pasaribu', 4321)
print(Student.number_of_students)
del(s1)
del(s2)
s4 = Student('Test', 9876)
print(Student.number_of_students)
    


