date = 15

if date == 1:
    print("start your new month")
elif date == 30:
    print("end your month")
else:
    print("enjoy your day")

#ternary
mydate = 15
myword = "start or end of your month" if mydate == 1 or mydate == 30 else "enjoy your day"
print(myword)

a = 3
a = 7 if 3**2 > 9 else 14
print(a)