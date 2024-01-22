"""
We are interested in the sequence of integers defindes by
U1 = 1, U2 = 1, and, for any natural number n, by Un + 2 = Un + 1 + Un.
It is called the Fibonacci sequence.
Write the fibonacci function that takes an integer n > 0 and
returns the element of index n of this sequence.
We will use dynamic programming (no recursion)
"""

def fibonacci(n):
    # first three nums of fibo seq
    u = [0, 1, 1]
    i = 2
    while len(u) <= n:
        i = i + 1
        u.append(u[i - 2] + u[i - 1])
    return u[n]


print(fibonacci(10))
print([fibonacci(n) for n in range(15)])
