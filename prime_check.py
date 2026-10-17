import math

# Check whether the literal below is prime.
n = 97

# A composite n = a * b with 1 < a <= b has a <= isqrt(n), so scanning the
# divisors up to and including isqrt(n) misses no factor; the + 1 makes that
# bound inclusive, which is what catches a prime square such as 49.
prime = n > 1
for d in range(2, math.isqrt(n) + 1):
    if n % d == 0:
        prime = False
        break

# Report the number judged and the verdict on one line.
print(f"{n} is prime" if prime else f"{n} is not prime")
