A = [0]*(2**10+1)
for i in range(1,10):
    A[2**i] = 1

C = [0]*(2**10+1)
for t in range(1,19):
    B = [0]*(2**10+1)
    for n in range(0,2**10):       
        if(A[n] == 0):
            continue
        
        C[n] += A[n]
        
        #Tilføj ciffer 0,1,2,...,9
        for d in range(0,10):
            X = []
            z = str(bin(n)[2:]).zfill(10)[::-1]
            for i in range(0,10):
                if(z[i] == '1'):
                    X.append(i)
            
            if(d in X):
                B[n] += A[n]
            else:
                B[n+2**d] += A[n]
    A = B

def T(n):
    return (n*(n+1))//2

#C[2**3+2**4] indeholder præcist det antal
#tal som kun består af 3'ere og 4'ere og
#tilsvarende for andre indices.
#Burde nu kunne løse problem vha. inklusion-
#eksklusion.
CC = [0]*(2**10+1)
for n in range(1,2**10+1):
    if(C[n] == 0):
        continue
    z = str(bin(n)[2:]).zfill(10)[::-1]
    X = []
    for i in range(0,10):
        if(z[i] == '1'):
            X.append(i)
    
    Y = [[]]
    for x in X:
        Z = []
        for y in Y:
            if(x in y):
                Z.append(y)
                continue
            Z.append(y)
            Z.append(y+[x])
        Y = Z
    
    Y = sorted(Y)
    i = 1
    YY = [Y[0]]
    while(i < len(Y)):
        if(Y[i] != YY[i-1]):
            YY.append(Y[i])
        i += 1

    for s in Y:
        if(s == []):
            continue
        m = 0
        for t in s:
            m += 2**t
        CC[m] += C[n]

res = 0
for n in range(1,2**10+1):
    if(CC[n] == 0):
        continue
    z = str(bin(n)[2:]).zfill(10)[::-1]
    c = 1
    for i in range(0,10):
        if(z[i] == '1'):
            c += 1
    if(CC[n] == 0):
        continue
    res += (-1)**c*T(CC[n]-1)

MOD = 1000267129
#print()
print("RESULTAT:")
print(res%MOD)







#print()
#print("TEST")
#print(A[2**3+2**4])

#def friends(n,m):
#    x = str(n)
#    y = str(m)
#    X = [x[i] for i in range(len(x))]
#    Y = [y[i] for i in range(len(y))]
#
#    for l in X:
#        if(l in Y):
#            return True
#    return False
#
#N = 1000
#res = 0
#for i in range(1,N):
#    for j in range(i+1,N):
#        if(friends(i,j)):
#            res += 1
#print("BRUTEFORCE")
#print(res)

#print()
#print()
#print()
#print()
#print("TEST")
#contains23 = 0
#for i in range(1,N):
#    x = str(i)
#    T = []
#    for j in range(0,len(x)):
#        if(x[j] == '2'):
#            T.append(2)
#        if(x[j] == '3'):
#            T.append(3)
#    T = sorted(list(set(T)))
#    if(T == [2,3]):
#        contains23 += 1
#
#print(contains23)
#res = 0
#for i in range(1,2**10):
#    if(A[i] == 0):
#        continue
#    z = str(bin(i)[2:]).zfill(10)[::-1]
#    if(z[2**2] == '1' and z[2**3]== '1'):
#        res += C[i]
#        #print(z)
#print(res)
#print(CC[2**2+2**3])
