

def poly_add(f,g):
    a = len(f)
    b = len(g)
    l = max(a,b)
    h = [0]*l
    for i in range(0,l):
        if(i < a):
            h[i] += f[i]
        if(i < b):
            h[i] += g[i]
        h[i] = h[i]%2
    
    k = l-1
    while(k > 0):
        if(h[k] == 0):
            k -= 1
        else:
            break
    if(k == -1):
        return []
    return h[0:k+1]


def poly_mul(f,g):
    a = len(f)
    b = len(g)
    h = [0]*(a+b-1)
    for i in range(0,a+b-1):
        for j in range(0,a):
            if(j > i):
                break
            k = i-j
            if(k > b-1):
                continue
            h[i] += f[j]*g[i-j]
        h[i] = h[i]%2
    
    return h

#Divide f by g, i.e. output q and r
#such that f=q*g+r and deg(r)<deg(g).
def poly_division(f,g):
    a = len(f)-1
    b = len(g)-1

    if(a < b):
        return [],f
    
    #Assume now a >= b
    #Quotient
    q = [0]*(a-b+1)
    r = f
    
    c = 0
    while(a >= b):
        #print(r,a,b)
        c += 1
        q[a-b] = 1
        t = r
        xr = [0]*(a-b)+g
        r = poly_add(xr,r)
        a = len(r)-1
        #print(xr)
        #print(r)
        #print()
        if(r == [] or r == [0]):
            return q,r
    return q,r

print()
f = [0,1,1,1,0,1]
g = [0,1,0,1]
print(f)
print(g)
q,r = poly_division(f,g)
print(q,r)

print()

#Compute f mod g.
def poly_mod(f,g):
    #f = qg+r
    q,r = poly_division(f,g)
    
    return r

#Computes gcd of f and g
def poly_gcd(f,g):
    a = len(f)-1
    b = len(g)-1

    if(a<b):
        f,g = g,f

    q,r = poly_division(f,g)
    if(r == [0] or r == []):
        return g
    return poly_gcd(g,r)


print(poly_gcd(f,g))

primes = [2,3,5,7,11,13,17,19]
def is_irred(f):
    n = len(f)-1
    pfs = []
    for p in primes:
        if(n%p == 0):
            pfs.append(p)
    for i in pfs:
        ni = n//i
        h = [0]*(2**ni+1)
        h[1] = 1
        h[2**ni] = 1
        g = poly_gcd(f,h)
        if(g != [1] and g != []):
            #print(f,g,h)
            return False
    g = [0]*(2**n+1)
    g[2**n] = 1
    g[1] = 1
    g = poly_mod(g,f)
    if(g == [0]):
        return True
    return False
print()
print("ABE")
print(is_irred([0,1]))

c = 0
res = 0
goal = 5*10**6
print()
for i in range(2,10**9):
    print(i)
    z = bin(i)[2:][::-1]
    f = [int(k) for k in list(z)]
    if(is_irred(f)):
        c += 1
        if(c == goal):
            print(i)
            res = i

print()
print("RESULTAT")
print(res)


































