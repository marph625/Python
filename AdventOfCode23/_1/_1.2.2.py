import _1_submission


def calculation_2():
    total_sum = 0
    dict_digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
                   "six": 6, "seven": 7, "eight": 8, "nine": 9}

    for string in _1_submission.string_list:
        digits = []
        if any(key in string for key in dict_digits.keys()):
            digits.append([dict_digits[key] for key in dict_digits.keys() if key in string])

    result = digits[0] + digits[1]
    print("The decrypted code is", result)
    total_sum += int(result)

    print("\nThe total sum of it is", total_sum)


def calculation():
    total_sum = 0
    for string in _1_submission.string_list:
        digits = []
        for letter in string:
            if letter.isdigit():
                digits.append(letter)
                break

        for letter in reversed(string):
            if letter.isdigit():
                digits.append(letter)
                break

        result = digits[0] + digits[1]
        print("The decrypted code is", result)
        total_sum += int(result)

    print("\nThe total sum of it is", total_sum)


calculation_2()
