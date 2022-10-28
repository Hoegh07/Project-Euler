def mex(A):
    m = 0
    for a in A:
        m = max(m,a)
    for i in range(0,m+2):
        if(i not in A):
            return i

N = 9
g = {}
def grundy(x,y):
    if((x,y) in g):
        return g[(x,y)]
    if(x+2 >= N and y+2 >= N):
        g[(x,y)] = 0
        return 0
    B = []
    for i in [2,3,5,7]:
        if(x+i < N):
            B.append(grundy(x+i,y))
        if(y+i < N):
            B.append(grundy(x,y+i))
    v = mex(B)
    g[(x,y)] = v
    return v

res = 0
m = 0
A = [0]*20
for x in range(0,N):
    for y in range(0,N):
        if(grundy(x,y) > 0):
            res += 1
        A[grundy(x,y)] += 1
        m = max(m,grundy(x,y))
print(res)
print(m)
print(A)

































