#Given bit strings representing polys 
# f=a_0+a_1*x+...+a_(n-1)*x^(n-1)
# g=b_0+b_1*x+...+b_(m-1)*x^(m-1)
#over GF(2), computes the product fg.
def pmul(a,b):
    c = ''
    n = len(a)
    m = len(b)
    for d in range(0,n+m-1):
        temp = 0
        for i in range(0,n):
            if(i > d):
                break
            j = d-i
            if(j > m-1):
                continue
            if(a[i] == '1' and b[j] == '1'):
                temp +=1
            temp = temp%2
        if(temp == 1):
            c = c+'1'
        else:
            c = c+'0'
    return c

N = 2**28
IRR = [[2,3]]
A = [1]*(N+1)
    
print(bin(3)[2:][::-1])

z = bin(3)[2:][::-1]
zz = bin(6)[2:][::-1]
print(pmul(z,zz))

f = bin(2)[2:][::-1]
print(f)
print(pmul(f,f))


def bin_to_nat(b):
    res = 0
    for i in range(0,len(b)):
        if(b[i] == '1'):
            res += 2**i
    return res

N = 1
for i in range(2,N):
    f = bin(i)[2:][::-1]

    for j in range(2,N):
        if(len(str(i))+len(str(j))-1 > 27):
            break
        g = bin(j)[2:][::-1]
        h = pmul(f,g)
        y = bin_to_nat(h)
        
        if(y > N):
            continue
        A[y] = 0
    

print()






















