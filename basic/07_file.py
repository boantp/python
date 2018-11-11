#File Managament
#open(filename, access, buffering)

file = open("/home/boan/learning-boan/python/basic/file.txt", "r")
#print(file.read())
print(file.read(4)) #Hell
#file.seek(5) # we set the position to read the file
print(file.tell()) #where we currently read the file #5
print(file.read()) # boan tua pasaribu!
file.close()

files = open("/home/boan/learning-boan/python/basic/file.txt", "r")
# for line in files:
#     print(line)

print("File name :" + files.name)
print("is closed ? :" + str(files.closed))
print("Model :"  + files.mode)
files.close()

myfile = open("/home/boan/learning-boan/python/basic/file.txt", "w+")
myfile.write("Hello file, I am a string")
myfile.seek(0)
myfile.write("This")
myfile.seek(0)
print(myfile.read()) #Thiso file, I am a string
myfile.close()
