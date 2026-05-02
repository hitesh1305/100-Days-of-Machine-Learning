def nth_fibonacci(n):
    
    #Step 1: Check for base case
    if n <= 1:
        return n
      
    # Step 2: sum of the two preceding 
    # Recursively
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

n = int(input("Enter n: "))

print(nth_fibonacci(n))