# def isOdd(num):
#     if num % 2 == 0:
#         return False
#     else:
#         return True
#
#
# def isEven(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False

def is_odd(number):
    return number % 2 == 1

def is_even(number):
    return number % 2 == 0

# print(isOdd(3))
# print(isOdd(4))
# print(isEven(3))
# print(isEven(4))

assert is_odd(42) == False
assert is_odd(9999) == True
assert is_odd(-10) == False
assert is_odd(-11) == True
assert is_odd(3.1415) == False
assert is_even(42) == True
assert is_even(9999) == False
assert is_even(-10) == True
assert is_even(-11) == False
assert is_even(3.1415) == False

# assert isOdd(42) == False
# assert isOdd(9999) == True
# assert isOdd(-10) == False
# assert isOdd(-11) == True
# assert isOdd(3.1415) == False
# assert isEven(42) == True
# assert isEven(9999) == False
# assert isEven(-10) == True
# assert isEven(-11) == False
# assert isEven(3.1415) == False