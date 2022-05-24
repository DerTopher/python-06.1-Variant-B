class Kunden:
    def __init__(self,
                 name,
                 alter,
                 kundennummer):
        self.name = name
        self.alter = alter
        self.kundennummer = kundennummer

##TODO: Warum verwenden Unternehmen eigentlich Kundennummern?

class Konten:
    def __init__(self,
                 kontostand,
                 kundennummer):
        self.kontostand = kontostand
        self.Kundennummer = kundennummer

    ##TODO: Funktionen/Methoden von Objekten - Welche Methoden kann man auf einem Konto ausführen - Gibt es Verschiedene Arten von Konten - Wie unterscheiden sie sich?

    def auszahlen(self,
                  kontostand,
                  auszahlungsbetrag):
        self.kontostand = kontostand - auszahlungsbetrag


##TODO: Vererbung von Eigenschaften

class Debitkonten(Konten):
    def __init__(self):

        ##TODO: Funktionen von Objekten
        pass

class Kreditkonten(Konten):
    def __init__(self):
        pass

class Bausparkonten(Konten):
    def __init__(self):
        pass
