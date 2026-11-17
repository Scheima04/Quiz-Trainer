#Gemeinsame Hilfsfunktionen für User Story 10 und 11 (ask Text, ask_choice, get_existing_categories, create_question, save_to_csv)

#Funktion fragt einen Text ab und prüft, ob die Eingabe gültig ist.  
def ask_text(prompt):                                                                                      
    while True:                                             
        text = input(prompt)

        if text == "" or ";" in text:
            print("Ungültige Eingabe") 
        else:                                     
            return text                      

#Funktion prüft die eingegebene Auswahl und gibt den passenden Wert zurück. (Dictionary)
def ask_choice(prompt, choices):                            
    while True:                                             
        answer = input(prompt)

        if answer not in choices:
            print("Ungültige Eingabe") 
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
    question_type = ask_choice("Fragetyp (1.Multiple Choice, 2. True/False): ",{"1": "Multiple Choice", "2": "True/False"})
    text = ask_text("Fragetext: ")                                                                  

    if question_type == "Multiple Choice":                                                          
        options = [ask_text("Antwort 1: "), ask_text("Antwort 2: "), ask_text("Antwort 3: ")]
        letters = {"1": "a", "2": "b", "3": "c"}
    else: 
        options = ["WAHR", "FALSCH", ""]                                                            
        letters = {"1": "a", "2": "b"}

    solution = ask_choice("Nummer der richtigen Antwort:", letters)
   
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
        name = ask_text("Name der neuen Kategorie: ")

        if name not in existing:     
            break
        else:                                       
            print("Ungültige Eingabe")                                                                    

    print("Bitte erstelle die erste Frage.")      
    new_question = create_question(questions,name)          
    questions.append(new_question)                              
    save_to_csv(questions)

    print("Kategorie erfolgreich hinzugefügt.")         

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

    category = ask_choice("Kategorie wählen: ", choices)
    new_question = create_question(questions, category)
    questions.append(new_question)                              
    save_to_csv(questions)     

    print("Die Frage wurde hinzugefügt.")                                                


 
# US2: Kategorie auswählen

def kategorie_auswaehlen(Quizes):
    kategorien = []

    # Kategorien aus den geladenen Fragen sammeln
    for quiz in Quizes:
        kategorie = quiz["category"]

        if kategorie not in kategorien:
            kategorien.append(kategorie)


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