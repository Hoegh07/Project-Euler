MOD = 987654321
N = 10**18

def P(k):
    if(k == 1):
        return 1
    if(k%2 == 0):
        return k-2*(P(k//2)-1)
    if(k%2 == 1):
        return k-2*(P(k//2)-1)-1

def S(n):
    if(n == 1):
        return 1
    if(n%2 == 0):
        return 1+2*n+2*(n//2)*(n//2+1)-4*S(n//2)-P(n)
    if(n%2 == 1):
        return 1+2*(n-1)+2*(n//2)*(n//2+1)-4*S(n//2)

print(S(N)%MOD)



































