# This solution uses recursion. See fibonacci2 for a non-recursive approach

def fibonacci_of(n):
    if n in {0, 1}: # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2) # Recursive case


print(fibonacci_of(10))
# Output: 55
print([fibonacci_of(n) for n in range(15)])
# Output: List with 15 elements