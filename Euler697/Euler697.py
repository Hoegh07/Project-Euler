import math

#Første forsøg - problemer med at regne gamma cdf
low =  0
high = 10**3 
n = 10**2
c = 0
while(high-low > 0.000001):
    c += 1
    mid = (low+high)/2
    u = math.e**(-mid)
    s = 0
    ss = 0
    t = 1
    f = 1
    for k in range(0,n):
        ss += f*t
        if(k%1000 == 0 or k==n-1):
            s += ss*u
            ss = 0
        t *= mid
        f /= (k+1)
    if(s < 1/4):
        low,high = low,mid
    else:
        low,high = mid,high


print(low/math.log(10,math.e))


#Samme som version 1, men bruger scipys indbyggede gamma-funktion
from scipy.stats import gamma
N = 10**7
low = 0 
high = 10**9 

while(high-low > 0.000001):
    mid = (high+low)/2
    
    pr = gamma.cdf(mid,N)
    if(pr < 0.75):
        low,high = mid,high
    else:
        low,high = low,mid

print(low/math.log(10,math.e))

#Smartere ved brug af metode fra scipy...
print(gamma(N).ppf(0.75)/math.log(10))







