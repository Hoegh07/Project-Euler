S = [290797]
mod = 50515093
n = 2*10**6
for i in range(1,2*n+20):
    S.append((S[i-1]**2)%mod)

P = []
for i in range(0,n):
    P.append([S[2*i],S[2*i+1]])

def dist(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**(0.5)

def bruteforce(Q):
    res = 10**10
    for i in range(len(Q)):
        for j in range(i+1,len(Q)):
            res = min(res,dist(Q[i],Q[j]))
    return res

#print(bruteforce(P))
#print(9262015.547769556)

def mindist(Q):
    if(len(Q) <= 3):
        return bruteforce(Q)

    m = len(Q)//2
    xm = Q[m][0]

    L = Q[0:m]
    R = Q[m:]

    ld = mindist(L)
    rd = mindist(R)
    d = min(ld,rd) 

    strip = []
    for i in range(0,len(Q)):
        if(abs(Q[i][0]-xm) <= d):
            strip.append(Q[i])
    strip = [a[::-1] for a in strip]
    strip = sorted(strip)
    
    for i in range(0,len(strip)):
        P = strip[i]
        for j in range(1,8):
            if(i+j >= len(strip)):
                break
            PP = strip[i+j]
            t = dist(P,PP)
            d = min(d,t)

    return d

P = sorted(P)
print(mindist(P))































