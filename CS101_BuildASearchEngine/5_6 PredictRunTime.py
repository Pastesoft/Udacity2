import time

def time_exec(code):
    start = time.clock()
    result = eval(code)
    stop = time.clock()
    run_time= stop - start
    return result, run_time

def spin_loop(n):
    i = 0
    while i < n:
        i += 1

print time_exec("spin_loop(10**5)")[1]
print time_exec("spin_loop(10**6)")[1]
print time_exec("spin_loop(10**9)")[1]
