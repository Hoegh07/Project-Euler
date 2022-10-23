
def mex(A):
    for i in range(0,len(A)+10):
        if(i not in A):
            return i


N = 10**6
g = [0,0,1]
for n in range(3,150):
    A = []
    for i in range(0,n-1):
        A.append(g[i]^g[(n-2-i)])
    g.append(mex(A))

res = 0
for i in range(1,68):
    if(g[i] > 0):
        res += 1
print(res)

h = 0
for i in range(68,102):
    if(g[i] > 0):
        h += 1

no_periods = (N-68)//34
remainder = (N-68)%34

print(no_periods)
print(remainder)
res += h*no_periods
for i in range(68,68+remainder+1):
    if(g[i] > 0):
        res += 1
print(res)




#a = []
#for i in range(68,102):
#    a.append(g[i])
#
#b = []
#for i in range(102,136):
#    b.append(g[i])
#
#for i in range(0,34):
#    print(a[i] == b[i])






























