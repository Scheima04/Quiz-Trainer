# Quiz Trainer

Ein Quiz-Programm in Python. Der User wählt eine Kategorie, beantwortet Fragen und sieht am Schluss sein Ergebnis. Der User kann zusätzlich eigene Kategorien und Fragen hinzufügen.

## So speichern wir eine Frage

Jede Frage hat 5 Angaben: Kategorie, Typ, Fragetext, Antworten und Lösung:

{
    "category": "Python",
    "type": "mc",
    "question": "Welcher Datentyp gibt input() zurück?",
    "options": ["int", "str", "float"],
    "solution": 2
}

- "mc" = Multiple Choice (3 Antworten), "tf" = Wahr/Falsch (2 Antworten)
- "solution" ist die Nummer der richtigen Antwort (1, 2 oder 3)
- Alle Fragen zusammen sind in einer Liste namens questions

## Welche Datei macht was

- main.py: Hauptmenü
- quiz/questions.py: Fragen laden
- quiz/ask.py: Fragen stellen und sagen, ob die Antwort richtig ist
- quiz/result.py: Ergebnis anzeigen
- quiz/manage.py: neue Kategorien und Fragen hinzufügen

## Wer macht was

- Dina (Story 1–3): Hauptmenü, Kategorie wählen, Multiple-Choice-Fragen
- Angela (Story 4–6): Wahr/Falsch-Fragen, Rückmeldung richtig/falsch, alle Fragen einer Kategorie durchgehen
- Scheima (Story 7–9): Ergebnis anzeigen, neues Quiz starten, Fragen aus CSV laden
- Besarta (Story 10–12): Kategorien und Fragen hinzufügen, Programm beenden

