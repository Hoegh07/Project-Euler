
print((2**3+2+1)**2)
n = (2**3+2+1)**2

res = 0
for i in range(0,10):
    if(2**i > n):
        continue
    if((n%(2**i)) == (n%(2**(i+1)))):
        continue
        #res += 2**i
        #n -= 2**i
        #print(2**i)
    else:
        print(2**i)
        res += 2**i

print()

from math import factorial as fac

def binom(n,k):
    if(k > n):
        return 0
    return fac(n)//(fac(k)*fac(n-k))

n = 5
c4 = 0
for j in range(0,4):
    c4 += binom(n,j)*binom(n-j,9-3*j)
print(c4)
























