a = int(input("Number 1: "))
b = int(input("Number 2: "))
c = int(input("Number 3: "))

print("The largest is: ",end="")
if(a > b and a > c):
    print(a)
elif(b > a and b > c):
    print(b)
else:
    print(c)