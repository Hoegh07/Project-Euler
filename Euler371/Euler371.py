#Opgaven løses vha. en Markovkæde

s0 = 1/1000
A = [0]*500
B = [0]*500
B[0] = 1/1000
A[1] = 998/1000
res = 0
for r in range(2,5000):
    s00 = s0/1000
    AA = [0]*500
    BB = [0]*500
    
    #New probabilities for B-states
    BB[0] += s0/1000+B[0]/1000
    for i in range(1,500):
        BB[i] += (i+1)*B[i]+A[i]+B[i-1]*(1000-2*i)
        BB[i] /= 1000

    #New probabilities for A-states
    AA[1] += 998*s0/1000+2*A[1]/1000
    for i in range(2,500):
        AA[i] += (i+1)*A[i]+(1000-2*i)*A[i-1]
        AA[i] /= 1000

    #Probability of winning
    pr = B[0]/1000
    for i in range(1,500):
        pr += (A[i])*i/1000
        pr += B[i]*(i+1)/1000
    res += r*pr
    
    s0 = s00
    A = AA
    B = BB
print(res)

























































