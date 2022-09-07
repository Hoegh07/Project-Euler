import math
from scipy.integrate import quad as quad
import numpy


def xy(t,v):
    P0 = numpy.array([1,0])
    P1 = numpy.array([1,v])
    P2 = numpy.array([v,1])
    P3 = numpy.array([0,1])

    B = (1-t)**3*P0+3*(1-t)**2*t*P1
    B += 3*(1-t)*t**2*P2
    B += t**3*P3
    return max(B[0],0),max(B[1],0)

def dxy(t,v):
    P0 = numpy.array([1,0])
    P1 = numpy.array([1,v])
    P2 = numpy.array([v,1])
    P3 = numpy.array([0,1])

    B = 3*(1-t)**2*(P1-P0)
    B += 6*(1-t)*t*(P2-P1)+3*t**2*(P3-P2)
    return B[0],B[1]


#Areal af området begrænset af Bezierkurven
#og linjestykkerne O-P0 og O-P3.

def integrand(t,v):
    _,y = xy(t,v)
    dxdt,_ = dxy(t,v)
    return dxdt*y

def area(v):
    return quad(integrand,0,1,args=(v))

def integrand_L(t,v):
    dxdt,dydt = dxy(t,v)
    return math.sqrt(dxdt**2+dydt**2)

def arclength(v):
    return quad(integrand_L,0,1,args=(v))

A = math.pi/4
L = math.pi/2

vlow = 0
vhigh = 10

print(area(vlow))
print(area(vhigh))
print("ABE")

while(vhigh-vlow > 0.000001):
    vmid = (vhigh+vlow)/2
    a = area(vmid)[0]
    if(a < A):
        vlow = vmid
    else:
        vhigh = vmid


print(area(vlow))
print(A)
print()
print(vlow)











































