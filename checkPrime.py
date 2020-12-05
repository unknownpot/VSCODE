T = int(input())
for k in range(T):
    primes = []
    low, high = map(int, input().split())    
    for possiblePrime in range(low, high+1):
    
        # Assume number is prime until shown it is not. 
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        
        if possiblePrime == 1:
            isPrime = False
            
        if isPrime:
            primes.append(possiblePrime)

    for i in primes:    
        print(i, end=' ')
    print('')