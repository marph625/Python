import random

geheimnis = random.randrange(20)
versuch = -1
zaehler = 0

while versuch != geheimnis:
    versuch = int(input("Ich denke an eine zufällige Zahl die größer als 0 und kleiner oder gleich 20 ist. Welche ist es?"))
    if versuch < geheimnis:
        print("Zu klein!")
    if versuch > geheimnis:
        print("Zu groß!")
    zaehler = zaehler + 1
print("Super! Sie haben es in",zaehler ,"Versuchen geschafft!")