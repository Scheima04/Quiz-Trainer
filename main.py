
# US1: Hauptmenü des Quiz-Trainers
def hauptmenue():
    auswahl = ""
# Das Hauptmenü wird wiederholt, bis der Nutzer 4 eingibt.
    while auswahl != "4":
        print("\n--- HAUPTMENÜ ---")
        print("1. Quiz starten")
        print("2. Kategorie hinzufügen")
        print("3. Frage hinzufügen")
        print("4. Programm beenden")

        auswahl = input("Bitte wähle eine Option: ")
# Je nach Eingabe wird die passende Option ausgewählt.
        if auswahl == "1":
            print("Kategorieauswahl wird gestartet.")

        elif auswahl == "2":
            print("Neue Kategorie hinzufügen.")

        elif auswahl == "3":
            print("Neue Frage hinzufügen.")

        elif auswahl == "4":
            print("Programm wird beendet.")

        else:
            print("Ungültige Eingabe")


hauptmenue()



# US2: Kategorie auswählen
# Zeigt die Kategorien an und lässt den Nutzer eine auswählen.
def kategorie_auswaehlen():
    kategorien = ["Geschichte", "Mathe", "Geografie"]

    print("\n--- KATEGORIEN ---")
# Die Kategorien werden nummeriert und angezeigt.
    nummer = 1
    for kategorie in kategorien:
        print(nummer, kategorie)
        nummer = nummer + 1

    auswahl = input("Wähle eine Kategorie (1-3): ")
# Bei ungültiger Eingabe muss der Nutzer erneut wählen.
    while auswahl != "1" and auswahl != "2" and auswahl != "3":
        print("Ungültige Kategorienummer")
        auswahl = input("Wähle eine Kategorie (1-3): ")

    print("Gewählte Kategorie:", kategorien[int(auswahl) - 1])
# Die ausgewählte Kategorie wird zurückgegeben.
    return kategorien[int(auswahl) - 1]

# Ruft die Kategorieauswahl zum Testen auf.
kategorie_auswaehlen()
