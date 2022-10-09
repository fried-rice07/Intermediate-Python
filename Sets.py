# Sets : unordered, mutable, no duplicates
myset = set("Hello")

#Adding
myset.add(1)
myset.add(2)
myset.add(3)
myset.discard(1)
print(myset)
#iterate in loop
for i in myset:
    print(i)
if 2 in myset:
    print("YES")

odds = {1,3,5,7,9}
evens = {0, 2,4,6,8}
primes = {2,3 ,5 ,7}
u  = odds.union(evens) #calculate the union
print( u)
i = odds.intersection(primes)  # calculate the intersection
print(i)

setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}
diff  = setA.difference(setB) #difference
print(diff)
diff1 = setA.symmetric_difference(setB) #symmetric difference
print(diff1)

setA.intersection_update(setB) #keeping the both numbers in the set
print(setA)

print(setA.issubset(setB)) #subset
print(setA.issuperset(setB)) #super set

#frozen set
a = frozenset([1,2,3,4])

