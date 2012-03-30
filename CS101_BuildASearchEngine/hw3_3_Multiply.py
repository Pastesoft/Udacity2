def product_list(p):
    res = 1
    while p:
        res = res * p.pop()
    return res
	
print product_list([1,2,3,4])
print product_list([9])
print product_list([0])
