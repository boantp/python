class Complex:
    'this class simulates complex numbers'
    def __init__(self,real=0,imag=0):

        #self.__real = real
        #self.__imag = imag
        self.SetReal(real)
        self.SetImag(imag)

    def GetReal(self):
        return self.__real
    def GetImag(self):
        return self.__imag
    def SetReal(self, val):
        self.__real = val
    def SetImag(self, val):
        self.__imag = val
    def __str__(self):
        return str(self.GetReal()) + '+' + str(self.GetImag())
    #operator overloading
    def __add__(self, other):
        return Complex(self.GetReal() + other.GetReal(), self.GetImag() + other.GetImag())

c = Complex(2.5, 5.2)
print(c.GetReal(),c.GetImag())

c = Complex()
c.SetImag(1)
c.SetReal(2)
print(c.GetReal())
print(c.GetImag())

#operator overloading
a = Complex(5, 0.3)
b = Complex(-3, 4)
print(a + b)