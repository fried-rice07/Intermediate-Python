# Write a program to print following pattern
# if input is 5 the output must be
# 5
# 4 5
# 3 4 5
# 2 3 4 5
# 1 2 3 4 5
# rows for i and j for columns
num = int(input())
print(num)
for i in reversed(range(1,5)):
    for j in range(i,num+1):
        print(j,end=" ")
    print()
