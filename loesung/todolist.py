# 5 Ziel: Eine einfache To-Do-Liste erstellen.

# 1. Der Benutzer sollte in der Lage sein, To-Dos hinzuzufügen und zu entfernen.
# 2. Bei jedem Start des Programms sollte die Liste leer sein.
# 3. Eine Option anzeigen, um alle To-Dos auszugeben.

todos = []

while True:
    print("\n1. To-Do hinzufügen\n2. To-Do entfernen\n3. Alle To-Dos anzeigen\n4. Beenden")
    auswahl = input("Wähle eine Option (1/2/3/4): ")

    if auswahl == "1":
        todo = input("Was möchtest du hinzufügen? ")
        todos.append(todo)

    elif auswahl == "2":
        todo = input("Welches To-Do möchtest du entfernen? ")
        if todo in todos:
            todos.remove(todo)
        else:
            print("Dieses To-Do wurde nicht gefunden.")

    elif auswahl == "3":
        if todos:
            for todo in todos:
                print(todo)
        else:
            print("Deine To-Do-Liste ist leer!")

    elif auswahl == "4":
        break
