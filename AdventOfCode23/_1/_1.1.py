import _1_submission


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


calculation()
