import math

def area_circle(r):
    return math.pi*r**2

#Giver krumningen af den mindste cirkel som tangerer cirkler,
#med krumning henholdsvis k1,k2 og k3, i seks punkter.
def k4(k1,k2,k3):
    return k1+k2+k3+2*math.sqrt(k1*k2+k2*k3+k3*k1)

A = area_circle(1)
r = 2*math.sqrt(3)-3
area = 3*area_circle(r)
P = [[1/r,1/r,1/r],[-1,1/r,1/r],[1/r,-1,1/r],[1/r,1/r,-1]]
for i in range(10):
    Q = []
    for p in P:
        k = k4(p[0],p[1],p[2])
        area += area_circle(1/k)
        Q.append([p[0],p[1],k])
        Q.append([p[0],k,p[2]])
        Q.append([k,p[1],p[2]])
    P = Q
print((A-area)/A)








