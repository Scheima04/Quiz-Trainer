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

# Hier werden dem Nutzer die Quizfragen gestellt, seine Antworten geprüft und ihm ein Feedback gegeben.

# Testfragen (nur zum Testen, später kommen die Fragen aus der CSV Datei)

test_question_1 = {
    "ID": "1",
    "category": "Python",
    "type": "True/False",
    "question": '"3" + 2 ergibt 5.',
    "option_a": "WAHR",
    "option_b": "FALSCH",
    "option_c": "",
    "solution": "b"
}

test_question_2 = {
    "ID": "2",
    "category": "Python",
    "type": "True/False",
    "question": "range(1, 5) enthält die Zahl 5.",
    "option_a": "WAHR",
    "option_b": "FALSCH",
    "option_c": "",
    "solution": "b"
}

test_question_3 = {
    "ID": "3",
    "category": "Geographie",
    "type": "True/False",
    "question": "Bern ist die Hauptstadt der Schweiz.",
    "option_a": "WAHR",
    "option_b": "FALSCH",
    "option_c": "",
    "solution": "a"
}

test_questions = [test_question_1, test_question_2, test_question_3]




def ask_true_false(question):
    choices = {"1": "a", "2": "b"}

    while True:
        print(question["question"])
        print("1. Wahr")
        print("2. Falsch")
        answer = input("Deine Antwort (1 oder 2): ").strip()

        if answer in choices:
            break
        
        print("Ungültige Eingabe")

    return choices[answer] == question["solution"]

def show_feedback(is_correct, question):
    if is_correct:
        print("Richtig!")
    else:
        correct_answer = question["option_" + question["solution"]]
        print(f"Falsch! Die richtige Antwort ist: {correct_answer}")

def run_quiz(questions, category):
    category_questions = [question for question in questions if question["category"] == category]
    correct = 0

    for question in category_questions:
        if question["type"] == "True/False":

            is_correct = ask_true_false(question)
        else:
            is_correct = multiple_choice(question)              # multiplechoice wurde hinzugefügt 

        show_feedback(is_correct, question)

        if is_correct:
            correct += 1

    # US 7 – Ergebnis anzeigen
    show_result(correct, len(category_questions))

    return correct, len(category_questions)