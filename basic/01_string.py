#String
string = 'Boan Tua Pasaribu'
print(string) #Boan Tua Pasaribu
print(string[0]) #B
print(string[-1]) #u
print(string[3:10]) #n Tua P
print(string[15:]) #bu
print(string[:5]) #Boan
print(len(string)) #17

string2 = 'boan' + 'tua' + 'pasaribu'
string3 = 2 * string2
print(string2) #boantuapasaribu
print(string3) #boantuapasaribuboantuapasaribu

string4 = "ford"
string4 = "L" +string4[1:] 
string5 = "C" +string4[:3]
print(string4) #Lord
print(string5) #CLor

#Format Method
print("Ronaldo score {0} goals and dybala make {1} assist".format(3, 2)) #Ronaldo score 3 goals and dybala make 2 assist
print("Ronaldo score {x} goals and dybala make {y} assist".format(x=3, y=2)) #Ronaldo score 3 goals and dybala make 2 assist
print("{striker} score {0} goals and dybala make {1} assist".format(3, 2, striker = 'Ronaldo')) #Ronaldo score 3 goals and dybala make 2 assist

#allign the text, binary, hexadecimal, octal
print('{:<20}'.format("goal")) #goal
print('{:>20}'.format("goal")) #                goal
print('{:b}'.format(21)) #10101
print('{:x}'.format(21)) #15
print('{:o}'.format(21)) #25

#specific character
print(r'c:\number\nan') #c:\number\nan
print("""\
    Hello
        This is a paragraph
            from python
""")
""" output:
    Hello
        This is a paragraph
            from python
"""

