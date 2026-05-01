
n = int(input("Enter number: "))
num = n 
rev = 0

while num > 0:
    rev = rev*10 + num%10
    num = num // 10

print(f"Reverse of {n} is {rev}")