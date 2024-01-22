def ordinalSuffix(num):
    if num == 1:
        print(str(num) + "st")
    elif num == 2:
        print(str(num) + "nd")
    elif num == 3:
        print(str(num) + "rd")
    else:
        print(str(num) + "th")


ordinalSuffix(0)
ordinalSuffix(1)
ordinalSuffix(2)
ordinalSuffix(3)
ordinalSuffix(4)
ordinalSuffix(5)


#assert ordinalSuffix(0) == '0th'
assert ordinalSuffix(1) == "1st"
assert ordinalSuffix(2) == '2nd'
assert ordinalSuffix(3) == '3rd'
assert ordinalSuffix(4) == '4th'
assert ordinalSuffix(10) == '10th'
assert ordinalSuffix(11) == '11th'
assert ordinalSuffix(12) == '12th'
assert ordinalSuffix(13) == '13th'
assert ordinalSuffix(14) == '14th'
assert ordinalSuffix(101) == '101st'
