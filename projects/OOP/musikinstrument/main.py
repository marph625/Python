# Import der Klasse Musikinstrument
from musikinstrument import Musikinstrument, Gitarre

# Instanziierung, anlegen eines Objektes

instrument = Musikinstrument("PRS Custom 24 BW", "PRS")
gitarre1 = Gitarre("SG Standard HC", "Gibson", 1689.0, 628)

def main():
    instrument.set_preis(3997.0)
    print(instrument.get_daten())
    print(gitarre1.get_daten())

# Aufruf
main()
