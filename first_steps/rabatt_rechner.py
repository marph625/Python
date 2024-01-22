print("Willkommen beim Rabattotron 5000!")
umsatz = int(input("Geben Sie Ihren Umsatz in € ein."))
if umsatz >= 100 and umsatz < 500:
    print("Die Höhe Ihrer Rechnung beträgt abzüglich 5% Rabatt:", umsatz - umsatz * 0.05, "€")
elif umsatz >= 500:
    print("Die Höhe Ihrer Rechnung beträgt abzüglich 10% Rabatt:", umsatz - umsatz * 0.1, "€")
else: print("Die Höhe Ihrer Rechung beträgt ohne Rabatt: ",umsatz, "€")