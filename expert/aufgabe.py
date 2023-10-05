# 1. Einführung und Installationsanleitung
# Installieren Sie Python von https://www.python.org/downloads/
# Starten Sie Ihr Terminal und führen Sie `python` oder `python3` aus, um die Python-Shell zu starten.

# 2. Grundlagen der Syntax und 3. Datentypen
# Deklarieren Sie eine leere Liste namens `todo_list` zur Speicherung der To-Dos.
todo_list = []

# Aufgabe: Definieren Sie eine Funktion namens "save_todos_to_file", die die "todo_list" in "meine_todos.txt" speichert.
# Verwenden Sie hierfür die Dateioperationen.

# Aufgabe: Vervollständigen Sie die Funktion, um die To-Dos aus der Datei zu laden.
def load_todos_from_file():
    pass

while True:
    print("Was möchten Sie tun? [hinzufügen, entfernen, anzeigen, beenden]")
    aktion = input()

    if aktion == 'beenden':
        # Aufgabe: Speichern Sie die "todo_list" in "meine_todos.txt", bevor Sie das Programm beenden.
        break

    elif aktion == 'hinzufügen':
        print("Welche Aufgabe möchten Sie hinzufügen?")
        aufgabe = input()
        # Aufgabe: Fügen Sie "aufgabe" zur "todo_list" hinzu.

    elif aktion == 'entfernen':
        print("Welche Aufgabe möchten Sie entfernen?")
        aufgabe = input()
        # Aufgabe: Entfernen Sie "aufgabe" aus der "todo_list", wenn sie vorhanden ist. Geben Sie eine Nachricht aus, wenn sie nicht gefunden wird.

    elif aktion == 'anzeigen':
        # Aufgabe: Laden Sie die "todo_list" aus "meine_todos.txt" und geben Sie sie aus.

    else:
        print("Unbekannte Aktion, bitte erneut versuchen.")

# Hinweis: Hier befindet sich ein Fehler, der behoben werden muss.
with open('../meine_todos.txt', 'w') as f:
    for item in todo_list:
        f.write(f"{item}\n")
