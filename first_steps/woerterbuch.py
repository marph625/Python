woerter = {}
fobj = open("Erste Schritte\woerterbuch.txt", "r")
for line in fobj:
    line = line.strip()
    zuordnung = line.split(" ")
    woerter[zuordnung[0]] = zuordnung[1]
fobj.close()
while True:
    wort = input("Geben Sie ein Wort ein: ")
    if wort in woerter:
        print("Das deutsche Wort lautet:", woerter[wort])
    elif wort == "Ende" or wort == "ende": # Groß- und Kleinschreibung möglich. Das geht bestimmt auch eleganter.
        print("Das Programm wird beendet")
        break
    else:
        print("Das Land ist unbekannt") 