mydict = {"name": "Max", "age":28, "city" : "New York"}
print(mydict)


#copy
mydict_copy = dict(mydict)
mydict_copy["email"] = "mj@"
print(mydict_copy)

#Assigning email
value = mydict["name"]
print(value)
mydict["email"] = "marcelaribal963@gmail.com"
print(mydict)


del mydict["name"] #deleting name in dictionary
print(mydict)
mydict.pop("age") #deleting name in dictionary
print(mydict)
if "name" in mydict:
    print(mydict["lastname"])
try:
    print(mydict["name"])
except:
    print("Error")

for i in mydict: # printing key and value in dictionary
    print(i)
for key, value  in mydict.items():
    print(key, value)

#dictionaries with number
mydict1 = {3: 9, 6: 36, 9: 81}
print(mydict1)
value = mydict1[6]
print(value)
