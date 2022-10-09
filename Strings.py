list1 = ['1'] * 5
print(list1)
string = ""
for i in list1:
    string += i
print(string)

my_string = "".join(list1)
print(my_string)

# %, format(), f string
#string
var = "Tom"
my_string = "the variable is %s" %var
print(my_string)
# decimal
var = 3
my_string = "the number is %d" %var
print(my_string)
# float
num = 3.11123
my_num = "the float is %.2f" %num
print(my_num)
# another way is
var = 3.12433
var1 = 6
my_string = "the number is {:.2f} and {}".format(var, var1)
print(my_string)
# another way is
num = 5.344355
print(f"the number is {num:.2f}")