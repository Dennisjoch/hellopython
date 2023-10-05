# 1. Einführung und Installationsanleitung
# Installieren Sie Python von https://www.python.org/downloads/
# Starten Sie Ihr Terminal und führen Sie `python` oder `python3` aus, um die Python-Shell zu starten.

# 2. Grundlagen der Syntax und 3. Datentypen
# Deklarieren Sie eine leere Liste namens `todo_list` zur Speicherung der To-Dos.
todo_list = []


def load_todos_from_file():
    try:
        with open('../meine_todos.txt', 'r') as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []


# 4. Operatoren und 5. Kontrollstrukturen
while True:
    print("Was möchten Sie tun? [hinzufügen, entfernen, anzeigen, beenden]")
    aktion = input()  # 7. Funktionen und Parameterübergabe

    if aktion == 'beenden':  # Vergleichsoperator und Kontrollstruktur
        break  # Schleife beenden

    elif aktion == 'hinzufügen':
        print("Welche Aufgabe möchten Sie hinzufügen?")
        aufgabe = input()
        todo_list.append(aufgabe)  # 6. Listen

    elif aktion == 'entfernen':
        print("Welche Aufgabe möchten Sie entfernen?")
        aufgabe = input()
        if aufgabe in todo_list:  # 4. Operatoren
            todo_list.remove(aufgabe)  # 6. Listen
        else:
            print("Aufgabe nicht gefunden.")

    elif aktion == 'anzeigen':
        todo_list = load_todos_from_file()
        print("Ihre To-Do-Liste:")
        for i, item in enumerate(todo_list):
            print(f"{i + 1}. {item}")

    else:
        print("Unbekannte Aktion, bitte erneut versuchen.")  # 3. Datentypen

# 9. Dateioperationen
with open('../meine_todos.txt', 'w') as f:  # 10. Fehlerbehandlung ist hier optional
    for item in todo_list:
        f.write(f"{item}\n")  # Datei schreiben
