
def isPrime(n):

    #Step 1: Check is n <=1
    if n<=1:
        return False
    
    #Step 2: Check if it is 2 or 3
    if n == 2 or n == 3:
        return True
    
    #Step 3: Check if it is divisible by 2 or 3
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    '''Step 3 has now eliminated major part,
    now we only check for 6k +-1''' 

    #Step 4: Start from 5 now upto root(n)
    i = 5
    while i*i <=n:

        if n % i ==0 or n % (i+2) == 0:
            return False
        i += 6

    return True


n = int(input("Enter a number: "))
if(isPrime(n)):
    print(f"{n} is Prime")

else:
    print(f"{n} is not prime")