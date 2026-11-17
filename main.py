
# user wählt menupunkt



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

    # Das Menü wird wiederholt, bis der Nutzer 4 eingibt.
    while auswahl != "4":
        print("HAUPTMENÜ")
        print("1. Quiz starten")
        print("2. Eigenes Quiz erstellen")
        print("3. Quiz bearbeiten")
        print("4. Programm beenden")

        auswahl = input("Bitte wähle eine Option: ")

        if auswahl == "1":
            kategorie_auswaehlen()

        elif auswahl == "2":
            print("Eigenes Quiz erstellen")

        elif auswahl == "3":
            print("Quiz bearbeiten")

        #Dieser Teil gehört auch zur User Story 12: Programm beenden
        elif auswahl == "4":
            print("Programm wird beendet.")

        else:
            print("Ungültige Eingabe")





# US2: Kategorie auswählen

def kategorie_auswaehlen():
    kategorien = ["Geschichte", "Mathe", "Geografie"]

    # Die Kategorien werden nummeriert und angezeigt.
    nummer = 1
    for kategorie in kategorien:
        print(nummer, kategorie)
        nummer = nummer + 1

    auswahl = input("Wähle eine Kategorie (1-3): ")

    # Bei ungültiger Eingabe wird erneut gefragt.
    while auswahl != "1" and auswahl != "2" and auswahl != "3":
        print("Ungültige Kategorienummer")
        auswahl = input("Wähle eine Kategorie (1-3): ")

    # Die ausgewählte Kategorie wird zurückgegeben.
    return kategorien[int(auswahl) - 1]


# Hauptprogramm starten

def main():
    hauptmenue()


if __name__ == "__main__":
    main()
