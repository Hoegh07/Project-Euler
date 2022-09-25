from math import factorial as fac

def f(n):
    if(n <= 2):
        return 0
    
    res = fac(n-1)*(n-1)
    
    #Træk dem fra hvor der er er lukket på en 
    #underdiagonal.
    for i in range(2,n+1):
        res -= fac(n-i)

    #Træk dem fra hvor der er lukket på en
    #overdiagonal.
    for i in range(3,n+1):
        #res -= f(i-1)
        res -= fac(i-1)
        print(i-1,f(i-1))

    return res
print(fac(0))
print(f(5))

#print(f(5))
n = 3
res = fac(n-1)*(n-1)








































