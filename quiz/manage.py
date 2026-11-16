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
    for question in questions:                             #Jede einzelne Frage wird durchgegangen
        if question["category"] not in categories:          #Wird geprüft, ob die Kategorie bereits in unserer Liste vorhanden ist.
            categories.append(question["category"])         #Falls nicht vorhanden, wird die Kategorie unserer Liste hinzugefügt.
    return categories                                       #Gibt alle Kategorien an

#User Story 10 + 11: Nutzer kann eine neue Frage mit der Funktion erstellen 
#create_question = fragt eine neue Frage ab und gibt sie als Dictionary in CSV-Format zurück. 

def create_question(questions, category):
    question_type = ask_choice("Frage-Typ (1.Multiple Choice, 2. Wahr/Falsch): ",                   #Hier entscheidet der Nutzer ob multiple Choice oder Wahr/Falsch.
                               {"1": "Multiple Choice", "2": "Wahr/Falsch"})
    text = ask_text("Fragetext: ")                                                                  #Hier wird die Frage des Nutzers eingegeben.

    if question_type == "Multiple Choice":                                                          #Falls Multiple Choice ausgewählt wird, braucht es 3 Antwortmöglichkeiten.
        options = [ask_text("Antwort 1: "), ask_text("Antwort 2: "), ask_text("Antwort 3: ")]
        letters = {"1": "a", "2": "b", "3": "c"}
    else: 
        options = ["Wahr", "Falsch", ""]                                                            #Ansonsten wird Wahr/Falsch ausgewählt und man braucht 2 Antwortmöglichkeiten.
        letters = {"1": "a", "2": "b"}

    solution = ask_choice(f"Nummer der richtigen Antwort (1-{len(letters)}): ", letters)

    return {                                                                                        #Funktion erstellt ein Dictionary mit allen Informationen zur Frage.
        "ID": f"{len(questions) + 1}",                                                              #Dieses Dictionary wird dann von add_question() oder add_category() verwendet. 
        "category": category,
        "type": question_type,
        "question": text, 
        "option_a": options[0],
        "option_b": options[1],
        "option_c": options[2],
        "solution": solution
    }

#User Stoy 10 + 11 Die neu erstellte Kategorie/Frage soll in der CSV-Datei gespeichert werden
#save_to_csv = Frage in der CSV-Datei speichern

def save_to_csv(questions):
    print("Speichern in die CSV-Datei.")                                            #Wird nach der Themenfolie 8 ergänzt.

#User Story 10 noch nicht vorhandene Kategorie hinzufügen
#add_category Kategorie hinzufügen

def add_category(questions):
    existing = [question["category"].lower() for question in questions]             #Hier werden alle Kategorien gesammelt, die bereits existieren. .lower wird angewendet, damit Gross- und Kleinschreibung keine Rolle spielen. 

    while True:                                                                     #Der Nutzer wird solange nach einem gültigen Namen gefragt.
        name = ask_text("Name der neuen Kategorie: ")       
        if name.lower() not in existing:                                            #Diese Funktion prüft, ob dieser Name schon existent ist. 
            break                                                                   #Wenn Name gültig ist, Wenn-Schleife verlassen.

        print("Ungültige Eingabe: Diese Kategorie gibt es schon.")                  #Falls die eingegebene Kategorie bereits existiert.

    questions.append(create_question(questions, name))                              #create_question(questions, name) hier weiss create_question, dass die neue Frage zur neuen Kategorie gehört. #und questions.append fügt die neue Frage zur Liste questions hinzu.
    save_to_csv(questions)
    print(f"Die Kategorie {name} wurde mit einer ersten Frage hinzugefügt.")        #Bestätigung für den Nutzer. f wird eingesetzt, da die Variable {name} benutzt wird. 

#User Story 11 Nutzer wählt eine bereits vorhandene Kategorie und erstellt dazu eine neue Frage.
#add_question Frage hinzufügen

def add_question(questions):
    categories = get_existing_categories(questions)                                            #Alle bereits vorhandenen Kategorien werden geholt. 

    if categories == []:                                                                       #Gibt es überhaupt bereits Kategorien.
        print("Es gibt noch keine Kategorie. Bitte zuerst eine Kategorie hinzufügen.")
    else: 
        choices = {}                                                                         #Falls Kategorie vorhanden ist, werden dem Nutzer die vorhandenen Kategorien gezeigt. choices = {} - leeres Dictionary wird erstellt, damit später die möglichen Antwortmöglichkeiten gepseichert werden können. 
        for i in range(len(categories)):                                                     #Alle Kategorien werden durchgegangen. 
              print(f"{i + 1}. {categories[i]}")                                               #Die Kategorien werden mit den Nummern angezeigt. i + 1, da Python bei 0 anfängt und wir ja dann nicht 0. Kategorie stehen haben wollen, sondern 1. Kategorie.
              choices[f"{i + 1}"] = categories[i]                                              #Hier wird, dass Dictionary aufgebaut. 
        category = ask_choice("Kategorie wählen: ", choices)

        questions.append(create_question(questions, category))                              #Hier wird eine neue Frage erstellt und anschliessend dann zur Frageliste hinzugefügt.
        save_to_csv(questions)                                                              #Wird zur CSV-Datei gespeichert, ohne die bereits vorhandenen Fragen zu löschen.
        print("Die Frage wurde hinzugefügt.")                                               #Bestätigung dür den Benutzer.