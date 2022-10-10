fib = [0,1,1]
for i in range(3,100):
    fib.append(fib[i-2]+fib[i-1])


N = 1000
res = 0

for i in range(0,2**9):
    z = bin(i)[2:][::-1]
    
    nat = 0
    irr = 0
    
    #even part
    for j in range(0,len(z)):
        n = 2*j
        if(z[j] == '1'):
            if(n == 0):
                nat += 0
                irr += 1
                continue

            nat += fib[n+2]+fib[n-1]
            irr += fib[n-1]

    #odd part
    i = 1
    while(fib[i+2] <= irr):
        i += 2

    while(irr > 0):
        irr -= fib[i]
        nat += -fib[i]+fib[i-3]
        while(fib[i] > irr and i >= 2):
            i -= 2
    
    if(irr == 0 and nat <= N):
        #print(nat)
        #print(z)
        res += nat

import time
start_time = time.time()
N = 10**10
res = 0
C = []
for i in range(0,2**26):
    z = bin(i)[2:][::-1]
    
    nat = 0
    irr = 0
    
    B = []
    #odd part
    for j in range(0,len(z)):
        if(z[j] == '0'):
            continue

        n = 2*j+1
        B.append(n)
        nat += fib[n-1]+fib[n+2]
        irr += fib[n-1]

    
    #even part
    j = 0
    A = []
    while(fib[j+2] <= irr):
        j += 2

    while(irr > 0 and j>=2):
        if(j == 0):
            irr -= 1
            break
        
        A.append(j-2)
        nat += fib[j-3]-fib[j]
        irr -= fib[j]
        j -= 2

        while(fib[j] > irr and j >= 2):
            j -= 2
    t = True
    for b in B:
        if(b+1 in A or b-1 in A):
            t = False
            break
    if(t == False):
        continue
    for a in A:
        if(a+1 in B or (a >0 and a-1 in B)):
            t = False
            break
    if(t == False):
        continue

    if(irr == 0 and nat <= N):
        #print(nat)
        #print(z)
        res += nat
        C.append(nat)


print()
print(sum(list(set(C)))+1)
print()
print("--- %s seconds ---" % (time.time() - start_time))






































