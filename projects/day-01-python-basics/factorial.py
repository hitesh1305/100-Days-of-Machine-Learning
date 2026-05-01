
num = int(input("Enter n: "))

fact = 1
i = num
while i > 0:
    fact *= i
    i-=1
    
print(f"Factorial of {num} is {fact}")