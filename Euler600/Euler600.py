N = 12
res = 0
for i in range(1,12):
    for j in range(i,12):
        for k in range(j,12):
            for a in range(k,12):
                for b in range(a,12):
                    for c in range(b,12):
                        if(c > i+j+k+a+b):
                            res += 1
print(res)


