# Quiz Trainer

Der Quiz Trainer ist ein Python-Programm. Der Nutzer wählt eine Kategorie, beantwortet Multiple-Choice und Wahr/Falsch Fragen und sieht am Schluss sein Ergebnis. Zusätzlich kann er eigene Kategorien und Fragen hinzufügen. Die Fragen werden in einer CSV-Datei gespeichert.

## Funktionen

- Hauptmenü: Quiz starten, Kategorie hinzufügen, Frage hinzufügen, Programm beenden.
- Kategorie auswählen und die dazugehörigen Fragen nacheinander beantworten.
- Feedback nach jeder Antwort (richtig / falsch inkl. Lösung).
- Ergebnis mit Anzahl richtiger Antworten und Prozent.
- In der CSV-Datei sind die Fragen und Kategorien gespeichert.

## Projektstruktur 

```text
Quiz-Trainer/
  quiz/
    __init__.py          macht quiz zu einem Paket
    ask.py               Fragen stellen und Feedback
    manage.py            Kategorien und Fragen hinzufügen
    questions.py         Fragen aus der CSV-Datei laden
    quiz_9_fragen.csv    gespeicherte Fragen
    result.py            Ergebnis anzeigen
  .gitignore             Dateien, die Git ignoriert
  Flussdiagramm.pdf      Grober Ablauf
  main.py                Hauptmenü und Programmablauf
  README.md              Projektbeschreibung
```
    
## Programm starten

1. Repository klonen:
   ```text
   git clone https://github.com/Scheima04/Quiz-Trainer.git
   ```
2. In den Ordner wechseln:
   ```text
   cd Quiz-Trainer
   ```
3. Programm starten:
   ```text
   python main.py
   ```

## Datenformat der Fragen (CSV)

Spalten, getrennt durch `;`:

| Spalte | Bedeutung |
|---|---|
| ID | laufende Nummer |
| category | Kategorie, z. B. Geschichte |
| type | `Multiple Choice` oder `True/False` |
| question | Fragetext bzw. Aussage |
| option_a, option_b, option_c | Antwortmöglichkeiten (bei Wahr/Falsch ist `option_c` leer) |
| solution | richtige Antwort als Buchstabe: `a`, `b` oder `c` |

## Teamarbeit

- Arbeit nach User Stories aufgeteilt (siehe unten)
- Vor dem Arbeiten immer `git pull`, Commits mit Nachricht 
- Nur Code pushen, der ohne Fehler startet 

## Rolle

| Rolle | Beschreibung |
|---|---|
| Nutzer | Lernt mit dem Quiz Trainer: wählt eine Kategorie, beantwortet Fragen und sieht das Ergebnis. Erstellt ausserdem eigene Kategorien und Fragen, damit das Quiz zu den eigenen Lernthemen passt. |

## Aufteilung

| User Stories | Teilnehmerin |
|---|---|
| 1, 2, 3 | Dina Dzeliloska |
| 4, 5, 6 | Angela Davidovska |
| 7, 8, 9 | Scheima Gheriani |
| 10, 11, 12 | Besarta Sejdija |

---

## 1 – Hauptmenü

**Als Nutzer möchte ich das Hauptmenü sehen, damit ich auswählen kann, ob ich das Quiz starten, eine Kategorie oder eine Frage hinzufügen oder das Programm beenden möchte.**

Akzeptanzkriterien:
- Das Hauptmenü wird beim Start der Anwendung angezeigt.
- Jede der vier Optionen wird auf einer eigenen Zeile angezeigt:
  - «1. Quiz starten»
  - «2. Kategorie hinzufügen»
  - «3. Frage hinzufügen»
  - «4. Programm beenden»
- Die Kategorieauswahl des Quiz wird angezeigt, wenn der Nutzer die Option 1 («Quiz starten») im Hauptmenü auswählt.
- Die Eingabe einer neuen Kategorie wird gestartet, wenn der Nutzer die Option 2 («Kategorie hinzufügen») im Hauptmenü auswählt.
- Die Eingabe einer neuen Quizfrage wird gestartet, wenn der Nutzer die Option 3 («Frage hinzufügen») im Hauptmenü auswählt.
- Das Programm wird beendet, wenn der Nutzer die Option 4 («Programm beenden») im Hauptmenü auswählt.
- Bei einer ungültigen Eingabe erscheint «Ungültige Eingabe» und das Hauptmenü wird erneut angezeigt.

## 2 – Kategorie auswählen

**Als Nutzer möchte ich eine Quiz-Kategorie auswählen können, damit ich mein Wissen zu einem bestimmten Thema testen kann.**

Akzeptanzkriterien:
- Nach dem Start des Quiz werden die verfügbaren Kategorien angezeigt.
- Die Kategorien werden nummeriert dargestellt, damit der Nutzer eine davon auswählen kann.
- Der Nutzer kann durch Eingabe der entsprechenden Zahl eine Kategorie auswählen.
- Nach der Auswahl werden ausschliesslich Fragen aus der gewählten Kategorie angezeigt.
- Bei einer ungültigen Kategorienummer wird der Nutzer erneut zur Eingabe aufgefordert.

## 3 – Multiple-Choice-Fragen

**Als Nutzer möchte ich Multiple-Choice-Fragen beantworten können, damit ich zwischen verschiedenen Antwortmöglichkeiten wählen kann.**

Akzeptanzkriterien:
- Eine Multiple-Choice-Frage wird mit drei nummerierten Antwortmöglichkeiten angezeigt.
- Der Nutzer kann nur eine Antwort durch Eingabe der entsprechenden Zahl auswählen.
- Die ausgewählte Antwort wird mit der gespeicherten richtigen Lösung verglichen.

## 4 – Wahr/Falsch-Fragen

**Als Nutzer möchte ich Wahr/Falsch-Fragen beantworten können, damit ich entscheiden kann, ob eine Aussage stimmt oder nicht.**

Akzeptanzkriterien:
- Eine Wahr/Falsch-Frage wird als Aussage angezeigt.
- Der Nutzer erhält zwei Antwortmöglichkeiten: «1. Wahr» und «2. Falsch».
- Die Antwort wird durch Eingabe von 1 oder 2 ausgewählt.
- Wenn etwas anderes als 1 oder 2 eingegeben wird, erscheint «Ungültige Eingabe» und die Aussage wird erneut angezeigt.
- Die ausgewählte Antwort wird mit der gespeicherten Lösung verglichen.

## 5 – Feedback nach jeder Antwort

**Als Nutzer möchte ich nach jeder Antwort erfahren, ob sie richtig oder falsch war, damit ich aus meinen Fehlern lernen kann.**

Akzeptanzkriterien:
- Nach jeder beantworteten Frage wird angezeigt, ob die Antwort richtig, falsch oder ungültig war.
- Bei einer richtigen Antwort erscheint «Richtig!».
- Bei einer falschen Antwort erscheint «Falsch!».
- Bei einer Eingabe, die keiner vorhandenen Antwortmöglichkeit entspricht, erscheint die Rückmeldung «Ungültige Eingabe».
- Nach einer ungültigen Eingabe kann der Nutzer erneut antworten.
- Bei einer falschen Antwort wird zusätzlich die richtige Lösung angezeigt.

## 6 – Alle Fragen einer Kategorie nacheinander

**Als Nutzer möchte ich alle Fragen einer Kategorie nacheinander beantworten können, damit ich das Quiz dieser Kategorie vollständig abschliessen kann.**

Akzeptanzkriterien:
- Nach der Auswahl einer Kategorie wird die erste Frage dieser Kategorie angezeigt.
- Nach einer richtigen oder falschen Antwort wird die nächste Frage derselben Kategorie angezeigt, sofern weitere Fragen vorhanden sind.
- Jede Frage wird innerhalb eines Quizdurchgangs nur einmal gestellt.
- Der Quizdurchgang umfasst ausschliesslich die Fragen der ausgewählten Kategorie.
- Erst wenn alle Fragen dieser Kategorie beantwortet wurden, wird der Quizdurchgang beendet und die Ergebnisauswertung angezeigt.
- Fragen aus anderen Kategorien werden nicht automatisch gestartet.

## 7 – Ergebnis anzeigen

**Als Nutzer möchte ich nach Abschluss des Quiz mein Ergebnis sehen, damit ich einschätzen kann, wie gut ich die Fragen beantwortet habe.**

Akzeptanzkriterien:
- Nach Abschluss aller Fragen einer Kategorie wird das Quiz-Ergebnis angezeigt.
- Die Anzahl der richtig beantworteten Fragen wird im Verhältnis zur Gesamtzahl der Fragen angezeigt.
- Der Anteil der richtig beantworteten Fragen wird zusätzlich in Prozent berechnet und angezeigt.

## 8 – Weiteres Quiz starten

**Als Nutzer möchte ich nach Abschluss eines Quiz ein weiteres Quiz starten können, damit ich mein Wissen in anderen Kategorien testen kann.**

Akzeptanzkriterien:
- Nach der Ergebnisauswertung wird das Hauptmenü erneut angezeigt.
- Über das Hauptmenü kann ein neues Quiz gestartet werden.
- Beim Start eines neuen Quiz werden die verfügbaren Kategorien erneut angezeigt.
- Der Nutzer kann dieselbe oder eine andere Kategorie auswählen.
- Der Punktestand wird für jeden Quizdurchgang auf null zurückgesetzt.
- Die Ergebnisse des vorherigen Quiz beeinflussen den neuen Durchgang nicht.

## 9 – Fragen aus CSV laden

**Als Nutzer möchte ich, dass die gespeicherten Quizfragen beim Start des Programms geladen werden, damit ich die vorhandenen Kategorien und Fragen nutzen kann.**

Akzeptanzkriterien:
- Die Quizfragen und Antworten werden in einer separaten CSV-Datei gespeichert.
- Zu jeder Frage werden die Kategorie, der Frage-Typ, die Frage, die Antwortmöglichkeiten und die Lösung gespeichert.
- Beim Start des Programms werden die vorhandenen Quizfragen aus der CSV-Datei eingelesen.
- Die geladenen Fragen werden der jeweiligen Kategorie zugeordnet.
- Die Fragen können anschliessend im Quiz angezeigt und beantwortet werden.
- Änderungen an den Fragen in der Datei können beim nächsten Programmstart übernommen werden, ohne dass der Python-Code angepasst werden muss.
- Neu gespeicherte Fragen und Kategorien stehen auch nach einem Neustart des Programms zur Verfügung.

## 10 – Neue Kategorie hinzufügen

**Als Nutzer möchte ich eine neue Kategorie mit einer ersten Quizfrage hinzufügen können, damit das Quiz um weitere Themen erweitert werden kann.**

Akzeptanzkriterien:
- Über die Option 2 («Kategorie hinzufügen») im Hauptmenü kann eine neue Kategorie erstellt werden.
- Der Nutzer kann einen Namen für die neue Kategorie eingeben.
- Anschliessend kann der Nutzer eine erste Quizfrage für diese Kategorie eingeben.
- Der Nutzer kann den Frage-Typ (Multiple Choice oder Wahr/Falsch), die Antwortmöglichkeiten und die richtige Lösung festlegen.
- Die neue Kategorie wird zusammen mit der ersten Frage in der CSV-Datei gespeichert.
- Die neue Kategorie erscheint anschliessend bei der Kategorieauswahl und bleibt auch nach einem Neustart des Programms verfügbar.
- Ist der Kategoriename leer oder existiert die Kategorie bereits, erscheint «Ungültige Eingabe» und der Name wird erneut abgefragt.
- Als richtige Lösung sind bei Multiple Choice nur 1–3 gültig, bei Wahr/Falsch nur 1–2. Bei einer anderen Eingabe erscheint «Ungültige Eingabe» und die Lösung wird erneut abgefragt.

## 11 – Neue Frage hinzufügen

**Als Nutzer möchte ich neue Quizfragen hinzufügen können, damit das Quiz um weitere Inhalte erweitert werden kann.**

Akzeptanzkriterien:
- Über die Option 3 («Frage hinzufügen») im Hauptmenü kann eine neue Quizfrage hinzugefügt werden.
- Der Nutzer kann eine bereits vorhandene Kategorie auswählen, zu der die neue Frage gehören soll.
- Der Nutzer kann festlegen, ob es sich um eine Multiple-Choice- oder eine Wahr/Falsch-Frage handelt.
- Anschliessend können die Frage und die dazugehörigen Antwortmöglichkeiten eingegeben werden.
- Die richtige Antwort kann festgelegt werden.
- Die neue Frage wird in der CSV-Datei gespeichert, ohne bereits vorhandene Fragen zu löschen.
- Nach einem Neustart des Programms steht die neue Frage im Quiz zur Verfügung.

## 12 – Programm beenden

**Als Nutzer möchte ich den Quiz Trainer über das Hauptmenü beenden können, damit ich das Programm schliessen kann, wenn ich fertig bin.**

Akzeptanzkriterien:
- Im Hauptmenü wird die Option «4. Programm beenden» angezeigt.
- Der Nutzer kann das Programm durch Eingabe von 4 beenden.
- Vor dem Beenden erscheint eine kurze Abschiedsmeldung «Auf Wiedersehen!».
- Nach der Auswahl wird das Programm beendet und es werden keine weiteren Quizfragen angezeigt.
- Bereits gespeicherte Quizfragen bleiben in der CSV-Datei erhalten.