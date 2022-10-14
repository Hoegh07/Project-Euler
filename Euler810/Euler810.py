#Given bit strings representing polys 
# f=a_0+a_1*x+...+a_(n-1)*x^(n-1)
# g=b_0+b_1*x+...+b_(m-1)*x^(m-1)
#over GF(2), computes the product fg.
def pmul(a,b):
    c = ''
    n = len(a)
    m = len(b)
    for d in range(0,n+m-1):
        temp = 0
        for i in range(0,n):
            if(i > d):
                break
            j = d-i
            if(j > m-1):
                continue
            if(a[i] == '1' and b[j] == '1'):
                temp +=1
            temp = temp%2
        if(temp == 1):
            c = c+'1'
        else:
            c = c+'0'
    return c

N = 2**28
IRR = [[2,3]]
A = [1]*(N+1)
    
print(bin(3)[2:][::-1])

z = bin(3)[2:][::-1]
zz = bin(6)[2:][::-1]
print(pmul(z,zz))

f = bin(2)[2:][::-1]
print(f)
print(pmul(f,f))


def bin_to_nat(b):
    res = 0
    for i in range(0,len(b)):
        if(b[i] == '1'):
            res += 2**i
    return res

N = 1
for i in range(2,N):
    f = bin(i)[2:][::-1]

    for j in range(2,N):
        if(len(str(i))+len(str(j))-1 > 27):
            break
        g = bin(j)[2:][::-1]
        h = pmul(f,g)
        y = bin_to_nat(h)
        
        if(y > N):
            continue
        A[y] = 0
    

print()


#############
#############
#############

#Add two polynomials over GF(2)
def poly_add(f,g):
    h = ''
    for i in range(0,len(f)):
        c = int(f[i])
        if(i < len(g)):
            c += int(g[i])
        c = c%2
        h += str(c)
    
    i = len(h)-1
    while(i > 0):
        if(h[i] == '1'):
            break
        i -= 1
    h = h[0:i+1]
    return h

f = '110101'
g = '101111'
print(f)
print(g)
print(poly_add(f,g))


#Multiply polynomial f by x^d
def poly_mul(f,d):
    return '0'*d+f

print(poly_mul(f,3))

#Compute gcd of polynomials f and g
def poly_gcd(f,g):
    #print(f,g)
    a = len(f)
    b = len(g)
    if(a > b):
        return poly_gcd(g,f)
    
    #a <= b
    h = poly_mul(f,b-a)
    r = poly_add(g,h)
    if(r == '0'):
        return f
    return poly_gcd(r,f)

print()
print(poly_gcd('0101101','010111'))

#Computes f modulo g
def poly_mod(f,g):
    a = len(f)
    b = len(g)
    if(a < b):
        return f
    
    while(a >= b):
        #print(f,g,a-b)
        f =  poly_add(f,poly_mul(g,a-b))
        a = len(f)

    return f


print()
print(poly_mod('1001','11'))

#Test if polynomial over GF(2) is irreducible
def is_irred(f,P):
    n = len(f)-1
    prime_factors = []
    for p in P:
        if(n%p == 0):
            prime_factors.append(p)

    #QWE
    for p in prime_factors:
        if(n%p != 0):
            continue
        m = n//p
        h = '0'*(2**m)
        h = list(h)
        if(len(h) < 2):
            continue
        h[1] = '1'
        h[2**m-1] = '1'
        h = "".join(h)
        h = poly_mod(h,f)
        g = poly_gcd(f,h)
        if(g != '1'):
            return False

    g = '0'*(2**n)
    g = list(g)
    if(len(g) < 2):
        return False
    g[1] = '1'
    g[2**n-1] = '1'
    g = "".join(g)
    g = poly_mod(g,f)
    if(g == ''):
        return False
    return True

primes = [2,3,5,7,11,13]
for i in range(1,20):
    f = bin(i)[2:][::-1]
    if(is_irred(f,primes)):
        print(f)


































