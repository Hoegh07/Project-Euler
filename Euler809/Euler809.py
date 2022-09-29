import sys
sys.setrecursionlimit(2000)


def g(x):
    if(x == int(x)):
        return x
    if(x < 1):
        return f(1/(1-x))
    return f(1/(int(x+1)-x)-1+f(x-1))

#print(f(1/6))

#print(f(1,6))
import math
memo_f = {}
def f(p,q):
    print(p,q)
    if((p,q) in memo_f):
        return memo_f[(p,q)]
    if(p%q == 0):
        return p,q
    elif(p<q):
        c = f(q,q-p)
        memo_f[(p,q)] = c
        return c
    
    r = p%q
    #print(p,q,r)
    r = p%q
    tmp = f(p-q,q)
    pp = tmp[0]
    qq = tmp[1]
    
    ppp = r
    qqq = q-r

    A = ppp*qq+pp*qqq
    B = qq*qqq
    d = math.gcd(A,B)
    A = A//d
    B = B//d
    return f(A,B)


print(f(3,2))

def F(p,q):
    if(p%q == 0):
        return p//q,1
    if(p < q):
        return F(q,q-p)

    r = p%q
    k = p//q
    #print(p,q,r)
    
    k = 0
    for l in range(1,p):
        if(l > p/q-1):
            k = l
            break

    tmp = F(p-k*q,q)
    pp = tmp[0]
    qq = tmp[1]

    ppp = k*r
    qqq = q-r
    A = ppp*qq+pp*qqq
    B = qq*qqq
    d = math.gcd(A,B)
    A = A//d
    B = B//d
    return F(A,B)

print()
print(F(1,5))
print()
print(f(1,5))




























