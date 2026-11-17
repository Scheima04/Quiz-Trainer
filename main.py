from quiz.Interface.userInterface import show_menu
def main():
    show_menu()
# zeige menu
def show_menu():
    pass

# user wählt menupunkt

if __name__ == '__main__':
    main()

### muss noch überarbeitet werden
### 1. Quiz starten
    # zeige kategorien dem user 
    #user wählt kategorie und quiz startet

### 2. Eigenes Quiz erstellen
    # user nach kategoriebezeichnung fragen
#kategorie existiert schon, dann was?
#kategorie existiert noch nicht, dann was?
# while not Nein:
    # geben sie die erste frage ein
    # fragetype wählen "MC oder True False"
    # geben sie die antwort zur frage ein
    # weitere frage hinzufügen? Ja oder Nein
#hier wichtig mehrere antwortoptionen sammeln und speicher pro frage und die richtige antwort muss markiert werden, damit sie beim quizz dann als richtig zählt

# 3. Quiz berarbeiten
    #kategorie ändern?
    # frage berarbeiten
        #alle fragen zeigen und user wählt frage welcher er oder sie bearbeiten möchte
        # welche auswahl soll bearbeitet werden z.b. option 3 bei MC?
    #frage löschen
    #frage hinzufügen

# Quiz löschen
    # alle qiuz anzeigen und user fragen welches löschen und dann löschen
# ### 4. Programm beenden»


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
hauptmenue()
kategorie_auswaehlen()
