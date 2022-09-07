#Beregner kædebrøkrepræsentation af x
from decimal import *

getcontext().prec = 80


def cf_repr(x,d):
    a = [0,0,int(x)]
    f = Decimal(1/(Decimal(Decimal(x)-int(x))))
    p = [0,1]
    q = [1,0]
    i = 2
    #convergents = []
    while(q[i-1] <=  d):
        #Get p_i, q_i
        p.append(a[i]*p[i-1]+p[i-2])
        q.append(a[i]*q[i-1]+q[i-2])
        
        #Get a_(i+1)
        a.append(int(f))
        f = Decimal(1/(Decimal(f)-int(Decimal(f))))
        i += 1
    return a,p,q

import math
num = Decimal(4850)
a,p,q = cf_repr(num.sqrt(),10**12)
for t in a:
    print(t)

print("ABE")

def best(x,d):
    #Get all convergents
    a,p,q = cf_repr(x,d)
        
    #Try all semiconvergents
    bestsofar = 2*x
    bestq = Decimal(1)
    bestp = Decimal(10**15)
    for i in range(2,len(p)):
        for j in range(0,a[i]+1):
            pp = Decimal(j*p[i-1]+p[i-2])
            qq = Decimal(j*q[i-1]+q[i-2])
            if(qq == 0):
                continue
            if(pp**2*bestq**2-2*pp*qq*bestq**2*x < bestp**2*qq**2-2*bestp*bestq*qq**2*x and qq<=d):
                bestp = pp
                bestq = qq
    return bestq

print("HALLI HALLO")
N = 10**5
d = 10**12
res = 0
squares = [0]*(N+1)
for i in range(1,int(N**0.5)+1):
    squares[i*i] = 1
for i in range(1,N+1):
    if(i%100 == 1):
        print(i)
    if(squares[i]):
        continue
    res += best(Decimal(i).sqrt(),d)
print(res)
print(57060635927998347)











