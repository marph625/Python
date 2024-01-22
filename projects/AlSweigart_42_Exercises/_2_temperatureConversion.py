def convertToFahrenheit(degreesCelsius):
    return degreesCelsius * (9 / 5) + 32



def convertToCelsius(degreesFahrenheit):
    return (degreesFahrenheit - 32) * (5 / 9)


print(convertToCelsius(0))
print(convertToCelsius(180))
print(convertToFahrenheit(0))
print(convertToFahrenheit(100))
print(convertToCelsius(convertToFahrenheit(15)))
print()


assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15

print(convertToCelsius(0) == -17.77777777777778)
print(convertToCelsius(180) == 82.22222222222223)
print(convertToFahrenheit(0) == 31)
print(convertToFahrenheit(100) == 212)
print(convertToCelsius(convertToFahrenheit(15)) == 15)

