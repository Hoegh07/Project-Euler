#Update Fenwick tree with
def update(F,i,v):
    while(i < len(F)):
        F[i] += v
        i += (i&(-i))

#Get prefix-sum using Fenwick tree
def prefix_sum(F,i):
    res = 0
    while(i > 0):
        res += F[i]
        i -= (i&(-i))
    return res

#Get sum of some interval range
def range_sum(F,a,b):
    return prefix_sum(F,b)-prefix_sum(F,a-1)

def suffix_sum(F,i):
    return prefix_sum(F,len(F)-1)-prefix_sum(F,i-1)

S = 10000019
N = 10**6
MOD = 1000000007
FT = [0]*(S+1)
k = 153
D = [0]
for i in range(1,N+1):
    update(FT,k,1)
    D.append(k)
    k = (k*153)%S

A = [[0]*(N+1) for i in range(0,4)]
AA = [[0]*(N+1) for i in range(0,4)]
for i in range(1,N+1):
    A[0][i] = 1
    AA[0][i] = D[i]

for i in range(1,4):
    FT = [0]*(S+1)
    FFT = [0]*(S+1)
    update(FFT,D[1],AA[i-1][1])
    update(FT,D[1],A[i-1][1])
    for j in range(2,N+1):
        A[i][j] = prefix_sum(FT,D[j])
        AA[i][j] = (prefix_sum(FFT,D[j])+A[i][j]*D[j])%MOD
        update(FFT,D[j],AA[i-1][j])
        update(FT,D[j],A[i-1][j])

res = 0
for i in range(1,N+1):
    res += AA[3][i]
print(res%MOD)

if(False):
    C = [0]*(N+1)
    res = 0
    for a in range(1,N+1):
        for b in range(a+1,N+1):
            for c in range(b+1,N+1):
                for d in range(c+1,N+1):
                    if(D[a] < D[b] and D[b] < D[c] and D[c] < D[d]):
                        C[d] +=1 
                        res += D[a]+D[b]+D[c]+D[d]
    print(res)







































