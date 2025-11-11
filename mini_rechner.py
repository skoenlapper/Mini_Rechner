# Aufgaben:
# 1) Name eingeben und begrüßen
# 2) Zwei Zahlen eingeben
# 3) Rechenoptionen anzeigen und auswählen
# 4) Berechnungen mit if/elif/else durchführen
# 5) Schleife, um mehrere Rechnungen zu machen
# 6) Berechnungen in eigenen Funktionen
# 7) Ergebnis mit f-String ausgeben, Division durch 0 prüfen

# 1) Name eingeben und begrüßen
name = input("Wie heißt du? ")  # input() fragt den Nutzer nach seinem Namen
print(f"Hallo {name}! Willkommen zu deinem Mini-Rechner.")  # f-String zur personalisierten Ausgabe

# 6) Funktionen für Rechenoperationen erstellen
def addiere(a, b):  # Funktion zur Addition
    return a + b  # return gibt das Ergebnis zurück

def subtrahiere(a, b):  # Funktion zur Subtraktion
    return a - b

def multipliziere(a, b):  # Funktion zur Multiplikation
    return a * b

def dividiere(a, b):  # Funktion zur Division
    if b == 0:  # Überprüfung auf Division durch 0
        return "Fehler: Division durch 0!"  # Fehler zurückgeben
    else:
        return a / b  # sonst Division durchführen

def modulo(a, b):  # Funktion für Rest (Modulo)
    if b == 0:  # Überprüfung auf Division durch 0
        return "Fehler: Division durch 0!"
    else:
        return a % b  # Rest berechnen

# 5) Hauptschleife starten, damit mehrere Rechnungen möglich sind
while True:  # while True läuft endlos, bis wir break verwenden
    # 2) Zwei Zahlen eingeben
    zahl1 = float(input("Gib die erste Zahl ein: "))  # float() wandelt die Eingabe in eine Dezimalzahl um
    zahl2 = float(input("Gib die zweite Zahl ein: "))

    # 3) Rechenoptionen anzeigen
    print("Welche Operation möchtest du durchführen?")
    print("1) Addition")
    print("2) Subtraktion")
    print("3) Multiplikation")
    print("4) Division")
    print("5) Rest (Modulo)")

    auswahl = input("Deine Wahl (1-5): ")  # Auswahl des Nutzers speichern

    # 4) Berechnungen durchführen
    if auswahl == "1":  # Wenn 1 gewählt wird
        ergebnis = addiere(zahl1, zahl2)  # addiere-Funktion aufrufen
    elif auswahl == "2":  # Wenn 2 gewählt wird
        ergebnis = subtrahiere(zahl1, zahl2)
    elif auswahl == "3":  # Wenn 3 gewählt wird
        ergebnis = multipliziere(zahl1, zahl2)
    elif auswahl == "4":  # Wenn 4 gewählt wird
        ergebnis = dividiere(zahl1, zahl2)
    elif auswahl == "5":  # Wenn 5 gewählt wird
        ergebnis = modulo(zahl1, zahl2)
    else:  # Wenn etwas anderes eingegeben wird
        ergebnis = "Ungültige Auswahl!"  # Fehlermeldung

    # 7) Ergebnis ausgeben
    print(f"Das Ergebnis ist: {ergebnis}")  # f-String zeigt das Ergebnis an

    # 5) Abfrage, ob neue Rechnung gemacht werden soll
    weiter = input("Möchtest du eine neue Rechnung machen? (ja/nein) ").lower()  # .lower() wandelt Eingabe in Kleinbuchstaben
    if weiter != "ja":  # Wenn der Nutzer nicht "ja" sagt
        print(f"Okay {name}, danke fürs Rechnen! Bis zum nächsten Mal.")  # Abschiedsnachricht
        break  # Schleife beenden
