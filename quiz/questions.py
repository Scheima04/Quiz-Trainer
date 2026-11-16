
# US 9 – Fragen aus CSV laden

def load_questions():
    questions = []  # Leere Liste erstellen

    try:
        # CSV-Datei öffnen
        with open("quiz/quiz_9_fragen.csv", "r", encoding="utf-8-sig") as file:

            # Spaltennamen lesen
            header = file.readline().strip().split(";")

            # Jede Frage lesen
            for line in file:
                values = line.strip().split(";")  # Werte trennen

                # Anzahl der Spalten prüfen
                if len(values) == len(header):
                    question = {}  # Leeres Dictionary

                    # Spaltennamen und Werte verbinden
                    for i in range(len(header)):
                        question[header[i]] = values[i]

                    # Frage zur Liste hinzufügen
                    questions.append(question)

    # Fehler behandeln, falls Datei fehlt
    except FileNotFoundError:
        print("Fehler: CSV-Datei nicht gefunden.")

    return questions  # Alle Fragen zurückgeben
