from math import factorial as fac

def binom(n,r):
    return fac(n)//(fac(r)*fac(n-r))

#Første version
k = 3
n = 7
res = 0
for t in range(0,k):
    if(t*2 > k):
        break
    s = k-t*2
    res += binom(n,s)*binom(n-s,t)*(fac(k)/2**t*(1/n)**k)

print(1-res)


#Version hvor vi undgår overflow
k = 20000
n = 10**6
res = 0
for t in range(0,k):
    if(2*t > k):
        break
    s = k-2*t
    if(t%1000 == 1):
        print(t)
    temp = 1 
    c = 1
    for i in range(n,n-s,-1):
        temp *= (i*c)/(n*(n-i+1))
        c += 1
    for i in range(n-s,n-s-t,-1):
        temp *= (i*c*(c+1))/(((n-s)-i+1)*2*n**2)
        c += 2 
    res += temp

print(1-res)































