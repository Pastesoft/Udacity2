def proc1(p):
    p[0] = p[1]

def proc2(p):
    p = p + [1]

def proc3(p):
    a = p
    p.append(3)
    a.pop()

def proc4(p):
    a = []
    while p:
        a.append(p.pop())
    while a:
        p.append(a.pop())
    
pa = [0, 1, 2]
proc1(pa)
print pa
pa = [0, 1, 2]
proc2(pa)
print pa
pa = [0, 1, 2]
proc3(pa)
print pa
pa = [0, 1, 2]
proc4(pa)
print pa
