fib = [0, 1]


while len(fib) < 12:
    fib_len = len(fib)
    next_fib = fib[fib_len-1] + fib[fib_len-2]
    fib.append(next_fib)

print(fib)