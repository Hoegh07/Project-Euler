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
def power(x,n):
    y = [1,0]
    for i in range(n):
        y = mul(y,x)
    return y

N = 10**5+1
A = [0]*(N+1)
B = [0]*(N+1)
is_prime,primes,smpf = sieve(N)
print("FÆRDIG MED SI")
for a in range(1,10**4+10):
    for b in range(a,10**4+10):
        if(math.gcd(a,b) > 1):
            continue
        x = a**2+b**2
        if(x >= N-1):
            break
        if(is_prime[x]):
            A[x] = a
            B[x] = b

def Gdivisors(P,v):
    div = [[1,0]]
    for i in range(0,len(P)):
        p = P[i]
        u = []
        for d in div:
            for e in range(1,v[i]+1):
                u.append(mul(d,power(p,e)))
        div = div+u
    return div


print()
res = 1
for n in range(2,N):
    if(n%10000 == 2):
        print(n)
    P = []
    v = []
    x = n
    while(x > 1):
        p = smpf[x]
        if(p == 2):
            a = 1
            b = 1
        elif(p%4 == 1):
            a = A[p]
            b = B[p]
        else:
            a = p
            b = 0

        e = 0
        while(x%p == 0):
            e += 1
            x = x//p

        if(p==2 or p%4==1):
            P.append([a,b])
            P.append([a,-b])
            v.append(e)
            v.append(e)
        else:
            P.append([a,b])
            v.append(e)
    div = Gdivisors(P,v)
    q = 0
    udiv = []
    for d in div:
        if(d[0] > 0):
            udiv.append(d)
        else:
            udiv.append([-d[0],-d[1]])
        d = mul(d,[0,1])
        if(d[0] > 0):
            udiv.append(d)
        else:
            udiv.append([-d[0],-d[1]])

    udiv = sorted(udiv)
    udiv.append([-1,0])
    q = 0
    t = udiv[0]
    for l in range(1,len(udiv)):
        if(udiv[l] != t):
            q += t[0]
            t = udiv[l]
    res += q
    
    if(n in [5,5**2,5**3,5**4,5**5]):
        print(n,q)


#PRØV AT FINDE EN STRUKTUR AF 
#SUMMEN AF POSITIVE DIVISORER
#MULIGVIS DELVIS MULTIPLIKATIV
print(res)
print(17924657155)




















































































