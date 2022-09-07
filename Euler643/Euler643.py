import math


def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

N = 10**6
MOD = 1000000007
pri = sieve(N)
phi = [n for n in range(N+1)]
for p in pri:
    for j in range(p,N+1,p):
        phi[j] *= (1-1/p)
for n in range(1,N+1):
    phi[n] = int(phi[n]+0.5)

PHI = [0,0]
for n in range(2,N+1):
    PHI.append(PHI[n-1]+phi[n])
res = 0
for t in range(1,1000):
    m = N//(2**t)
    print(t)
    if(m == 0):
        break
    res += PHI[m]
print(res%MOD)

#Nu skal vi bare implementere den hurtige måde
#at regne phi(1)+phi(2)+phi(3)+...+phi(m)

from math import log as log

def TotientSum(n):
    L = int((n/log(log(n)))**(2/3))
    sieve = [i for i in range(0,L+1)]
    bigV = [0]*(n//L+1)

    for p in range(2,L+1):
        if(p == sieve[p]):
            for j in range(p,L+1,p):
                sieve[j] -= sieve[j]//p
        sieve[p] += sieve[p-1]

    res = 0
    for x in range(n//L,0,-1):
        k = n//x
        res = (k*(k+1))//2

        for g in range(2,int(k**0.5)+1):
            if(k//g <= L):
                res -= sieve[k//g]
            else:
                res -= bigV[x*g]

        for z in range(1,int(k**0.5)+1):
            if(z != k//z):
                res -= (k//z-k//(z+1))*sieve[z]
        
        bigV[x] = res

    return bigV[1]


N = 10**11
res = 0
for t in range(1,1000):
    m = N//(2**t)
    print(t)
    if(m == 0):
        break
    if(m > 100):
        res += TotientSum(m)-1
        continue
    else:
        res += PHI[m]
print(res%MOD)















