fobj = open("Erste Schritte\woerterbuch.txt", "a")
woerter = {"Greece" : "Griechenland",
           "Chad" : "Tschad",
           "Iceland" : "Island"}
for engl in woerter:
    fobj.write("{} {}\n".format(engl, woerter[engl]))
fobj.close