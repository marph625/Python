"""
Make the function dichotomy(tab, x) to satisfy the result
desired by the output.
def dichotomy(tab, x):
<<< tab : array of integers sorted in ascending order x : integer >>>

Outputs:
dichotomy([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28)
True
dichotomy([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 27)
False
"""


def dichotomy(listOfIntegers, x):
    # lists start with index 0
    start = 0
    # thus the last element of any list is the length of list - 1
    end = len(listOfIntegers) - 1
    # as long as start is lower OR equal to end
    while start <= end:
        # calculates the median of start and end
        m = (start + end) // 2

        if x == listOfIntegers[m]:
            return True
        if x > listOfIntegers[m]:
            start = m + 1
        else:
            end = m - 1
    return False


first = dichotomy([15, 16, 18, 19, 23, 24, 28, 29, 31, 33], 28)
second = dichotomy([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37], 4)
print(first, second)
print(second, first)
