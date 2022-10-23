def partitions(n, I=1):
    yield (n,)
    for i in range(I, n//2 + 1):
        for p in partitions(n-i, i):
            yield (i,) + p

def subsetsum(a):
    d = len(a)
    for i in range(0,2**d):
        z = bin(i)[2:].zfill(d)
        t = 0
        for j in range(0,len(a)):
            if(z[j] == '1'):
                t += a[j]
        if(t == sum(a)//2):
            return True
    return False

def f(k):
    for n in range(2,300,2):
        pi = partitions(n)
        b = True
        for p in pi:
            p = list(p)
            cont = False
            for x in p:
                if(x > k):
                    cont = True
                    break
            if(cont):
                continue

            #k-bounded partition
            if(not subsetsum(p)):
                print(p)
                b = False
                break
        if(b):
            return n
    return 1

print(f(4))



















