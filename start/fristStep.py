# Kommentare in Python beginnen mit einem '#'. Der Interpreter ignoriert sie, sie dienen zur Erklärung des Codes.

# Eine Variable ist wie eine Box, in der wir Informationen speichern können.
name = "Anna"  # Hier speichern wir den String "Anna" in der Variable namens "name".

# Wir können den Wert einer Variable mit der Funktion 'print' ausgeben.
print(name)  # Dies wird "Anna" ausgeben.

# Python hat verschiedene Datentypen, hier sind einige davon:

# Integer (Ganze Zahlen)
zahl = 5

# Float (Fließkommazahlen)
fließkommazahl = 5.5

# Strings (Zeichenketten)
text = "Hallo Welt!"

# Listen (geordnete Sammlungen von Elementen)
liste = [1, 2, 3, "Vier", "Fünf"]

# Wir können Bedingungen in unserem Code überprüfen mit 'if', 'elif' und 'else':
alter = 18
if alter < 20:
    print("Du bist ein Teenager!")
else:
    print("Du bist ein Erwachsener!")

# Schleifen helfen uns, Aufgaben mehrfach auszuführen. Hier ist eine 'for'-Schleife:
for nummer in range(5):  # Das wird die Zahlen 0 bis 4 ausgeben.
    print(nummer)

# Funktionen sind kleine Programmteile, die eine bestimmte Aufgabe erledigen. Sie können sie selbst erstellen:

def begrüßung(name):
    """Diese Funktion gibt eine Begrüßung aus."""  # Das ist ein Dokumentationsstring, der die Funktion beschreibt.
    return "Hallo, " + name + "!"

# Jetzt rufen wir die Funktion auf:
nachricht = begrüßung("Erik")
print(nachricht)  # Das wird "Hallo, Erik!" ausgeben.

# Dateioperationen: Hier ist, wie man eine Datei liest:
# (Achtung: Die Datei "beispiel.txt" muss existieren.)
with open('beispiel.txt', 'r') as datei:
    inhalt = datei.read()
    print(inhalt)

# Und so schreibt man in eine Datei:
with open('beispiel.txt', 'w') as datei:
    datei.write("Das ist ein Beispieltext.")

# Es gibt noch viel mehr zu lernen, aber das sind einige der Grundlagen von Python!
