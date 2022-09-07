def M(n):
    print(n)
    if(n > 100):
        return n-10
    else:
        return M(M(n+11))

print(M(91))
