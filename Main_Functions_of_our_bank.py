from Objects_of_our_bank import Kunden

def header():
    print('-------------------------------------')
    print('           Ihre Spaßkasse')
    print('-------------------------------------')
    print()


def Hauptfunktion():

    Kundenliste = []
    firstinput = ""

    while firstinput != "B":
        firstinput = input("Was möchten Sie tun? [A]nzeigen, Kunden [H]inzufügen oder [B]eenden? ")
        if firstinput == "A":
            anzeigen(Kundenliste)
        elif firstinput == "H":
            Kundenliste = hinzufuegen(Kundenliste)

        ###Todo: Methode zum Anzeigen der Konten eines Kunden
        ###Todo: Methode zum Erstellen eines Kontos (Gleich abfragen, welcher Kontentyp?)
        ###Todo: Methode zum Geld einzahlen
        ###Todo: Methode zum Geld auszahlen

        elif firstinput == "B":
            print("Bye Bye")
        else:
            print("Eingabe nicht erkannt. Bitte wiederholen")


def anzeigen(Kundenliste):
    ##TODO For Schleife zum Anzeigen der Kunden (Eigenschaften des Objekts) (Q1 - E hat schon)
    print(Kundenliste)
    for kunde in Kundenliste:
        print(kunde.name)



def hinzufuegen(Kundenliste):
    ##TODO: Userinput als Argumente in Klasse geben, um Objekt zu erstellen

    #kundenname = input("Wer soll hinzugefügt werden? ")
    #kundenalter = input("Wie alt ist der Kunde? ")
    kundenname = "peter"
    kundenalter = 42

    ##TODO: Kundennummern automatisch generieren
    kundennummer = len(Kundenliste) + 1
    Kundenliste.append(Kunden(kundenname, kundenalter, kundennummer))
    return Kundenliste

if __name__ == '__main__':
    header()
    Hauptfunktion()
