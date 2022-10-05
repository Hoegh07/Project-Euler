import numpy as np


#A = np.array([[1,1,0],[0,1,1],[1,1,1]])

#B = np.dot(A,A)
#B = np.dot(B,B)

#for b in B:
#    print(b)

#print()

MOD = 20092010
#g = [1 for i in range(0,2000)]
#for i in range(2000,10**6):
#    g.append((g[i-2000]+g[i-1999])%MOD)
#print(g[6000])


A = np.array([0]*2000)
A[0] = 1
A[1] = 1

for i in range(1,1999):
    a = np.array([0 for i in range(0,2000)])
    a[i] = 1
    a[i+1] = 1
    A = np.vstack([A,a])
a = np.array([0 for i in range(0,2000)])
a[1999] = 1
a[0] = 1
a[1] = 1
A = np.vstack([A,a])


import time
start_time = time.time()

#print(bin(6)[2:])
N = 2000*58
#N = (10**18)//2000

G = [1 for i in range(0,2000)]
for i in range(2000,N+1):
    G.append((G[i-2000]+G[i-1999])%MOD)
print("BRUTE FORCE")
print(G[N])


print()
MOD = 20092010
##########################
#FJERN HVIS TJEK KORREKTED
N = 10**18
##########################
N = N//2000
z = bin(N)[2:][::-1]
if(z[0] == '1'):
    RES = A
else:
    RES = np.identity(2000)

A = A.astype(int)
RES = RES.astype(int)

for i in range(1,100):
    print(i)
    if(i > len(z)-1):
        break
    
    A = np.dot(A,A)
    A = A.astype(int)
    for a in A:
        for j in range(0,len(a)):
            a[j] = a[j]%MOD
    if(z[i] == '1'):
        RES = np.dot(RES,A)
        RES = RES.astype(int)
    for r in RES:
        for j in range(0,len(r)):
            r[j] = r[j]%MOD

b = np.ones(2000)
c = np.dot(RES,b)
print("RESULTAT")
print(int(c[0])%MOD)

print("--- %s seconds ---" % (time.time() - start_time))





















