from scipy.integrate import quad
import math 

#Noget galt med x og y...
def x(t,v):
    return (1-t)**3+3*(1-t)**2*t+3*(1-t)*t**2*v

def y(t,v):
    return 3*(1-t)**2*t*v+3*(1-t)*t**2+t**3

def dxdt(t,v):
    return t*t*(6 - 9*v) + t*(-6 + 6*v)

def dydt(t,v):
    return -3*(1-t)*(t*(3*v-2)-v) 


def integrand(t,v):
    return math.sqrt(dxdt(t,v)**2+dydt(t,v)**2)

v = 0.25
I = quad(integrand,0,1,args=(v))

def integrand_area(t,v):
    return y(t,v)*dxdt(t,v)

vlow = 0
vhigh = 10
while(vhigh-vlow > 0.000000000001):
    vmid = (vhigh+vlow)/2
    temp = quad(integrand_area,0,1,args=(vmid))[0]
    if(temp < math.pi/4):
        vlow,vhigh = vmid,vhigh
    else:
        vlow,vhigh = vlow,vmid

#Find kurvelængde for vlow
print("SVAR")
print(vlow)
print((2+((22+5*math.pi)/3)**0.5))
from math import pi as pi

L = quad(integrand,0,1,args=(vlow))[0]
print()
print("ABE")
print(L)
print(pi/2)

print(100*(L-pi/2)/(pi/2))

print()
print(x(0,vlow),y(0,vlow))
print(x(1,vlow),y(1,vlow))












































