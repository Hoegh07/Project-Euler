def sd(n):
    x = str(n)
    res = 0
    for i in range(0,len(x)):
        res += int(x[i])
    return res

for i in range(0,100):
    print(sd(i),sd(137*i))










































