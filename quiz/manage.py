#Gemeinsame Hilfsfunktionen für User Story 10 und 11 (ask Text, ask_choice, get_existing_categories, create_question, save_to_csv)

#Funktion fragt einen Text ab und prüft, ob die Eingabe gültig ist.  
def ask_text(prompt):                                                                                      
    while True:                                             
        text = input(prompt)

        if text == "" or ";" in text:
            print("Ungültige Eingabe. Bitte gib deine Frage erneut ein. (Die Eingabe darf nicht leer sein und kein Semikolon (;) enthalten.") 
        else:                                     
            return text                      

#Funktion prüft die eingegebene Auswahl und gibt den passenden Wert zurück. (Dictionary)
def ask_choice(prompt, choices):                            
    while True:                                             
        answer = input(prompt)

        if answer not in choices:
            print("Ungültige Eingabe. Bitte wähle eine der angegebenen Nummern und versuche es erneut.") 
        else:           
            return choices[answer]                          
                                 
#Funktion sammelt alle vorhandenen Kategorien, ohne sie doppelt aufzulisten.
def get_existing_categories(questions):                                  
    categories = []   

    for question in questions:                             
        if question["category"] not in categories:          
            categories.append(question["category"])

    return categories                                       

#Funktion erstellt eine neue Frage mit Fragetyp, Antworten, Lösung und eigener ID. 
def create_question(questions, category):
    question_type = ask_choice("Welchen Fragetyp möchtest du wählen, 1. Multiple Choice oder 2. True/False?: ",{"1": "Multiple Choice", "2": "True/False"})
    text = ask_text("Wie lautet deine neue Quizfrage?: ")                                                                  

    if question_type == "Multiple Choice":                                                          
        options = [ask_text("Antwort 1: "), ask_text("Antwort 2: "), ask_text("Antwort 3: ")]
        letters = {"1": "a", "2": "b", "3": "c"}
    else: 
        options = ["WAHR", "FALSCH", ""]                                                            
        letters = {"1": "a", "2": "b"}

    solution = ask_choice("Welche Anwort ist richtig? Gib die entsprechende Nummer ein: ", letters)
   
    #Ermittelt die nächste ID, damit jede neue Frage eine eigene Nummer erhält.
    last_used_id = 0                       

    for question in questions: 
        number = int(question["ID"])

        if number > last_used_id:
            last_used_id = number

    new_id = last_used_id + 1
    
    return {                                                                                        
        "ID": str(new_id),                                                              
        "category": category,
        "type": question_type,
        "question": text, 
        "option_a": options[0],
        "option_b": options[1],
        "option_c": options[2],
        "solution": solution}

#Funktion speichert die neu hinzugefügte Frage in der CSV-Datei.
def save_to_csv(questions):
    question = questions[-1]

    with open("quiz/quiz_9_fragen.csv", "a", encoding="utf-8") as outfile:
        outfile.write(
            question["ID"] + ";" + 
            question["category"] + ";" +
            question["type"] + ";" +
            question["question"] + ";" +
            question["option_a"] + ";" +
            question["option_b"] + ";" +
            question["option_c"] + ";" +
            question["solution"] + "\n"       #Sorgt dafür, dass die nächste Frage in einer neuen Zeile stehen kann.
        )      

#User Story 10: Neue Kategorie hinzufügen
#Funktion prüft den Kategoriennamen und erstellt die erste Frage für diese Kategorie.
def add_category(questions):
    existing = get_existing_categories(questions)            

    while True:                                                                     
        name = ask_text("Wie soll die neue Kategorie heissen?: ")

        if name not in existing:     
            break
        else:                                       
            print("Diese Kategorie existiert leider bereits. Bitte wähle einen anderen Namen.")                                                                    

    print("Erstelle die erste Frage für deine neue Kategorie.") 

    #Exception Handling
    try:
        new_question = create_question(questions,name)                                      
        save_to_csv([new_question])

    #Fängt den Fehler ab, wenn die ID (der gelesene Text) nicht in eine Zahl umgewandelt werden kann.
    except ValueError:
        print("Die neue Kategorie konnte leider nicht erstellt werden, da die ID nicht in eine Zahl umgewandelt werden konnte. Bitte prüfen Sie deshalb die ID.")
        return

    #Fängt Fehler beim Öffnen oder Lesen der CSV-Datei ab.
    except OSError:
        print("Die neue Kategorie konnte leider nicht gespeichert werden. Bitte überprüfe, ob die Datei noch vorhanden ist und darin etwas gespeichert werden kann.")
        return
    
    questions.append(new_question)  
    print("Die neue Kategorie wurde erfolgreich hinzugefügt.")         

#User Story 11: Neue Frage hinzufügen.
#Funktion zeigt die vorhandenen Kategorien an und speichert eine neue Frage in der ausgewählten Kategorie. 
def add_question(questions):
    categories = get_existing_categories(questions)                                          

    if categories == []:                                                                     
        print("Es ist noch keine Kategorie vorhanden. Bitte füge zuerst eine Kategorie hinzu.")
        return
    
    choices = {}

    for i in range(len(categories)):                                                     
        print(f"{i + 1}. {categories[i]}")                                             
        choices[str(i + 1)] = categories[i] 

    category = ask_choice("Welche Kategorie soll die neue Frage erhalten?: ", choices)

    #Zusätzliche Funktion, um mehrere Fragen in der gleichen Kategorie hinzuzufügen, ohne die Kategorie erneut auswählen zu müssen.
    while True:

        #Exception Handling
        try: 
            new_question = create_question(questions, category)
            save_to_csv([new_question])     

        #Fängt den Fehler ab, wenn die ID (der gelesene Text) nicht in eine Zahl umgewandelt werden kann.
        except ValueError:
            print("Die neue Frage konnte leider nicht hinzugefügt werden, da die ID nicht in eine Zahl umgewandelt werden konnte. Bitte prüfen Sie deshalb die ID.")           
            return

        #Fängt Fehler beim Öffnen oder Lesen der CSV-Datei ab. 
        except OSError:
            print("Die neue Frage konnte leider nicht gespeichert werden. Bitte überprüfe, ob die Datei noch vorhanden ist und darin etwasgespeichert werden kann.")
            return

        questions.append(new_question)
        print("Die neue Frage wurde erfolgreich hinzugefügt und gespeichert.")     

        add_another_question = ask_choice("Möchtest du eine weitere Frage in dieser Kategorie hinzufügen? 1. Ja, 2. Nein: ", {"1": "Ja", "2": "Nein"})

        if add_another_question == "Nein":
            break      




# US2: Kategorie auswählen

def kategorie_auswaehlen(Quizes):
    kategorien = []

    # Kategorien aus den geladenen Fragen sammeln
    for quiz in Quizes:
        kategorie = quiz["category"]
        if kategorie not in kategorien:
            kategorien.append(kategorie)

    # Prüfen, ob Kategorien vorhanden sind
    if kategorien == []:
        print("Keine Kategorien vorhanden.")
        return None

    # Kategorien nummerieren und anzeigen
    nummer = 1
    for kategorie in kategorien:
        print(nummer, kategorie)
        nummer = nummer + 1

    # Gültige Kategorienummern sammeln
    nummern = []
    nummer = 1
    for kategorie in kategorien:
        nummern.append(str(nummer))
        nummer = nummer + 1

    # Kategorie auswählen
    auswahl = input("Wähle eine Kategorienummer: ")

    # Ungültige Eingaben erneut abfragen
    while auswahl not in nummern:
        print("Ungültige Kategorienummer")
        auswahl = input("Wähle eine Kategorienummer: ")

    # Ausgewählte Kategorie zurückgeben
    return kategorien[int(auswahl) - 1]