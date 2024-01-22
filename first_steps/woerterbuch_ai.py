woerter = {}
uebersetzungen = {}
with open("woerterbuch.txt", "r") as fobj:
    for line in fobj:
        line = line.strip()
        zuordnung = line.split(" ")
        woerter[zuordnung[0]] = zuordnung[1]
        if zuordnung[1] not in uebersetzungen:
            uebersetzungen[zuordnung[1]] = [zuordnung[0]]
        else:
            uebersetzungen[zuordnung[1]].append(zuordnung[0])

while True:
    wort = input("Geben Sie ein Wort ein (oder 'exit' zum Beenden): ")
    if wort.lower() == "exit":
        break

    found = False
    if wort in woerter:
        print("Die Übersetzung lautet:", woerter[wort])
        found = True

    if not found:
        if wort in uebersetzungen:
            print("Die Übersetzungen sind:")
            translations = ", ".join(uebersetzungen[wort])
            print(translations)
            found = True

    if not found:
        print("Das Wort ist unbekannt")