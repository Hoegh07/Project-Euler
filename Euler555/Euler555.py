def M(m,k,s,n):
    if(n > m):
        return n-s
    else:
        return M(m,k,s,M(m,k,s,n+k))


def F(m,k,s):
    res = []
    for n in range(1,m+s+1):
        if(n == M(m,k,s,n)):
            res.append(n)
    return res

p = 10
m = 10
res = 0
for s in range(1,p+1):
    for k in range(s+1,p+1):
        for n in range(1,1000+1):
            if(n == M(m,k,s,n)):
                res += n
print(res)

res = 0
for s in range(1,p+1):
    for k in range(s+1,p+1):
        res += sum(F(m,k,s))
print(res)































