
def isPrime(n):

    #Step 1: check if number is <= 1, if yes then its not prime
    if n <= 1:
        return False
    
    #Step 2: Check for all other positive numbers
    for i in range(2,n):
        
        #If n is divisible by any other number except 1 and itself then not prime 
        if n%i == 0:
            return False
        
    #If all the numbers completed and n is not divisible then only it will reach till this part of code    
    return True


n = int(input("Enter a number: "))
if(isPrime(n)):
    print(f"{n} is Prime")

else:
    print(f"{n} is not prime")