# Kommentare in Python beginnen mit einem '#'. Der Interpreter ignoriert sie, sie dienen zur Erklärung des Codes.

# In vielen Programmiersprachen, besonders in kompilierten Sprachen wie C oder Java,
# wird der Datentyp einer Variable explizit angegeben. Zum Beispiel: int age = 1;
# Python ist jedoch dynamisch typisiert. Das bedeutet, dass der Datentyp einer Variable zur Laufzeit bestimmt wird.

age = 1  # In Python wird dies als Integer (Ganze Zahl) erkannt.
name = "Anna"  # Dies wird als String (Zeichenkette) erkannt.

# Python erkennt den Typ automatisch, basierend auf dem zugewiesenen Wert.
# Das macht den Code oft kürzer und einfacher zu lesen.

# Die 'main'-Funktion ist der Einstiegspunkt für viele Programme.
# In Python wird sie jedoch oft weggelassen, da Skripte von oben nach unten ausgeführt werden.
# In größeren Programmen oder Modulen wird jedoch oft eine 'main'-Funktion verwendet
# zusammen mit diesem speziellen Block, um den Code besser zu strukturieren:

def main():
    print("Das ist die main Funktion!")

# Dieser spezielle Block führt die 'main'-Funktion aus, wenn das Skript direkt ausgeführt wird:
if __name__ == "__main__":
    main()

# Warum ist das nützlich? Wenn jemand dieses Python-Modul in einem anderen Script importiert,
# wird der Code im obigen Block nicht automatisch ausgeführt. Das ermöglicht eine bessere Modularität.

# Datenanalyse:
# Datenanalyse in Python wird oft mit speziellen Bibliotheken wie Pandas und NumPy durchgeführt.
# Sie bieten leistungsstarke Werkzeuge zur Verarbeitung und Analyse von Daten.
# Hier ist ein sehr einfaches Beispiel mit Pandas:

# zuerst müssen Sie Pandas installieren: pip install pandas
import pandas as pd

# Erstellen eines einfachen Datenframes (eine Art Tabelle in Pandas)
data = {
    'Namen': ['Anna', 'Erik', 'John'],
    'Alter': [28, 34, 22]
}

df = pd.DataFrame(data)

# Anzeigen des Durchschnittsalters
print(f"Durchschnittsalter: {df['Alter'].mean()}")

# Pandas bietet viele andere Funktionen zur Datenmanipulation und -analyse.

# Das ist nur die Spitze des Eisbergs für Datenanalyse in Python.
# Für umfangreiche Datenanalysen sollten Sie weitere Ressourcen und Tutorials zu Pandas, NumPy und verwandten Bibliotheken konsultieren.
