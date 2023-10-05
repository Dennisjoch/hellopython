# Einführung in Python und Grundlagen der Programmierung

## 1. Was ist Python?
Python ist eine interpretierte, interaktive und objektorientierte Programmiersprache. Sie wurde entwickelt, um sowohl einfach zu lesen als auch zu schreiben zu sein. Python eignet sich hervorragend für Anfänger, die Programmieren lernen möchten.

## 2. Grundlagen der Programmierung

### 2.1 Datentypen

- **Integer (int)**: Dies ist der Datentyp für ganze Zahlen. Beispiel: `5`, `-3`, `0`.

- **Float**: Dies ist der Datentyp für Gleitkommazahlen. Beispiel: `5.0`, `-3.5`.

- **String (str)**: Eine Zeichenkette oder Text. Beispiel: `"Hallo Welt!"`.

- **Liste**: Eine geordnete Sammlung von Elementen. Die Elemente können von gemischten Datentypen sein. Beispiel: `[1, 2, "Drei"]`.

### 2.2 Variablen

Eine Variable dient dazu, Daten zu speichern, die während der Programmausführung verwendet werden können. Zum Beispiel:
```python
name = "Anna"
alter = 30
```

### 2.3 Operatoren

- **Arithmetische Operatoren**: `+`, `-`, `*`, `/`, `%` (Modulus), `**` (Potenz), `//` (ganzzahlige Division).
  
- **Vergleichsoperatoren**: `==` (ist gleich), `!=` (ungleich), `<`, `>`, `<=`, `>=`.

### 2.4 Kontrollstrukturen

- **if, elif und else**: Zum Testen von Bedingungen.
```python
if bedingung:
    # Anweisungen
elif andere_bedingung:
    # Andere Anweisungen
else:
    # Wieder andere Anweisungen
```

- **Schleifen**: `for` und `while`. Diese werden verwendet, um Anweisungen mehrfach auszuführen.

### 2.5 Funktionen

Eine Funktion ist ein Block von organisiertem, wiederverwendbarem Code, der verwendet wird, um eine einzelne, verwandte Aktion auszuführen. Funktionen bieten eine bessere Modularität und eine hohe Wiederverwendungsrate für Anwendungen.

```python
def funktionsname(parameter1, parameter2):
    # Anweisungen
    return etwas
```

## 3. Dateioperationen

In Python können Sie Dateien lesen und schreiben. Zum Beispiel:
```python
with open('dateiname.txt', 'r') as datei:
    inhalt = datei.read()
```

## 4. Die Aufgabe

Ihre Aufgabe ist es, eine einfache To-Do-Liste in Python zu vervollständigen. Verwenden Sie die oben genannten Konzepte, um die fehlenden Teile des bereitgestellten Codes zu vervollständigen.

---

# Infos

**pip**

`pip` ist das Paketverwaltungssystem von Python, mit dem Sie Softwarepakete aus dem Python Package Index (PyPI) installieren können. PyPI ist ein Repository für Open-Source-Softwarepakete von Drittanbietern für den Python-Programmierspracheneinsatz. Einfach ausgedrückt, ermöglicht `pip` Python-Entwicklern, Bibliotheken und Tools zu installieren und zu verwalten, die sie in ihren Projekten verwenden möchten.

---

**Pandas mit pip installieren**

Um `pandas` zu installieren, benötigen Sie zunächst `pip`. `pip` ist standardmäßig in Python-Versionen ab 3.4 enthalten. Falls Sie `pip` noch nicht installiert haben oder sich nicht sicher sind, können Sie dies überprüfen, indem Sie folgenden Befehl in Ihrem Terminal oder Ihrer Kommandozeile ausführen:

```bash
pip --version
```

Wenn `pip` installiert ist, wird eine Version angezeigt. Wenn nicht, müssen Sie `pip` zuerst installieren.

Sobald `pip` installiert ist, können Sie `pandas` wie folgt installieren:

```bash
pip install pandas
```

---

**Was ist Pandas?**

`pandas` ist eine leistungsstarke und flexible Open-Source-Datenanalysebibliothek für Python. Es bietet Datenstrukturen und Datenanalyse-Tools, die speziell für den schnellen und einfachen Datenaufschluss und die Datenmanipulation konzipiert sind. Ein zentrales Feature von `pandas` ist das DataFrame-Objekt, eine zweidimensionale Tabelle ähnlich einer Excel-Tabelle oder einer SQL-Tabelle. Mit `pandas` können Sie große Datenmengen laden, bearbeiten und analysieren, was es zu einem wesentlichen Werkzeug für Datenwissenschaftler und Analysten macht.
