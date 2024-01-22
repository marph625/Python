urlaub = 26
alter = int(input("Wie alt sind Sie?"))
behinderung = str(input("Beträgt der Grad Ihrer Behinderung mindestens 50%?"))
betriebszugehoerigkeit = int(input("Wie viele Jahre sind sie bei uns angestellt?"))

if alter < 18:
    urlaub = urlaub + 4
elif alter > 55:
    urlaub += 2 # urlaub = urlaub + 2 ist urlaub +=2
if behinderung == "Ja" or behinderung == "ja":
    urlaub += 5
if betriebszugehoerigkeit > 10:
    urlaub += 2

print(f"Der Urlaubsanspruch beträgt {urlaub} Tage")

# int - integer - Ganzzahl (1, 2, 3 ....)
# float - Gleitkommazahlen (1.5, 3.14...)
# str - string - Text ("Hallo Welt")
# boolean - True/False 

