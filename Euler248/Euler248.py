from math import factorial as fac
# Python3 program Miller-Rabin primality test
import random
 
# Utility function to do
# modular exponentiation.
# It returns (x^y) % p
def power(x, y, p):
     
    # Initialize result
    res = 1;
     
    # Update x if it is more than or
    # equal to p
    x = x % p;
    while (y > 0):
         
        # If y is odd, multiply
        # x with result
        if (y & 1):
            res = (res * x) % p;
 
        # y must be even now
        y = y>>1; # y = y/2
        x = (x * x) % p;
     
    return res;
 
# This function is called
# for all k trials. It returns
# false if n is composite and
# returns false if n is
# probably prime. d is an odd
# number such that d*2<sup>r</sup> = n-1
# for some r >= 1
def miillerTest(d, n):
     
    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + random.randint(1, n - 4);
 
    # Compute a^d % n
    x = power(a, d, n);
 
    if (x == 1 or x == n - 1):
        return True;
 
    # Keep squaring x while one
    # of the following doesn't
    # happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while (d != n - 1):
        x = (x * x) % n;
        d *= 2;
 
        if (x == 1):
            return False;
        if (x == n - 1):
            return True;
 
    # Return composite
    return False;
 
# It returns false if n is
# composite and returns true if n
# is probably prime. k is an
# input parameter that determines
# accuracy level. Higher value of
# k indicates more accuracy.
def isPrime( n, k):
     
    # Corner cases
    if (n <= 1 or n == 4):
        return False;
    if (n <= 3):
        return True;
 
    # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    d = n - 1;
    while (d % 2 == 0):
        d //= 2;
 
    # Iterate given number of 'k' times
    for i in range(k):
        if (miillerTest(d, n) == False):
            return False;
 
    return True;
 
# Driver Code
# Number of iterations
k = 16
 
P = []
for i in range(0,12):
    for j in range(0,7):
        for k in range(0,4):
            for a in range(0,3):
                for b in range(0,3):
                    for c in range(0,3):
                        n = 2**i*3**j*5**k*7**a*11**b*13**c+1
                        if(isPrime(n,k)):
                            v2 = 0
                            v3 = 0
                            v5 = 0
                            v7 = 0
                            v11 = 0
                            v13 = 0
                            if(i > 1):
                                v2 = i-2
                            if(j > 1):
                                v3 = j-2
                            if(k > 1):
                                v5 = k-2
                            if(a > 1):
                                v7 = a-2
                            if(b > 1):
                                v11 = b-2
                            if(c > 1):
                                v13 = c-2
                            
                            if(j >= 1):
                                v2 += 1
                            if(k >= 1):
                                v2 += 2
                            if(a >= 1):
                                v2 += 1
                                v3 += 1
                            if(b >= 1):
                                v2 += 1
                                v5 += 1
                            if(c >= 1):
                                v2 += 2
                                v3 += 1

                            if(v2 <= 10 and v3 <= 5 and v5 <= 2 and v7 <= 1 and v11 <= 1 and v13 <= 1 and n != 1):
                                P.append([n,v2,v3,v5,v7,v11,v13])

def prod(a,b):
    return [a[0]*b[0],a[1]+b[1],a[2]+b[2],a[3]+b[3],a[4]+b[4],a[5]+b[5],a[6]+b[6]]

def good(a):
    if(a[1] == 10 and a[2] == 5 and a[3] == 2 and a[4] == 1 and a[5] == 1 and a[6] == 1):
        return True

B = []
A = [[1,0,0,0,0,0,0]]
for t in range(0,0):
    AA = []
    for a in A:
        if(good(a)):
            B.append(a[0])
            continue
        for b in P:
            if(a[1]+b[1] > 10 or a[2]+b[2] > 5 or a[3]+b[3] > 2 or a[4]+b[4] > 1 or a[5]+b[5] > 1 or a[6]+b[6] > 1):
                continue
            AA.append(prod(a,b))
    A = AA

#C = []
#for a in A:
#    if(good(a)):
#        C.append(a[0])
#C = sorted(C)
#print(C[0])
#print(6227180929)
#print()
#print(len(C))

#print()
#PP = [a[0] for a in P]
#print(66529 in PP)
#print(93601 in PP)





#VI KAN OGSÅ HAVE PRODUKTER AF PRIMTAL FRA P!!!!!!!!!!!

from math import gcd as gcd

PP = [a[0] for a in P]
PP = sorted(PP)
print(PP[0])

P = sorted(P)
Q = []
for p in P:
    if(p[0] != 1):
        Q.append(p)

print(Q[0])
print(Q[1])





















