# Bingo

Kleines Python-Skript zum Ziehen von Bingo-Zahlen (1 bis 90) ohne Duplikate.

Das Skript merkt sich bereits gezogene Zahlen in einer lokalen Datei `numbers.csv`.
Bei jedem erneuten Start wird genau eine neue Zahl gezogen, bis alle 90 Zahlen verbraucht sind.

## Voraussetzungen

- Python 3.10+ (getestet mit Python 3.12)
- Keine externen Pakete notwendig

## Verwendung

```bash
python3 BingoNumberGenerator.py
```

Beispielausgabe:

```text
------------------
------- 42 -------
------------------
```

## Wie der Zustand gespeichert wird

- Datei: `numbers.csv`
- Inhalt: Kommagetrennte Ganzzahlen, z. B. `3,17,42,88`
- Die Datei wird automatisch erstellt, falls sie noch nicht existiert.

## Verhalten bei vollständiger Ziehung

Sobald alle Zahlen von 1 bis 90 gezogen wurden, gibt das Skript aus:

```text
Fertig! Nummern komplett!!
```

## Zurücksetzen

Wenn eine neue Runde gestartet werden soll, einfach `numbers.csv` löschen:

```bash
rm numbers.csv
```
