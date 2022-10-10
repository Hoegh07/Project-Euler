def M(n):
    return (n+1)**2-1

def T(n):
    return (n*(n+1))//2


c = 0
for i in range(1,10**3):
    b = False
    low = 0
    high = 10**30
    x = M(i)
    while(high-low > 1):
        mid = (low+high)//2
        if(T(mid) < x):
            low = mid
        else:
            high = mid

    if(x == T(low) or x == T(high)):
        c += 1
        print(i,M(i),c)
    if(c == 40):
        print(i)


print()
#a(n) = 35*(a(n-2) - a(n-4)) + a(n-6)

def a(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 3
    if(n == 2):
        return 15
    if(n == 3):
        return 120
    if(n == 4):
        return 528
    if(n == 5):
        return 4095
    if(n == 6):
        return 17955
    return 35*(a(n-2)-a(n-4))+a(n-6)

res = 0
for i in range(1,41):
    res += int((a(i)+1)**0.5)-1
print(res)



















