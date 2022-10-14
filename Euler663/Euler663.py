#Implementation af segment tree

#NAIV
class SlowRangeQuery:
    def __init__(self,n):
        self.A = [0]*(n+1)

    def update(self,i,val):
        self.A[i] += val

    def query(self,i,j):
        res = 0
        for k in range(i,j+1):
            res += self.A[k]
        return res

class SegmentTree:
    def __init__(self,n):
        self.lo = [0]*(4*n+1)
        self.hi = [0]*(4*n+1)
        self.sum = [0]*(4*n+1)
        self.ps = [0]*(4*n+1)
        self.ss = [0]*(4*n+1)
        self.bs = [0]*(4*n+1)

        self.make(1,0,n)
    
    def make(self,i,a,b):
        self.lo[i] = a
        self.hi[i] = b

        if(a == b):
            return
        
        #Midpoint
        m = (a+b)//2

        #left child
        self.make(2*i,a,m)
        
        #right child
        self.make(2*i+1,m+1,b)

    def build(self,A):
        for j in range(len(self.lo)-1,0,-1):
            a = self.lo[j]
            b = self.hi[j]

            if(a == b):
                self.sum[j] = A[a]
                self.ps[j] = max(A[a],0)
                self.ss[j] = max(A[a],0)
                self.bs[j] = max(A[a],0)
                continue

            ls,lps,lss,lbs = self.sum[2*j],self.ps[2*j],self.ss[2*j],self.bs[2*j]
            rs,rps,rss,rbs = self.sum[2*j+1],self.ps[2*j+1],self.ss[2*j+1],self.bs[2*j+1]
            
            s = ls+rs
            ps = max(lps,max(ls+rps,0))
            ss = max(rss,max(lss+rs,0))
            bs = max(lbs,max(rbs,max(lss+rps,0)))

            self.sum[j] = s
            self.ps[j] = ps
            self.ss[j] = ss
            self.bs[j] = bs
            
    
   
    def update(self,i,val):
        self.bubble(i,val,1)
    
    def bubble(self,i,val,j):
        a = self.lo[j]
        b = self.hi[j]
        #print(i,a,b,val)
        
        if(a == b):
            self.sum[j] = val
            self.ps[j] = max(0,val)
            self.ss[j] = max(0,val)
            self.bs[j] = max(0,val)
            return

        m = (a+b)//2
        if(i <= m):
            self.bubble(i,val,2*j)
        else:
            self.bubble(i,val,2*j+1)
        
        ls,lps,lss,lbs = self.sum[2*j],self.ps[2*j],self.ss[2*j],self.bs[2*j]
        rs,rps,rss,rbs = self.sum[2*j+1],self.ps[2*j+1],self.ss[2*j+1],self.bs[2*j+1]
        
        s = ls+rs
        ps = max(lps,max(ls+rps,0))
        ss = max(rss,max(lss+rs,0))
        bs = max(lbs,max(rbs,max(lss+rps,0)))

        self.sum[j] = s
        self.ps[j] = ps
        self.ss[j] = ss
        self.bs[j] = bs


n = 107
l = 1000
t0,t1,t2 = 0,0,1
T = [t0,t1,t2]
for j in range(3,2*l+1):
    T.append((T[j-3]+T[j-2]+T[j-1])%n)
A = [0]*(n+1)

res = 0
ST = SegmentTree(n)
for i in range(1,l+1):
    A[T[2*i-2]] = A[T[2*i-2]]+2*T[2*i-1]-n+1
    ST.update(T[2*i-2],A[T[2*i-2]])
    res += ST.bs[1]
print(res)
print(1618572)

print()

n = 10**7+3
l = 10**7
r = 2*10**5

#Lav array med tribonaccital og A
t0,t1,t2 = 0,0,1
T = [t0,t1,t2]
for j in range(3,4*l+1):
    T.append((T[j-3]+T[j-2]+T[j-1])%n)
A = [0]*(n+1)

ST = SegmentTree(n)

for i in range(1,l+1):
    if(i%100000 == 1):
        print(i)
    A[T[2*i-2]] = A[T[2*i-2]]+2*T[2*i-1]-n+1
    ST.update(T[2*i-2],A[T[2*i-2]])

res = 0
#Kør de sidste r opdateringer
#og læg bedste sum til resultat
for i in range(l+1,l+r+1):
    A[T[2*i-2]] = A[T[2*i-2]]+2*T[2*i-1]-n+1
    ST.update(T[2*i-2],A[T[2*i-2]])
    res += ST.bs[1]

print(res)
print(1884138010064752)

print()
print("Bedre løsning")
ST = SegmentTree(n)
res = 0
for i in range(1,l+1):
    A[T[2*i-2]] = A[T[2*i-2]]+2*T[2*i-1]-n+1
ST.build(A)

for i in range(l+1,l+r+1):
    A[T[2*i-2]] = A[T[2*i-2]]+2*T[2*i-1]-n+1
    ST.update(T[2*i-2],A[T[2*i-2]])
    res += ST.bs[1]

print(res)











