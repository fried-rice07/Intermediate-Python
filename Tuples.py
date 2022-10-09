my_tuple =tuple(["Max",28,"Boston"])
print(my_tuple)
item = my_tuple[2]
print(item)
for  i in my_tuple:
    print(i)
if "Max" in my_tuple:
    print("Yes")
else:
    print("No")
my_tuple = ('a','p','p','l','e')
print(my_tuple.count('l'))
print(my_tuple.index('p'))
#convert to list
my_list = list(my_tuple)
print(my_list)
#slicing in tuple
a = (1,2,3,4,5,6,7)
b = a[2:5]
print(b)
#user
my_tuple = "Marcel", 19, "Bulacan"
name,age,city = my_tuple
print(name, age, city)
import sys
my_list = [0,1,2,"Hello",True]
my_tuple = (0,1,2,"Hello",True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")
#time
import timeit
print(timeit.timeit(stmt="[0,1,2,3,4,5]",number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)",number=1000000))
#COncatenate
tuple = [1,2] + [3,]
print(tuple)