# Hier werden dem Nutzer die Quizfragen gestellt, seine Antworten geprüft und ihm ein Feedback gegeben.

test_question = {
    "ID": "1",
    "category": "Python",
    "type": "True/False",
    "question": '"3" + 2 ergibt 5.',
    "option_a": "WAHR",
    "option_b": "FALSCH",
    "option_c": "",
    "solution": "b"
}

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

# result = ask_true_false(test_question)
# print(result)

def show_feedback(is_correct, question):
    if is_correct:
        print("Richtig!")
    else:
        correct_answer = question["option_" + question["solution"]]
        print(f"Falsch! Die richtige Antwort is: {correct_answer}")

result = ask_true_false(test_question)
show_feedback(result, test_question)
