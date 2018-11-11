#range(start, stop, step)
for i in range(1,10,2):
    if i == 3:
        continue
    elif i == 7:
        break
    else:
        print(i) # 1, 6

#string loop
string = 'boan tua pasaribu'
for i in range(len(string)):
    print(string[i]) # boan tua pasaribu

#string loop char
for char in string:
    print(char) # boan tua pasaribu

#10x10 multiplication table
for i in range(1, 11):
    print('{:<3}|'.format(i)),
    for j in range(1, 11):
        print('{:>4}'.format(i * j)),
    if i == 1:
        print('\n{:#^54}'.format("")),

    print("")

#while loop
condition = 5
while condition !=0:
    print(condition)
    condition = condition - 1
    break
        