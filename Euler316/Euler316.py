A = [1,0,0,0]

res = 0
for r in range(1,100000):
    AA = [0,0,0,0]

    AA[0] = 9*A[0]/10+8*A[1]/10+9*A[2]/10 
    AA[1] = A[0]/10+A[1]/10
    AA[2] =         A[1]/10
    
    A = AA

    res += (r-1)*A[2]/10

print(int(res+0.5))
print(res)

def create_markovchain(n):
    x = str(n)
    prefix = ['']
    for i in range(1,len(x)+1):
        prefix.append(prefix[i-1]+x[i-1])
    
    states = [0]*(len(x)+1)
    transitions = {}
    



    return 0
































