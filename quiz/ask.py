# US7 - Ergebnis anzeigen
from quiz.result import show_result


# US3: Multiple-Choice-Fragen
# Zeigt Fragen mit drei Antwortmöglichkeiten und prüft die Antwort.
def multiple_choice(question):
    print(question["question"])
    print("1.", question["option_a"])
    print("2.", question["option_b"])
    print("3.", question["option_c"])
    # Bei einer ungültigen Eingabe wird erneut nach einer Antwort gefragt.
    answer = input("Deine Antwort (1, 2 oder 3): ")

    while answer != "1" and answer != "2" and answer != "3":
        print("Ungültige Eingabe")
        answer = input("Deine Antwort (1, 2 oder 3): ")

    if answer == "1":
        selected_answer = "a"
    elif answer == "2":
        selected_answer = "b"
    else:
        selected_answer = "c"
    # Vergleicht die Antwort mit der Lösung und gibt True oder False zurück.
    return selected_answer == question["solution"]


# US 4 - Wahr/Falsch-Fragen
def ask_true_false(question):
    """Stellt eine Wahr/Falsch-Frage und prüft die Antwort.

    Gibt True zurück, wenn die Antwort richtig ist, sonst False.
    """
    choices = {"1": "a", "2": "b"}

    # Wiederholen, bis 1 oder 2 eingegeben wird (US 4).
    while True:
        print(question["question"])
        print("1. Wahr")
        print("2. Falsch")
        answer = input("Deine Antwort (1 oder 2): ").strip()

        if answer in choices:
            break

        print("Ungültige Eingabe")

    return choices[answer] == question["solution"]


# US 5 - Feedback nach jeder Antwort
def show_feedback(is_correct, question):
    """Zeigt an, ob die Antwort richtig war, sonst die Lösung."""
    if is_correct:
        print("Richtig!")
    else:
        correct_answer = question["option_" + question["solution"]]

        # In der CSV steht WAHR/FALSCH, angezeigt wird Wahr/Falsch.
        if question["type"] == "True/False":
            correct_answer = correct_answer.capitalize()

        print(f"Falsch! Die richtige Antwort ist: {correct_answer}")


# US 6 - Fehlerhafte Fragen erkennen
def has_valid_solution(question):
    """Prüft, ob die Lösung zum Fragetyp passt (a-c bzw. a-b)."""
    if question["type"] == "True/False":
        return question["solution"] in ["a", "b"]
    return question["solution"] in ["a", "b", "c"]


# US 6 - Nur die Fragen der gewählten Kategorie
def get_category_questions(questions, category):
    """Gibt alle Fragen zurück, die zur Kategorie gehören."""
    return [question for question in questions
            if question["category"] == category]


# US 6 - Alle Fragen einer Kategorie nacheinander
def run_quiz(questions, category):
    """Stellt alle Fragen einer Kategorie und zählt richtige Antworten.

    Fehlerhafte Fragen werden übersprungen und nicht gezählt.
    """
    correct = 0
    asked = 0

    for question in get_category_questions(questions, category):
        # Vorher prüfen, damit eine kaputte Frage gar nicht gestellt wird.
        if not has_valid_solution(question):
            print("Diese Frage ist fehlerhaft und wird übersprungen.")
            continue

        # Sicherheitsnetz, falls trotzdem ein Schlüssel fehlt.
        try:
            if question["type"] == "True/False":
                is_correct = ask_true_false(question)
            else:
                is_correct = multiple_choice(question)
            show_feedback(is_correct, question)
        except KeyError:
            print("Diese Frage ist fehlerhaft und wird übersprungen.")
        else:
            asked += 1
            if is_correct:
                correct += 1

    # US 7 - Zeigt Ergebnis an.
    show_result(correct, asked)
    return correct, asked


# Kleine Tests ohne Eingabe. Start im Projektordner mit:
# python -m quiz.ask
if __name__ == "__main__":
    test_questions = [
        {"category": "A", "type": "True/False", "solution": "a"},
        {"category": "A", "type": "True/False", "solution": "c"},
        {"category": "B", "type": "Multiple Choice", "solution": "c"},
        {"category": "B", "type": "Multiple Choice", "solution": "d"},
    ]

    print("has_valid_solution (erwartet: True False True False):")
    for test_question in test_questions:
        print(has_valid_solution(test_question))

    print("get_category_questions (erwartet: 2):")
    print(len(get_category_questions(test_questions, "A")))
