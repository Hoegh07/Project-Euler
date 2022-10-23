import time


MOD = 10**12
n = 2*10**5

start_time = time.time()
#Regn multipliciteterne...
C = [1,1]
for i in range(2,n+1):
    b = [0]*(i+1)
    b[0] = 1
    b[i] = 1
    for j in range(1,i):
        b[j] = (C[j-1]+C[j])%MOD
    C = b

print("--- %s seconds ---" % (time.time() - start_time))

res = 0
a = [1]
for i in range(1,n+1):
    b = [0]*(i+1)
    b[0] = 1
    b[i] = 1
    c = C[i]

    if(c%MOD == 0):
        res += (i+1)
        continue

    for j in range(1,i):
        b[j] = (a[j-1]+a[j])%MOD
        if((b[j]*c)%MOD == 0):
            res += 1
    a = b

print()
print("RESULTAT")
print(res)














































