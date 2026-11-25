# US1: Hauptmenü des Quiz-Trainers


from quiz.ask import run_quiz
from quiz.manage import kategorie_auswaehlen, add_category, add_question
from quiz.questions import load_questions


def hauptmenue():
    auswahl = ""

    # Das Menü wird wiederholt, bis der Nutzer 4 eingibt.
    while auswahl != "4":
        print("HAUPTMENÜ")
        print("1. Quiz starten")
        print("2. Kategorie hinzufügen")
        print("3. Frage hinzufügen")
        print("4. Programm beenden")

        auswahl = input("Bitte wähle eine Option: ")
        questions = load_questions()  # Fragen aus CSV laden

        if auswahl == "1":
            kategorie = kategorie_auswaehlen(questions)  # Kategorie auswählen
            run_quiz(questions, kategorie)  # Quiz starten

        elif auswahl == "2":
            print("Eigenes Quiz erstellen")
            add_category(questions)

        elif auswahl == "3":
            
            print("Quiz bearbeiten")

        elif auswahl == "4":
            print("Programm wird beendet.")

        else:
            print("Ungültige Eingabe")


