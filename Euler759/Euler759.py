def f(n):
    if(n == 1):
        return 1
    if(n%2 == 0):
        return 2*f(n//2)
    if(n%2 == 1):
        m = (n-1)//2
        return n+2*f(m)+1/m*f(m)

for n in range(1,20):
    print(f(n)**2)


















