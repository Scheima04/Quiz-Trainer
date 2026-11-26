# US1: Hauptmenü des Quiz-Trainers


from quiz.ask import run_quiz
from quiz.manage import kategorie_auswaehlen, add_category, add_question
from quiz.questions import load_questions
from quiz.delete import delete_quiz 

def hauptmenue():
    auswahl = ""

    # Das Menü wird wiederholt, bis der Nutzer 5 eingibt.
    while auswahl != "5":
        print("HAUPTMENÜ")
        print("1. Quiz starten")
        print("2. Kategorie hinzufügen")
        print("3. Frage hinzufügen")
        print("4. Quiz löschen")
        print("5. Programm beenden")

        auswahl = input("Bitte wähle eine Option: ")
        questions = load_questions()  # Fragen aus CSV laden

        if auswahl == "1":
            kategorie = kategorie_auswaehlen(questions)  # Kategorie auswählen
            if kategorie != None:
                run_quiz(questions, kategorie)  # Quiz starten

        elif auswahl == "2":
            print("Kategorie hinzufügen")
            add_category(questions)

        elif auswahl == "3":
            print("Frage hinzufügen")
            add_question(questions)

        elif auswahl == "4":
            print("Quiz löschen")
            delete_quiz(questions)

        elif auswahl == "5":
            print("Auf Wiedersehen!")

        else:
            print("Ungültige Eingabe")


