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
primes = sieve(N)

A = [0]*(N+1)
def f(s,h,l):
    s += 2**h*3**l
    if(s == 3):
        print(s,h,l)
    if(s <= N):
        A[s] += 1
    else:
        return
    for j in range(l+1,13):
        for k in range(0,h):
            f(s,k,j)

for i in range(0,30):
    print(i)
    f(0,i,0)

res = 0
for p in primes:
    if(A[p] == 1):
        res += p
print(res+3)






















































