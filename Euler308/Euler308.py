fractions = [[17,91],[78,85],[19,51],[23,38],[29,33],[77,29],[95,23],[77,19],[1,17],[11,13],[13,11],[15,2],[1,7],[55,1]]


s = 2
k = 0
p = [2,3,5,7,11,13,17,19]
for i in range(1,10000):
    for f in fractions:
        n = f[0]
        d = f[1]
        if((s*n)%d == 0):
            s = (s*n)//d
            #print(s)
            if(s == 2**p[k]):
                print(i)
                k += 1
            break


#number of steps from state 5^n*7^d*13 
#to the state 5^n*7^(d-1)*13 or 5^(n+1)*7^n*13
def steps(n,d):
    r = n%d
    q = (n-r)//d
    
    res = (q)*2*(2*d+1)
    res += 2*r+1
    if(r == 0):
        return res+1+n+(d-1)+1+2*n+1
    return res+1+2*n+1+2*(r-1)+1

print()
print(steps(2,1))
print()
k = 5
s = 0 
for n in range(2,10000000):
    for d in range(n-1,0,-1):
        k += steps(n,d)
        if(d == 1):
            s += 1
            if(s == 10001 ):
                print(k-2*n-1-n-1)
                print("ABE")
        if(n%d == 0):
            break









































