def sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False


def ispal(n):
    return str(n)==str(n)[::-1]


N = 10**8*3
pri = sieve(N)
primes = [p for p in pri]
is_prime = [0]*(N+1)
for p in primes:
    is_prime[p] = 1


def is_prime_square(n):
    y = n**0.5
    if(y != int(y)):
        return 0
    return is_prime[int(y)]

goodprimes = []
for p in primes:
    if(ispal(p)):
        continue
    q = int(str(p)[::-1])
    if(q > N):
        continue
    if(is_prime[q]):
        goodprimes.append(p)

for i in range(0,10):
    print(goodprimes[i])
print("START")
good = []
for p in goodprimes:
    x = p**2
    q = int(str(p)[::-1])
    y = q**2

    if(ispal(x)):
        continue

    if(int(str(x)[::-1]) == y):
        good.append(x)

good = sorted(good)
for x in good:
    print(x)

res = 0
for i in range(0,50):
    res += good[i]
print()
print(res)
print(len(good))










































