import math

# Report both real square roots of the given prime number: the same 97 the
# primality check judges, held as a literal because this tool takes no input.

n = 97

# Both roots are reported because 97 is prime, so neither root is an
# integer and both are irrational.

# math.sqrt returns the positive (principal) root, and its negation is the
# other root.
root = math.sqrt(n)

# The number judged and both of its square roots, on one line.
print(f"The square roots of {n} are {root} and {-root}")
