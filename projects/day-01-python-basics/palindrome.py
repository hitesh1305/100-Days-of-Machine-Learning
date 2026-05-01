
n = int(input("Enter a number: "))
num = n
rev = 0

while num > 0:
    rev = rev*10 + num%10
    num = num // 10


if n == rev:
    print(f"{n} is palindrome")

else:
    print(f"{n} is not palindrome")