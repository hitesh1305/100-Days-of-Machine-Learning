
def findGCD(a,b):

    #Step 1: if remainder is 0 then return GCD
    if a == 0:
        return b
    #Perform recursively until find the GCD
    return findGCD(b%a,a)


a = int(input("Enter a: "))
b = int(input("Enter b: "))
g = findGCD(a, b)
print(g)