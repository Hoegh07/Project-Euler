def f(n):
    res = 0
    for x in range(1,n**2-n+1):
        for y in range(1,n**2-n+1):
            if(pow(x,y,n) == pow(y,x,n)):
                print(x,y,pow(x,y,n))
                res += 1
    print()
    return res

#print(f(2))
#print(f(3))
print(f(5))
#print(f(7))
#print(f(11))




































