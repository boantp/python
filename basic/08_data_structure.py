#Data Structure

'''
Tupple
'''

tup = (1, 'abc', 2, 'cde')
tup1 = 3, 'efg', True

tup2 = 'A' # tup2 = ('A',)

#tupple cannot item assignment
#tup[3] = 5
#item assignment only with concat and override variable
tup = tup[0:3] + (5,)
print(tup)
print(tup2 * 4)
#check value in tupple
print(5 in tup) #true if exist

#tupple really usefull for multiple result
for x in ('a', 'b', 'c'):
    print(x)

def multiple_result():
    return(1,2,'a')

print(multiple_result())

print((1,2) == (1,2,3)) #False

#function tupple : len, max, min
print(len(tup))
print(max(tup))
print(min(tup))

'''
List
'''
list1 = [1, 'abc', (2,3)]
print(list1[2][0]) #2
print(2 in list1) #false
print(list1[:2]) #[1, 'abc']

#tools append
list1.append(6)
list1[len(list1):] = [7]
print(list1)

#function list: map, filter, reduce, append
print(map(lambda x: x**2  + 3*x + 1, [1,2,3,4])) #[5, 11, 19, 29]
print(filter(lambda x: x < 4, [1,2,3,4,5,4,3,2,1])) #[1, 2, 3, 3, 2, 1]
print(reduce(lambda x, y: x * y, [1,2,3,4])) #24 => 1x2 -> (1x2)x3 -> ((1x2)x3)x4

'''
Dictionaries
'''
my_dict = {'key': 'value', ('k', 'e', 'y') : 5}
print(my_dict.keys())
print(my_dict.values())
#unlike tupple cannot item assignment, dict can set key value for data
my_dict[1] = 3
print(my_dict)

my_dict1 = {x: x + 1 for x in range(10)}
print(my_dict1)

#function dictionary: del, clear, keys, values
del my_dict[1]
print(my_dict)
my_dict.clear()
print(my_dict)

'''
Shallow copy
'''
my_dictionaries = {'item': 'shirt', 'size': 'medium', 'price': 50}
my_dictionaries1 = my_dictionaries

print(my_dictionaries)
my_dictionaries['size'] = 'small'
print(my_dictionaries1) 

'''
Sets
'''
my_set = set(['one', 'two', 'three', 'one'])
my_set1 = set(['two', 'three', 'four'])
print(my_set)


#arithmetic: |(union), ^(intersection) , -(sort of diff or the unique one)
print(my_set1 | my_set) #set(['four', 'one', 'two', 'three'])
print(my_set1 ^ my_set) #set(['four', 'one'])
print(my_set1 - my_set) #set(['four'])

#function set : add, union, intersection, difference
my_set.add('five')
print(my_set) #set(['three', 'five', 'two', 'one'])
print(set.difference(my_set1, my_set))
print(set.union(my_set1, my_set))
print(set.intersection(my_set1, my_set))