import math


def mex(A):
    m = 0
    for a in A:
        m = max(m,a)
    for i in range(0,m+2):
        if(i not in A):
            return i


g = {}
g[(0,0)] = 0
def grundy(a,b):
    if((a,b) in g):
        return g[(a,b)]

    if(math.gcd(a,b) > 1):
        g[(a,b)] = 0
        return 0
    
    B = []
    for c in range(0,a+1):
        for d in range(0,b+1):
            if(a*d-b*c in [-1,1]):
                B.append(grundy(a-c,b-d))
    v = mex(B)
    g[(a,b)] = v
    return v

res = 0
for a in range(1,101):
    for b in range(1,101):
        if(math.gcd(a,b) > 1):
            continue
        if(a+b > 100):
            break
        if(grundy(a,b) > 0):
            res += 1
print(res)


















