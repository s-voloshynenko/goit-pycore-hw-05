def caching_fibonacci() -> callable:
    """
    Returns a Fibonacci function with caching.
    """
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return n
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    return fibonacci

fib = caching_fibonacci()

print(fib(10)) # 55
print(fib(15)) # 610
