import _1_submission

_1 = "one"
_2 = "two"
_3 = "three"
_4 = "four"
_5 = "five"
_6 = "six"
_7 = "seven"
_8 = "eight"
_9 = "nine"

# dict_digits = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
#                6: "six", 7: "seven", 8: "eight", 9: "nine"}
dict_digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5,
               "six": 6, "seven": 7, "eight": 8, "nine": 9}


def calculation():
    total_sum = 0
    for string in _1_submission.string_list:
        digits = []
        for key in dict_digits.keys():
            if key in string:
                digits.append(key)
        # else:
        #     for letter in string:
        #         # CHANGE CODE HERE 1.2
        #         if letter.isdigit():
        #             digits.append(letter)
        #             break
        for key in dict_digits.keys():
            if key in reversed(string):
                digits.append(key)
        # else:
        #     for letter in reversed(string):
        #         # AND HERE 1.2
        #         if letter.isdigit():
        #             digits.append(letter)
        #             break

        result = digits[0] + digits[1]
        print("The decrypted code is", result)
        total_sum += int(result)

    print("\nThe total sum of it is", total_sum)


calculation()
