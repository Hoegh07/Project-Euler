pascal = [[1],[1,1]]
for i in range(2,30):
    A = [1]
    p = pascal[i-1]
    for j in range(0,len(p)-1):
        A.append((p[j]+p[j+1])%7)
    A.append(1)
    pascal.append(A)

for a in pascal:
    print(a)




























