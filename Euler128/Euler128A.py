def sieve(limit):
    a = [True] * limit      
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

# Python3 program Miller-Rabin primality test
import random
 
# Utility function to do
# modular exponentiation.
# It returns (x^y) % p
def power(x, y, p):
    return pow(x,y,p) 

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


#nbh of a corner
def nbh(n,l,s):
    if(s == 0):
        return [n+1,n+6*l-1,n+6*l,n+6*l+1,n-6*(l-1),n+6*l+6*(l+1)-1]
    else:
        return [n-1,n+1,n-6*(l-1)-s,n+6*l+s-1,n+6*l+s,n+6*l+s+1]

#Returns nbh of second last element in layer l
def nbhsl(n,l):
    if(n == 7):
        return [2,1,6,17,18,19]
    return [n-1,n-6*l+1,n-6*l+1-6*(l-1),n-6*l,n+6*l+5,n+6*l+5+1]


def PD(n,N):
    t = 0
    for x in N:
        y = abs(n-x)
        if(isPrime(y,25)):
            t += 1
    return t


def solution(goal):
    count = 1
    n = 2
    l = 1
    while(count < goal):
        N = nbh(n,l,0)
        if(PD(n,N) == 3):
            count += 1
            if(count == goal):
                return n

        for s in range(1,6):
            n += l
            N = nbh(n,l,s)
            if(PD(n,N) == 3):
                count += 1
                if(count == goal):
                    return n

        n += l-1
        N = nbhsl(n,l)
        if(PD(n,N) == 3):
            count += 1
            if(count == goal):
                return n
        n += 1
        l += 1

print(solution(2000))
    
def better_solution(goal):
    count = 1
    n = 2
    l = 1
    while(count < goal):
        N = nbh(n,l,0)
        if(PD(n,N) == 3):
            count += 1
            if(count == goal):
                return n

        #for s in range(1,6):
        #    n += l
        #    N = nbh(n,l,s)
        #    if(PD(n,N) == 3):
        #        count += 1
        #        if(count == goal):
        #            return n
        n += 6*l
        n -= 1
        N = nbhsl(n,l)
        if(PD(n,N) == 3):
            count += 1
            if(count == goal):
                return n
        n += 1
        l += 1

print(better_solution(2000))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

















