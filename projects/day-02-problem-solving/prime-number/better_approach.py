
def isPrime(n):
    #Step 1: Check if n < = 1 then not prime
    if n <=1:
        return False
    

    #Step 2: now we check from 2 to root(n) with i*i <=n
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        i+=1

    #Step 3: if no divisors found then n is prime
    return True

n = int(input("Enter a number: "))
if(isPrime(n)):
    print(f"{n} is Prime")

else:
    print(f"{n} is not prime")