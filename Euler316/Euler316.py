A = [1,0,0,0]

res = 0
for r in range(1,10):
    AA = [0,0,0,0]

    AA[0] = 9*A[0]/10+8*A[1]/10+9*A[2]/10 
    AA[1] = A[0]/10+A[1]/10
    AA[2] =         A[1]/10
    
    A = AA
    res += (r-1)*A[2]/10

def create_mc(n):
    x = str(n)
    prefix = ['']
    for i in range(1,len(x)+1):
        prefix.append(prefix[i-1]+x[i-1])
    
    d = len(x)
    states = [0]*(d+1)
    transitions = [[0]*10 for i in range(d+1)]

    #Hvis jeg er i state s og ser tal j, 
    #så skal jeg gå til denne state.
    for s in range(0,d+1):
        for e in range(s-1,d+1):
            for j in range(0,10):
                #if(s == 2 and e == 4):
                    #print(e,s,x[e-s+1:e]+str(j),prefix[s])
                if(x[e-s+1:e]+str(j) == prefix[s]):
                    transitions[e][j] = s
                    #print(x[e-s+1:e]+str(j),prefix[s])

    #Nu finder vi ss. for at gå imellem
    #de forskellige tilstande
    probs = []
    for i in range(0,d):
        freq = [0]*(d+1)
        for j in range(0,10):
            freq[transitions[i][j]] += 1
        pr = []
        for s in range(0,d+1):
            if(freq[s] > 0):
                pr.append([s,freq[s]])
        probs.append(pr)

    return probs


n = 535
T = create_mc(n)
d = len(T)
A = [0]*(d+1)
A[0] = 1
s = 0
for t in range(1,10**5):
    AA = [0]*(d+1)
    
    for i in range(0,d-1):
        for x in T[i]:
            AA[x[0]] += x[1]*A[i]/10

    #i = d-1
    for x in T[d-1]:
        if(x[0] == d):
            continue
        else:
            AA[x[0]] += x[1]*A[d-1]/10

    A = AA
    s += (t-1)*A[d-1]/10
print(int(s+0.9))


#Den her metode konvergerer alt for langsomt.
#Kan løses vha. metoden i afsnittet om absorberende
#markovkæder på wikipedia.

import numpy as np
A = np.array([[0.1,-0.1,0],[-0.8,0.9,-0.1],[-0.9,0,1]])
B = np.linalg.inv(A)    
import scipy.linalg
import sympy as sp


N = 10**6
LIM = 10**3
res = 0
for nn in range(2,LIM):
    if(nn%10000 == 0):
        print(nn)
    n = N//nn
    T = create_mc(n)
    d = len(T)
    A = np.identity(d)
    AA = []
    for i in range(0,d):
        for x in T[i]:
            if(x[0] == d):
                continue
            else:
                A[i,x[0]] -=  x[1]/10
        AA.append(A[i])
    c = np.ones(d)
    x = scipy.linalg.solve(A,c)
    res += x[0]-d+1


print(int(res+0.8))
#print(542934735751917735)
#print(574929170053009792)

#Brug Gaussisk elimination i stedet for indbyggede
#solvers (de er ikke præcise nok).

def gauss_elim(A):
    n = len(A)

    #i = søjle
    for i in range(0,n):
        j = -1

        #Find en række...
        
        for k in range(0,n):
            if(A[k,i] != 0):
                j = k
                break
        if(j == -1):
            continue
        #fjern indgange over/under vha indgang (i,j)
        for k in range(0,n):
            if(A[i,k] == 0):
                continue
            if(k == j):
                continue
            A[k] = A[k]-A[k,i]*A[j]/A[j,i]
            print(A[k],A[j,i],i,j,k)
    return A

A = np.array([[1,2,3],[3,3,2],[1,5,8]])
B = gauss_elim(A)
for a in A:
    print(a)

print()
for b in B:
    print(b)

























