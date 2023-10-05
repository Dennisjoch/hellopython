# 4 Ziel: Einfaches Ratespiel für Zahlen zwischen 1 und 10.

# 1. Der Computer "denkt" an eine Zahl zwischen 1 und 10 (verwende die random-Bibliothek).
# 2. Der Benutzer hat drei Versuche, diese Zahl zu erraten.
# 3. Nach jedem Versuch sollte der Computer mitteilen, ob die geratene Zahl zu hoch, zu niedrig oder korrekt ist.

import random

zahl = random.randint(1, 10)
versuche = 3

for _ in range(versuche):
    tipp = int(input("Rate eine Zahl zwischen 1 und 10: "))
    if tipp == zahl:
        print("Richtig geraten!")
        break
    elif tipp < zahl:
        print("Zu niedrig!")
    else:
        print("Zu hoch!")
