**CheatSheet.md**
```markdown
# Python Cheat Sheet

## Grundlagen

- **Kommentare**: Zeilen, die mit `#` beginnen, werden vom Python-Interpreter ignoriert und dienen zur Erklärung des Codes: 
  ```python
  # Dies ist ein Kommentar
  ```

- **Ausgabe**: Verwenden Sie die `print`-Funktion, um Text oder Variablenwerte auszugeben:
  ```python
  print("Hallo Welt!")
  ```

- **Eingabe**: Mit der `input`-Funktion können Sie den Benutzer um Eingaben bitten:
  ```python
  name = input("Geben Sie Ihren Namen ein: ")
  ```

## Variablen und Datentypen

- **Integer (Ganzzahlen)**: Ganze Zahlen ohne Dezimalstellen. 
  ```python
  x = 10
  ```

- **Float (Fließkommazahlen)**: Zahlen mit Dezimalstellen. 
  ```python
  y = 20.5
  ```

- **Strings (Zeichenketten)**: Text. Kann in Einzel- oder Doppelzitaten geschrieben werden.
  ```python
  name = "Max"
  ```

- **Listen**: Eine Sammlung von Werten, die geändert werden kann.
  ```python
  fruechte = ["Apfel", "Banane", "Kirsche"]
  ```

- **Tupel**: Eine Sammlung von Werten, die nicht geändert werden kann.
  ```python
  farben = ("rot", "grün", "blau")
  ```

- **Sets**: Eine Sammlung von eindeutigen Werten.
  ```python
  set_a = {1, 2, 3}
  ```

- **Dictionaries**: Eine Sammlung von Schlüssel-Wert-Paaren. Ähnlich wie Listen, aber jedes Element hat einen eindeutigen Schlüssel.
  ```python
  person = {"name": "Max", "alter": 25}
  ```

## Kontrollstrukturen

- **If-Bedingung**: Erlaubt es, Code nur unter bestimmten Bedingungen auszuführen.
  ```python
  if x > 10:
      print("x ist größer als 10")
  elif x == 10:
      print("x ist 10")
  else:
      print("x ist kleiner als 10")
  ```

- **For-Schleife**: Wiederholt einen Codeblock für jedes Element in einer Liste oder einem anderen iterierbaren Objekt.
  ```python
  for frucht in fruechte:
      print(frucht)
  ```

- **While-Schleife**: Wiederholt einen Codeblock, solange eine bestimmte Bedingung erfüllt ist.
  ```python
  while x < 20:
      print(x)
      x += 1
  ```

## Funktionen

- **Definition**: Ein Codeblock, der eine bestimmte Aufgabe ausführt und durch einen Namen identifiziert wird.
  ```python
  def begruessung(name):
      return "Hallo " + name + "!"
  ```

- **Aufruf**: Ausführen der vorher definierten Funktion.
  ```python
  begruessung("Anna")
  ```

## Klassen und Objekte

- **Klassendefinition**: Ein Entwurf oder eine Vorlage für Objekte mit ähnlichen Eigenschaften und Methoden.
  ```python
  class Auto:
      def __init__(self, marke, modell):
          self.marke = marke
          self.modell = modell
          
      def anzeigen(self):
          return f"Dies ist ein {self.marke} {self.modell}"
  ```

  - `__init__`: Dies ist der Konstruktor der Klasse. Er wird aufgerufen, wenn ein Objekt der Klasse erstellt wird.
  - `self`: Bezieht sich auf das aktuelle Objekt.

- **Objekterstellung**: Erzeugen eines Objekts basierend auf einer Klasse.
  ```python
  mein_auto = Auto("Audi", "A4")
  print(mein_auto.anzeigen())
  ```

## Fehlerbehandlung

- **Try-Except**: Erlaubt das Fangen und Behandeln von Fehlern während der Laufzeit.
  ```python
  try:
      x = 1 / 0
  except ZeroDivisionError:
      print("Teilung durch Null!")
  ```

## Module und Pakete

- **PIP**: Ein Paketmanager für Python, mit dem Sie externe Bibliotheken installieren können.
  
- **Installation von Bibliotheken mit PIP**: 
  ```
  pip install bibliotheksname
  ```

- **Importieren von Modulen/Bibliotheken**: 
  ```python
  import math
  from datetime import datetime
  ```