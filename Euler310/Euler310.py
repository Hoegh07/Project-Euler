def mex(A):
    m = 0
    for a in A:
        #print(m,a)
        m=max(m,a)
    for i in range(0,m+100):
        if(i not in A):
            return i


g = {}
g[0] = 0
def grundy(v):
    if(v in g):
        return g[v]
    
    B = []
    for i in range(1,int(v**0.5)+1):
        B.append(grundy(v-i*i))
    
    r = mex(B)
    g[v] = r
    return r


n = 29
freq = [0]*100
for i in range(0,n+1):
    freq[grundy(i)] += 1

res = 0
for i in range(0,100):
    for j in range(0,100):
        for k in range(0,100):
            if(i^j^k == 0):
                ni = freq[i]
                nj = freq[j]
                nk = freq[k]
                if(i == j and j == k):
                    res += ((ni*(ni+1)*(ni+2)))//6
                if(i == j and i < k):
                    res += ((ni*(ni+1))//2)*nk
                if(i < j and j < k):
                    res += ni*nj*nk

print(res)

#Første O(n²) metode
#n = 10**5
#A = [0]*(n+1)
#for i in range(1,n+1):
#    A[i] = grundy(i)
#
#print("FØRSTE DOBBELT LOOP")
#freq = [0]*1000
#for b in range(0,n+1):
#    x = A[b]
#    for c in range(b,n+1):
#        y = A[c]
#        freq[x^y] += 1
#
#
#print("VI STARTER")
#res = 0
#for a in range(0,n+1):
#    v = A[a]
#    res += freq[v]
#    
#    #Remove all frequencies where b = a
#    b = a
#    x = A[b]
#    for c in range(b,n+1):
#        y = A[c]
#        freq[x^y] -= 1
#
#print()
#print("RESULTAT")
#print(res)


















































