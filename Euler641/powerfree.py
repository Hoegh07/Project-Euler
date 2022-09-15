def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False


def powerful(P,N,p,prod,pos,s):
    total = 0
    for i in range(pos,len(P)):
        prodd = prod*P[i]
        c = N//(prodd**p)
        if(c < 1):
            break
        total += c*s+powerful(P,N,p,prodd,i+1,s*(-1))
    return total


N = 10**2
p = 6
pri = sieve(int(N**(1/p))+10)
primes = [p for p in pri]

#print(N-powerful(primes,N,p,1,0,1))
#print(684465067343069)

def solve(P,N,p,prod,pos):
    total = 0
    for i in range(pos,len(P)):
        prodd = prod*P[i]
        c = N//(prodd**p)
        if(c < 1):
            break
        total += (c-powerful(P,c,p,1,0,1))+solve(P,N,p,prodd,i+1)
    return total

print(solve(primes,N,p,1,0)+1)

print()
N = 100
A = [1]*(N+1)
for i in range(2,N+1):
    for j in range(i,N+1,i):
        A[j] = A[j] + 1
        if(A[j] == 7):
            A[j] = 1

for k in range(1,N+1):
    if(A[k] == 1):
        print(k)






























