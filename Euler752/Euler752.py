import math
from functools import reduce

def sieve(limit):
    a = [1] * limit
    primes = []
    smpf = [-1]*limit
    a[0] = a[1] = False
    
    for i in range(2,limit):
        if(a[i] == 1):
            primes.append(i)
            smpf[i] = i
            for j in range(i*i,limit,i):
                if(smpf[j] == -1):
                    smpf[j] = i
                a[j] = 0

    return primes,smpf


def AB(x):
    A = [1,1]
    B = [0,1]
    for i in range(2,10000):
        a = 2*A[i-1]+6*A[i-2]
        b = 2*B[i-1]+6*B[i-2]
        a = a%x
        b = b%x
        A.append(a)
        B.append(b)

        if(a == 1 and b == 0):
            return i
    return 0


def matmul(a,b,m):
    return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0])%m,(a[0][0]*b[0][1]+a[0][1]*b[1][1])%m],
            [(a[1][0]*b[0][0]+a[1][1]*b[1][0])%m,(a[1][0]*b[0][1]+a[1][1]*b[1][1])%m]]


def matexp(A,n,m,powers):
    res = [[1,0],[0,1]]
    z = str(bin(n)[2:])[::-1]
    for i in range(0,len(z)):
        if(z[i] == '1'):
            res = matmul(res,powers[i],m)
    return res


def factors(n):    
    return sorted(set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))


def G(x):
    A = [[1,7],[1,1]]
    powers = [A]
    d = 1
    X = A
    while(2*d <= x**2):
        d *= 2
        X = matmul(X,X,x)
        powers.append(X)

    fac = []
    fac1 = factors(x+1)
    fac2 = factors(x-1)
    for f1 in fac1:
        for f2 in fac2:
            fac.append(f1*f2)
    fac = sorted(list(set(fac)))
     
    for f in fac:
        X = matexp(A,f,x,powers)
        if(X[0][0] == 1 and X[1][0] == 0):
            return f
    return 0

def lcm(a,b):
    return (a*b)//math.gcd(a,b)

def lcm_a(A):
    res = 1
    for a in A:
        res = lcm(res,a)
    return res

N = 10**6
primes,smpf = sieve(N)
B = [0]*(N+1)

c = 0
for p in primes:
    if(p in [2,3]):
        continue
    B[7] = 7
    B[p] = G(p)
    c += 1
    if(c%1000 == 0):
        print(c)

def g(x):
    A = []
    p = smpf[x]
    z = x
    while(z>1):
        y = p
        r = B[p]
        while(x%(p*y) == 0):
            y *= p
            r *= p
        A.append(r)
        z = z//y
        p = smpf[z]
    return lcm_a(A)

res = 0
for i in range(2,N+1):
    if(i%2 == 0 or i%3 == 0):
        continue
    res += g(i)
print(res)














