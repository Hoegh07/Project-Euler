import math

def sieve(limit):
    a = [1] * limit
    a[0] = a[1] = 0
    smpf = [0] * limit
    primes = []

    for i in range(limit):
        if(a[i]):
            primes.append(i)
            smpf[i] = i
            for j in range(i*i,limit,i):
                a[j] = 0
                if(smpf[j] == 0):
                    smpf[j] = i
                    
    return a,primes,smpf

def add(x,y):
    return [x[0]+y[0],x[1]+y[1]]
def mul(x,y):
    return [x[0]*y[0]-x[1]*y[1],x[0]*y[1]+x[1]*y[0]]


N = 10**5
A = [0]*(N+1)
B = [0]*(N+1)
is_prime,primes,smpf = sieve(N)

for a in range(1,10**3+1):
    for b in range(a,10**3+1):
        if(math.gcd(a,b) > 1):
            continue
        x = a**2+b**2
        if(x > N):
            break
        if(is_prime[x]):
            A[x] = a
            B[x] = b

