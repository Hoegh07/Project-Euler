MOD = 1000000007 

def f(n):
    b = 0
    y = str(bin(n)[2:])
    for j in range(0,len(y)):
        if(y[j] == '1'):
            b += 1
    return b*n

def T(n):
    return ((n*(n+1))//2)

#Formel for summen H(1)+H(2)+...+H(n), hvor H betegner Hamming vægten.
memo_Sb = {}
def Sb(n):
    if(n in memo_Sb):
        return memo_Sb[n]
    if(n == 0):
        return 0
    if(n%2 == 0):
        c = (Sb(n//2)+Sb(n//2-1)+n//2)%MOD
        memo_Sb[n] = c
        return c
    c = (2*Sb(n//2)+n//2+1)%MOD
    memo_Sb[n] = c
    return c

#Regner summen f(1)+f(2)+f(3)+...+f(n) rekursivt.
memo_S1 = {}
def S1(n):
    if(n in memo_S1):
        return memo_S1[n]
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    if(n%2 == 0):
        c = (f(1)+f(n)+4*S1(n//2-1)+Sb(n//2-1)+2*T(n//2-1)+(n//2-1))%MOD
        memo_S1[n] = c
        return c
    c = (f(1)+4*S1(n//2)+Sb(n//2)+2*T(n//2)+(n//2))%MOD
    memo_S1[n] = c
    return c

N = 100

print("TEST sum f(1)+f(2)+...+f(n)")
res = 0
for i in range(1,N+1):
    res += f(i)
print(res)
print(S1(N))

print()
#Tæller antal satte bits i n 2-adisk ekspansion
def b(n):
    y = str(bin(n)[2:])
    res = 0
    for i in range(0,len(y)):
        if(y[i] == '1'):
            res += 1
    return res

print("Test sum b(1)+b(2)+...+b(n)")
res = 0
for i in range(1,N+1):
    res += b(i)
print(res)
print(Sb(N))

print()

print("Test sum b(1)²+b(2)²+...+b(n)²")
res = 0
for i in range(1,N+1):
    res += b(i)**2
print(res)

memo_Sb2 = {}
def Sb2(n):
    if(n in memo_Sb2):
        return memo_Sb2[n]
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    if(n%2 == 0):
        c = (1+b(n)**2+2*Sb2(n//2-1)+2*Sb(n//2-1)+n//2-1)%MOD
        memo_Sb2[n] = c
        return c
    c = (1+2*Sb2(n//2)+2*Sb(n//2)+n//2)%MOD
    memo_Sb2[n] = c
    return c

print(Sb2(N))

print()

print("Test sum b(1)*1²+b(2)*2²+...+b(n)*n²")
res = 0
for i in range(1,N+1):
    res += b(i)*i**2
print(res)

def sos(n):
    return (n*(n+1)*(2*n+1))//6

memo_Sbn2 = {}
def Sbn2(n):
    if(n in memo_Sbn2):
        return memo_Sbn2[n]
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    if(n%2 == 0):
        c = (1+b(n)*n**2+8*Sbn2(n//2-1)+4*S1(n//2-1)+Sb(n//2-1)+(n//2-1)+4*T(n//2-1)+4*sos(n//2-1))%MOD
        memo_Sbn2[n] = c
        return c
    c = (1+8*Sbn2(n//2)+4*S1(n//2)+Sb(n//2)+(n//2)+4*T(n//2)+4*sos(n//2))%MOD
    memo_Sbn2[n] = c
    return c

print(Sbn2(N))

print()

print("Test sum b(1)²+b(2)²+...+b(n)²")
res = 0
for i in range(1,N+1):
    res += b(i)**2
print(res)

memo_Sb2 = {}
def Sb2(n):
    if(n in memo_Sb2):
        return memo_Sb2[n]
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    if(n%2 == 0):
        c = (1+b(n)**2+2*Sb2(n//2-1)+2*Sb(n//2-1)+n//2-1)%MOD
        memo_Sb2[n] = c
        return c
    c = (1+2*Sb2(n//2)+2*Sb(n//2)+n//2)%MOD
    memo_Sb2[n] = c
    return c

print(Sb2(N))


memo_Sb2n = {}
def Sb2n(n):
    if(n in memo_Sb2n):
        return memo_Sb2n[n]
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    if(n%2 == 0):
        c = (1+b(n)**2*n+4*Sb2n(n//2-1)+4*S1(n//2-1)+Sb2(n//2-1)+2*Sb(n//2-1)+2*T(n//2-1)+n//2-1)%MOD
        memo_Sb2n[n] = c
        return c
    c = (1+4*Sb2n(n//2)+4*S1(n//2)+Sb2(n//2)+2*Sb(n//2)+2*T(n//2)+n//2)%MOD
    memo_Sb2n[n] = c
    return c

print()
print("Test sum b(1)²*1+b(2)²*2+...+b(n)²*n")
res = 0
for i in range(0,N+1):
    res += b(i)**2*i
print(res)
print(Sb2n(N))

print()

print("Test endelige sum, dvs. f(1)²+f(2)²+...+f(n)²")

memo_S2 = {}
def S2(n):
    if(n in memo_S2):
        return memo_S2[n]
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    if(n%2 == 0):
        a = n//2-1
        c = (f(1)+f(n)**2+8*S2(a)+8*Sbn2(a)+4*sos(a)+4*Sb2n(a)+8*S1(a)+4*T(a)+Sb2(a)+2*Sb(a)+a)%MOD
        memo_S2[n] = c
        return c
    a = n//2
    c = (f(1)+8*S2(a)+8*Sbn2(a)+4*sos(a)+4*Sb2n(a)+8*S1(a)+4*T(a)+Sb2(a)+2*Sb(a)+a)%MOD
    memo_S2[n] = c
    return c

res = 0
for i in range(1,N+1):
    res += f(i)**2
print(res)
print(int(S2(N)))

print()

print("SVAR PÅ OPGAVEN")
N = 10**16
print(int(S2(N)))

































