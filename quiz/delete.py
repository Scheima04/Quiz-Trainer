import csv
from quiz.manage import kategorie_auswaehlen


# US13 - Quiz löschen
def delete_quiz(questions):

    # Prüfen, ob Quiz vorhanden sind
    if len(questions) == 0:
        print("Keine Quiz vorhanden.")
        return

    # Quiz auswählen
    kategorie = kategorie_auswaehlen(questions)

    # Bestätigung abfragen
    print("Ausgewähltes Quiz:", kategorie)
    bestaetigung = input("Quiz wirklich löschen? (Ja/Nein): ")

    if bestaetigung == "Ja":

        # Fragen der anderen Kategorien behalten
        neue_fragen = []

        for question in questions:
            if question["category"] != kategorie:
                neue_fragen.append(question)

        # Spaltennamen der CSV-Datei
        fields = ["ID", "category", "type", "question",
                  "option_a", "option_b", "option_c", "solution"]

        # CSV-Datei neu speichern
        try:
            with open("quiz/quiz_9_fragen.csv", "w",
                      newline="", encoding="utf-8-sig") as file:

                writer = csv.DictWriter(file, fieldnames=fields,
                                        delimiter=";")
                writer.writeheader()
                writer.writerows(neue_fragen)

            print("Quiz wurde gelöscht.")

        # Fehler beim Speichern abfangen
        except OSError:
            print("Fehler: CSV-Datei konnte nicht gespeichert werden.")

    else:
        print("Löschen wurde abgebrochen.")
