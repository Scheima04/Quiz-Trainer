#User Story 10+11: Der Nutzer kann eine neue Kategorie erstellen (Dazu noch leere Eingaben verhindern) und der Kategorie einen Namen geben.
#ask_text = frage den Nutzer nach einem Text.

def ask_text(prompt):                                       #Funktion fragt so lange, bis die Eingabe nicht leer ist und gibt den Text zurück.
    while True:                                             #Funktion wiederholen bis gültige Eingabe
        text = input(prompt).strip()                        #Hier wird vom Benutzer etwas eingegeben #.strip() entfernt Leerzeichen am Anfang und Ende

        if text != "":                                      #Prüfeung: Wurde etwas eingegeben?
            return text
        print("Ungültige Eingabe")                          #Falls keine Eingabe = Fehlermeldung


#User Story 10+11: Der Nutzer muss an verschiedenen Stellen eine gültige Auswahl treffen. Bsp: Fragetyp, Antwortmöglichkeiten + richtige Lösung.
#ask_choice = frage den Nutzer nach einer Auswahl.

def ask_choice(prompt, choices):                            #Funktion fragt so lange, bis die Eingabe ein Schlüssel von choices ist und gibt den passenden Wert zurück. #prompt = Was soll angezeigt werden? #choices = Welche Antworten sind erlaubt?
    while True:                                             #Funktion wiederholen bis gültige Eingabe
        answer = input(prompt).strip()                      #Hier wird vom Benutzer etwas eingegeben.

        if answer in choices:                               #Prüfung: Ist answer eine erlaubte Antwort?
            return choices[answer]                          #Falls erlaubt - Das eingegebene wiedergeben
        print("Ungültige Eingabe")                          #Antwort nicht in choices = Fehlermeldung


#User Story 11: Nutzer kann bereits vorhandene Kategorie auswählen
#get_existing_categories = hole die vorhandenen Kategorien

def get_existing_categories(questions):                     #Gibt jede vorhandene Kategorie genau einmal zurück.             
    categories = []                                         #Eine leere Liste wird erstellt

    for questions in questions:                             #Jede einzelne Frage wird durchgegangen
        if question["category"] not in categories:          #Wird geprüft, ob die Kategorie bereits in unserer Liste vorhanden ist.
            categories.append(question["category"])         #Falls nicht vorhanden, wird die Kategorie unserer Liste hinzugefügt.

    return categories                                       #Gibt alle Kategorien an




