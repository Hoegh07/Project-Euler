def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for i in range(0,limit):
        if(a[i] == True):
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


A = [1]*(10**7+1)
for i in range(2,10**4+1):
    if(i*i > 10**7):
        break
    for j in range(i*i,10**7+1,i*i):
        A[j] = 0
sqfree = [0,1]
for i in range(2,10**7+1):
    sqfree.append(sqfree[i-1]+A[i])

memo = {}
def no_sqfree(n):
    return n-powerful(primes,n,2,1,0,1)
    if(n <= 10**7):
        return sqfree[n]
    elif(n in memo):
        return memo[n]
    else:   
        c = n-powerful(primes,n,2,1,0,1)
        memo[n] = c
        return c

def solve(P,N,prod,pos,k,depth):
    total = 0
    for i in range(pos+1,len(P)):
        e = 2
        c = N//(prod*P[i]**e)
        if(prod*P[i]**(e*(k-depth)) > N):
            break
        while(c > 0):
            if(depth == k-1):
                total += no_sqfree(c)
            else:
                total += solve(P,N,prod*P[i]**e,i,k,depth+1)
            e += 2
            c = N//(prod*P[i]**e)
    return total


N = 10**16
pri = sieve(int(N**0.5)+1)
primes = [p for p in pri]
MOD = 1000000007
LIM = int(N**0.5)+1
res = N-powerful(primes,N,2,1,0,1)
print(0,res)
k = 1
c = 1
while(True):
    c = solve(primes,N,1,-1,k,0)
    if(c == 0):
        break
    res = (res*c)%MOD
    print(k,c)
    k += 1
print()
print("Resultat:")
print(res)




















































