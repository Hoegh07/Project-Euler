def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for i in range(2,limit):
        if(a[i] == True): 
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False


N = 10**8
pri = sieve(int(N**0.5))
primes = [p for p in pri]

res = 0
for p in primes:
    if(p**12 <= N):
        res += 1
    if(p**19 <= N):
        res += 1
    if(p**30 <= N):
        res += 1
    if(p**36 <= N):
        res += 1
    if(p**6 <= N):
        res += 1
        print(p)
    else:
        break

D = len(primes)
for i in range(0,D):
    p = primes[i]
    if(p**8 > N):
        break
    for j in range(i+1,D):
        q = primes[j]
        
        if(p**4*q**4 <= N):
            res += 1
            print(p,q)
        if(p**4*q**10 <= N):
            print(p,q)
            res += 1
        if(p**10*q**4 <=N):
            res += 1
            print(p,q)
        if(p**4*q**16 <= N):
            res += 1
            print(p,q)
        if(p**16*q**4 <=N):
            res += 1
            print(p,q)

print("RESULTAT")
print(res+1)


print()
res = 0
N = 10**3
A = [1]*(N+1)
for i in range(2,N+1):
    for j in range(i,N+1,i):
        A[j] += 1
        if(A[j] == 7):
            A[j] = 1
for i in range(1,N+1):
    if(A[i] == 1):
        print(i)
        res += 1
print(res)


print()

pri = sieve(N)
primes = [p for p in pri]

def powerful(P,N,p,prod,pos,s):
    total = 0
    for i in range(pos,len(P)):
        prodd = prod*P[i]
        c = N//(prodd**p)
        if(c < 1):
            break
        total += c*s+powerful(P,N,p,prodd,i+1,s*(-1))
    return total


N = 10**36
pri = sieve(5*10**8)
primes = [p for p in pri]
print()
print("ABE")
def solve(P,N,ndiv,prod,pos):
    total = 0
    if(ndiv%6 in [0,2,3,4]):
        return 0
    for i in range(pos,len(P)):
        j = 4
        p = P[i]
        if(prod*p**4 > N):
            break
        while(p**j*prod <= N):
            if((j+1)%6 == 3):
                j += 2
                continue
            if(((j+1)*ndiv)%6 == 1):
                total += 1
            total += solve(P,N,((j+1)*ndiv)%6,p**j*prod,i+1)
            j += 2
            
    return total

print("VI BEGYNDER")
print(solve(primes,N,1,1,0)+1)












