# Klasse Musikinstrument

class Musikinstrument():
    # Eigenschaften
    __modell = "unbekannt"
    __hersteller = "unbekannt"
    __preis = 0.0

    # Methoden
    def __init__(self, modell="", hersteller="", preis = 0.0):
        self.__modell = modell
        self.__hersteller = hersteller
        self.__preis = preis

    def set_modell(self, value):
        self.__modell = value

    def set_preis(self, value):
        self.__preis = value

    def get_modell(self):
        return self.__modell

    def get_daten(self):
        return self.__modell, self.__hersteller, self.__preis



class Gitarre(Musikinstrument):
    def __init__(self, modell = "unbekannt", hersteller = "unbekannt", preis = 0.0, groesse = "unbekannt"):
        super().__init__(modell, hersteller, preis)
        self.__groesse = groesse

    def get_groesse(self):
        return self.__groesse

    def set_groesse(self, value):
        self.__groesse = value