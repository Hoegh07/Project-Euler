n = 5000000
cur = 0
m = 1
while cur < n:
    cur += 2**m//m
    m += 1

mm = 2**m
arr = [True]*mm
arr[0] = arr[1] = False

for i in range(2, mm):
    if arr[i]:
        pi = i.bit_length()-1
        for pj in range(pi, m-pi):
            cur = i<<pj
            for t in range(2**pj):
                arr[cur] = False
                cur ^= i*(((t^(t+1))+1)>>1)

irrp = [i for i,j in enumerate(arr) if j]
print(irrp[n-1])
































