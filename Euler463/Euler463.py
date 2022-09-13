memof = {1:1,3:3}

def f(n):
    if(n in memof):
        return memof[n]
    if(n%2 == 0):
        a = f(n//2)
        memof[n] = a
        return a
    if(n%4 == 1):
        k = (n-1)//4
        a = 2*f(2*k+1)-f(k)
        memof[n] = a
        return a
    if(n%4 == 3):
        k = (n-3)//4
        a = 3*f(2*k+1)-2*f(k)
        memof[n] = a
        return a

memo = {1:1,2:2,3:5}
def S(N):
    if(N in memo):
        return memo[N]

    n = N//4
    if(N%4 == 0):
        a = (6*(S(2*n+1)-1)-8*S(n)-f(4*n+1)-f(4*n+2)-f(4*n+3)+5)
        memo[N] = a
        return a
    if(N%4 == 1):
        a = (6*(S(2*n+1)-1)-8*S(n)-f(4*n+2)-f(4*n+3)+5)
        memo[N] = a
        return a
    if(N%4 == 2):
        a = (6*(S(2*n+1)-1)-8*S(n)-f(4*n+3)+5)
        memo[N] = a
        return a
    if(N%4 == 3):
        a = (6*(S(2*n+1)-1)-8*S(n)+5)
        memo[N] = a
        return a

MOD = 10**9
N = 3**37
print(S(N)%MOD)






























