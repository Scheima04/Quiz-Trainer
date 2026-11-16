
# User Story 7 – Ergebnis anzeigen
# Nach dem Quiz werden die richtigen Antworten und der Prozentwert angezeigt.


def show_result(correct, total):                            # Funktion für die Ergebnisauswertung
    if total > 0:   
        percentage = correct / total * 100                  # Prozentwert berechnen, wenn Fragen vorhanden sind
    else:
        percentage = 0                                      # Wenn keine Fragen vorhanden sind, ist das Ergebnis 0 %

    print("===== QUIZ ERGEBNIS =====")                      # Ergebnis im Terminal anzeigen
    print(f"Richtige Antworten: {correct} von {total}")
    print(f"Ergebnis: {percentage:.2f} %")
