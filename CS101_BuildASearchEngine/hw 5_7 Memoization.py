#[Double Gold Star] Memoization is a way to make code run faster by saving
#previously computed results.  Instead of needing to recompute the value of an
#expression, a memoized computation first looks for the value in a cache of pre-
#computed values.

#Define a procedure, cached_execution(cache, code), that takes in two inputs: a
#cache, which is a Dictionary that maps strings representing Python expressions
#to their previously computed values, and code, a string that is a Python
#expression.  Your procedure should return the value of code, but should only
#evaluate code if it has not been previously evaluated.

def cached_execution(cache,code):
    if code in cache:
        print "cached"
        return cache[code]
    else:
        print "eval"
        res = eval(code)
        cache[code] = res
        return res


#Here is an example showing the desired behavior of cached_execution:

def factorial(n):
    print "Running factorial"
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result

cache = {} # start cache as an empty dictionary
### first execution (should print out Running factorial and the result)
print cached_execution(cache, 'factorial(50)')                           

print "Second time:"
### second execution (should only print out the result)
print cached_execution(cache, 'factorial(50)')
