MOD = 10**8
def P(f,r):
    if(f == 1):
        return (r*(r+1))//2

    if(f%2 == 0):
        to_even = 2*f+1
        to_odd = 2
    else:
        to_even = 1
        to_odd = 2*f
   
    room1 = (f**2)//2
    res_alt = room1
    if(r%2 == 0):
        a = to_even
        b = to_odd
        res_alt += (r//2)*a+(r//2-1)*(r//2)
        res_alt += (r//2-1)*b+(r//2-2)*(r//2-1)
    else:
        a = to_even
        b = to_odd
        res_alt += (r//2)*a+(r//2-1)*(r//2)
        res_alt += (r//2)*b+(r//2-1)*(r//2)

    return res_alt%MOD

N = 2**27*3**12
res = 0
for i in range(0,28):
    for j in range(0,13):
        f = 2**i*3**j
        r = 2**(27-i)*3**(12-j)
        res += P(f,r)

print(res%MOD)







































