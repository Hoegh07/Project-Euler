import math

res = 0

def P(n,i):
    if(i == 1):
        i = n+1
    res = 0
    for r in range(0,10):
        res += (1/2**(i+n*r))*((i-1)+n*r)
    return res

n = 6
test = 0
for i in range(1,n+1):
    test += P(n,i)
print(test)

def PP(n,i):
    return ((i-1)/(2**i))*(2**n/(2**n-1))+(n/2**i)*(2**n/((2**n-1)**2))

for i in range(1,n+1):
    print(P(n,i),PP(n,i))

print()

n = 10**8+7
i = 10**4+7
MOD = 10**8
num = ((i-1)*pow(2,n-i,MOD)*(pow(2,n,MOD)-1)+pow(2,n-i,MOD)*n)%MOD
denom = ((pow(2,n,MOD)-1)**2)%MOD
print((num*denom)%MOD)









































