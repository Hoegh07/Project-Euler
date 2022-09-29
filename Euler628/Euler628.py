from math import factorial as fac
from itertools import permutations 
import time

MOD = 1008691207
    
#BRUTE FORCE METODE
def nbh(x,n):
    i = x[0]
    j = x[1]

    B = []
    if(i<n-1):
        B.append([i+1,j])
    if(j <n-1):
        B.append([i,j+1])
    return B

for i in range(4,3):
    perm = permutations([j for j in range(i)])
    res = 0
    for pi in perm:
        A = [[0]*i for j in range(i)]
        A[0][0] = 1
        for j in range(i):
            A[j][pi[j]] = -1
        if(A[0][0] == -1):
            continue
        for t in range(0,10):
            for x in range(i):
                for y in range(i):
                    if(A[x][y] == 0 or A[x][y] == -1):
                        continue
                    B = nbh([x,y],i)
                    for b in B:
                        u = b[0]
                        v = b[1]
                        if(A[u][v] == -1):
                            continue
                        A[u][v] = 1
        if(A[i-1][i-1] == 1):
            res += 1
    print(i,res)

print()

start_time = time.time()
n = 10**8

FAC = [1,1]
for i in range(2,n+1):
    FAC.append((FAC[i-1]*i)%MOD)
res = (n-1)*FAC[n-1]

#Vi kan regne "both" på en hurtigere måde -- vi ser at 0!
#optræder n-3 gange, 1! optræder n-4 gange, 2! optræder n-5
#gange og så videre.
both = 0
superdiag = 0
subdiag = FAC[n-2]
for j in range(3,n+1):
    subdiag = (subdiag+FAC[n-j])%MOD
    superdiag = (superdiag+(j-2)*FAC[j-2])%MOD
    both = (both+FAC[j-3]*(n-j+1))%MOD

print("RESULTAT:",(res-subdiag-superdiag+both)%MOD)

print("--- %s seconds ---" % (time.time() - start_time))





#subdiag = 0
#Træk fra hvor underdiagonal lukket
#for i in range(2,n+1):
#    subdiag += FAC[n-i]
#print("low",subdiag)

#Træk fra hvor overdiagonal lukket
#superdiag = 0
#for i in range(3,n+1):
#    superdiag += (i-2)*FAC[i-2]
#print("up",superdiag)

#both = 0
#Læg til hvor både overdiagonal og underdiagonal lukket
#for i in range(2,n+1):
#    for j in range(i+1,n+1):
#        both += fac(j-i-1)
#






























