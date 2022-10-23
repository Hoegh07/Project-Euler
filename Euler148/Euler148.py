print()
pascal = [[1],[1,1]]
#n = 2*7**2+5*7
#n = 7**4
n = 5*7**3+3*7**2+4*7+6
#n = 7**3
#n = 5*7**3+3*7**2
res = 0
for i in range(2,n):
    A = [1]
    p = pascal[i-1]
    for j in range(0,len(p)-1):
        if((p[j]+p[j+1])%7 == 0):
            res += 1
        A.append((p[j]+p[j+1])%7)
    A.append(1)
    pascal.append(A)
    #if(i == 7**2-1):
    #    print(res)
    #if(i == 7**3-1):
    #    print(res)

def T(k):
    return (k*(k+1))//2

i = 0
for a in pascal:
    #print(i,a)
    i += 1
print("RESULTAT",res)

print()
def dbs(n):
    return 0

#Resultat for n=7²
#print(T(7-1)**2)
#r2 = T(6)**2
#print(r2)

#Resultat for n=7³
#print(T(7)*441+T(6)*T(7**2-1))
#r3 = T(7)*r2+T(6)*T(7**2-1)
#print(r3)

#Resultat for n=7⁴
#r4 = T(7)*r3+T(6)*T(7**3-1)
#print(r4)


#RESULTAT FOR 5*7³
#print()
#res = T(5)*r3+T(4)*T(7**3-1)
#print(res)

r = [0,0,21*21]
for i in range(3,30):
    r.append(T(7)*r[i-1]+T(6)*T(7**(i-1)-1))


#n = 2*7**2+5*7
#res = 0
#res += T(6)*T(6)*3
#res += T(48)
#res += 2*(T(48)-T(13))
#res += 3*T(6)*T(4)
#print("RESULTAT",res)


#n = 5*7³+3*7²+4*7
#res = 0
#res += (T(5)*r[3]+T(4)*T(7**3-1))

#res += 5*(T(7**3-1)-T(7**3-3*7**2-4*7-1))
#res += 6*(T(3)*r[2]+T(2)*T(7**2-1))
#
#zeros = 3*(T(7**2-1)-T(7**2-4*7-1))
#filled = 4*T(3)*T(6)
#
#res += 6*(zeros)
#res += 6*(filled)


n = 5*7**3+3*7**2+4*7+6

res = 0
res += T(4)*T(7**3-1)
res += T(5)*r[3]
res += 5*(T(7**3-1)-T(7**3-1-3*7**2-4*7-6))

u = 6
res += u*T(3)*r[2]
res += u*T(2)*(T(7**2-1))
res += u*3*(T(7**2-1)-T(7**2-1-4*7-6))

u *= 4
res += u*T(3)*T(7**1-1)
res += 4*u*(T(7**1-1)-T(7**1-1-6))


print("RESULTAT",res)




print()


n = 3*7**10
n += 3*7**9
n += 5*7**8
n += 3*7**7
n += 1*7**6
n += 6*7**5
#4
#3
n += 6*7**2
n += 1*7**1
n += 6*7**0

res = 0

#pow = 10
m = n-3*7**10

res += T(3)*r[10]
res += T(2)*T(7**10-1)
res += 3*(T(7**10-1)-T(7**10-m-1))

#pow = 9
u = 4
n = m
m = n-3*7**9

res += u*T(3)*r[9]
res += u*T(2)*T(7**9-1)
res += u*3*(T(7**9-1)-(T(7**9-m-1)))

#pow = 8
u *= 4
n = m
m = n-5*7**8

res += u*T(5)*r[8]
res += u*T(4)*T(7**8-1)
res += u*5*(T(7**8-1)-T(7**8-m-1))

#pow = 7
u *= 6
n = m
m = n-3*7**7

res += u*T(3)*r[7]
res += u*T(2)*T(7**7-1)
res += u*3*(T(7**7-1)-T(7**7-m-1))

#pow = 6
u *= 4
n = m
m = n-1*7**6

res += u*T(1)*r[6]
#T(0)=0
res += u*1*(T(7**6-1)-T(7**6-m-1))

#pow = 5
u *= 2
n = m
m = n-6*7**5

res += u*T(6)*r[5]
res += u*T(5)*T(7**5-1)
res += u*6*(T(7**5-1)-T(7**5-m-1))

#pow = 2
u *= 7
n = m
m = n-6*7**2

res += u*T(6)*r[2]
res +=u*T(5)*T(7**2-1)
res += u*6*(T(7**2-1)-T(7**2-m-1))

#pow = 1
u *= 7
n = m
m = n-1*7

res += u*T(1)*r[1]
#T(0)=0
res += u*1*(T(7**1-1)-T(7**1-m-1))

print(T(10**9)-res)


























