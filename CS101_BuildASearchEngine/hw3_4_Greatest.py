def greatest(p):
    i = res = 0
    while i < len(p):
        a = p[i]
        i = i+1
        if(a > res):
            res = a
    return res

print greatest([4,23,1])
print greatest([])
