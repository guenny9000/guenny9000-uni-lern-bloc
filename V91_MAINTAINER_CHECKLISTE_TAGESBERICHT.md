# V91 Reality-First – Maintainer-Checkliste und Tagesbericht

Stand: 2026-10-12  
Zweck: Prüfaufträge und Ergebnisse nachvollziehbar dokumentieren. Diese Datei ist eine Arbeitsvorlage, kein Nachweis dafür, dass lokale Hardware, Live-Messungen oder ein Produktivsystem geprüft wurden.

## 1. Messwerte und Logs lokalisieren

- [ ] Vorhandene Messdateien und Logs an bekannten, zugänglichen Speicherorten suchen, bevor neue Dateien oder Messreihen angelegt werden.
- [ ] Für jeden Fund Dateipfad oder eindeutige Quelle, Zeitstempel samt Zeitzone, Messgröße, Einheit, Herkunft und Erfassungsmethode notieren.
- [ ] Status ausdrücklich klassifizieren: `GESPEICHERT`, `LIVE` oder `SIMULATION`.
- [ ] Messwerte nicht allein aufgrund eines Dateinamens, eines Statusfeldes oder einer Modellbehauptung als echt einstufen.
- [ ] Nicht zugängliche Speicherorte als `UNBEKANNT` kennzeichnen und den fehlenden Zugriff benennen.

## 2. Hardware-Schnittstellen prüfen

- [ ] Nur auf Systemen prüfen, für die tatsächlich autorisierter Zugriff besteht.
- [ ] Schnittstelle, Gerät, Treiber und verwendeten Prüfweg dokumentieren; Betriebssystem, Zeitpunkt und unveränderte Befehlsausgabe ergänzen.
- [ ] Code und Dokumentation vergleichen. Eine dokumentierte Schnittstelle ist noch kein Beleg für einen erfolgreichen Live-Zugriff.
- [ ] Keine Ports öffnen, Treiber installieren, Dienste stoppen oder Einstellungen ändern, nur um einen Prüfstatus zu erzeugen.
- [ ] Wenn lokale Prüfung nicht möglich ist: `UNBEKANNT – lokaler Zugriff fehlt`; benötigten Nachweis und den kleinsten sicheren nächsten Schritt nennen.

## 3. Fehler reproduzierbar untersuchen

- [ ] Betroffene Datei, Branch und Commit-SHA festhalten.
- [ ] Fehlerbeschreibung, Voraussetzungen und minimale Reproduktionsschritte dokumentieren.
- [ ] Tatsächliche Ausgabe und Exit-Code sichern; Geheimnisse, Zugangsdaten und personenbezogene Daten vorher entfernen.
- [ ] Test in einer isolierten, rücknehmbaren Umgebung durchführen, sofern autorisiert.
- [ ] Ursache nur dann als bestätigt bezeichnen, wenn ein Test sie stützt; sonst als Hypothese kennzeichnen.
- [ ] Vor und nach dem Test prüfen, ob Daten oder Dateien verändert wurden.

## 4. Pull Requests #3 und #234 prüfen

- [ ] Aktuellen PR-Status, Zielbranch, Quellbranch und Head-Commit-SHA abrufen.
- [ ] Änderungen gegenüber dem Zielbranch prüfen und relevante Dateien sowie Risiken benennen.
- [ ] CI-Ergebnisse mit Workflow, Lauf-ID, Commit-SHA und tatsächlich bestandenen Schritten dokumentieren.
- [ ] Tests möglichst reproduzierbar auf dem aktuellen Stand ausführen, wenn Zugriff und Berechtigung vorhanden sind.
- [ ] CI-Erfolg nicht als Beweis für Hardwarezugriff, Live-Telemetrie oder Produktivbetrieb ausgeben.
- [ ] Keine automatische Zusammenführung, Bereitstellung oder produktive Änderung aus dieser Checkliste ableiten.

## 5. Ledger und Audit prüfen

- [ ] Vorhandene Ledger-Datei und Verifikationsfunktion anhand des tatsächlichen Repository- oder lokalen Dateipfads identifizieren.
- [ ] Prüfen, was `verify_chain()` wirklich validiert: Reihenfolge, Vorgänger-Hashes, berechnete Hashes, Pflichtfelder und gegebenenfalls Zeitstempel.
- [ ] Prüfbefehl, Codeversion, Eingabedatei, unveränderte Ausgabe und Exit-Code festhalten.
- [ ] Ein Tagesbericht darf vorhandene Daten ergänzen, aber keine fehlenden Ereignisse rückdatieren oder erfinden.
- [ ] SHA-256 und `fsync()` allein machen einen Speicher nicht unveränderbar. Für einen WORM-Nachweis braucht es zusätzlich eine tatsächlich durchgesetzte Schreib-/Löschsperre oder unveränderbare Speicherung sowie einen unabhängig prüfbaren Nachweis.
- [ ] Keine Ledger-Historie überschreiben, zurücksetzen oder neu versiegeln, um einen Test grün erscheinen zu lassen.
- [ ] Einen Bericht nicht ungeprüft in ein WORM-Ledger schreiben. Erst Schema, Berechtigung, Append-Verfahren und Auswirkungen prüfen; bevorzugt zunächst einen getrennten Bericht außerhalb des Ledgers erstellen.

## 6. Unabhängige Gegenprüfung

- [ ] Jede prüfende Instanz nennt eigene Quellen und konkrete Fundstellen.
- [ ] Festhalten, ob Prüfungen unabhängig voneinander waren oder auf derselben Antwort, Datei oder Datenquelle beruhten.
- [ ] Übereinstimmung mehrerer Modelle ist kein Ersatz für Messdaten oder reproduzierbare Tests.
- [ ] Widersprüche offen dokumentieren und mit einem gezielten Test oder einer unabhängigen Quelle klären.

## 7. Tagesbericht – kopierbare Vorlage

```text
V91 REALITY-FIRST – TAGESBERICHT

Datum/Uhrzeit mit Zeitzone:
Prüfende Person/Instanz:
Ziel und Umfang:
Zugriff/Berechtigung tatsächlich vorhanden:
Geprüfte Repositorys, Branches und Commit-SHAs:
Geprüfte lokale Quellen/Pfade:
Vorhandene Messungen:
  - Quelle/Pfad:
  - Zeitstempel/Zeitzone:
  - Messgröße/Einheit:
  - Herkunft/Erfassungsmethode:
  - Einstufung: GESPEICHERT / LIVE / SIMULATION
Ausgeführte Befehle/Tests:
Unveränderte Ergebnisse, Exit-Codes und Protokollpfade:
Bestätigte Befunde:
Hypothesen / noch nicht bestätigte Ursachen:
UNBEKANNT / NICHT GETESTET:
  - Was fehlt:
  - Warum:
  - Was wurde geprüft:
  - Kleinster sicherer nächster Schritt:
Daten oder Systeme verändert: JA/NEIN
Wenn JA: genaue Änderung, Autorisierung und Rückweg:
Merge/Bereitstellung/Produktivänderung: JA/NEIN
Gesamteinstufung: BELEGT / TEILWEISE BELEGT / UNBEKANNT / WIDERLEGT
Offene Punkte und verantwortlicher nächster Schritt:
```

## 8. Regeln für Beispiele und Statuswerte

- Beispielberichte müssen sichtbar als `BEISPIEL – KEINE REALDATEN` markiert sein.
- Keine konkreten Sequenzen, Hashes, Knotennamen, Zeitstempel, Drift-Werte oder Statusmeldungen erfinden und als echte Betriebsdaten darstellen.
- Platzhalter wie `<SEQ AUS QUELLE>` und `<HASH AUS LEDGER>` verwenden, bis die Originalquelle geprüft wurde.
- `ACTIVE`, `SYNCED`, `VALID:TRUE`, `DRIFT:0/3` oder `CS:SECURE` sind Behauptungen, solange keine zugehörigen Rohdaten, Prüfmethode und Ergebnisse vorliegen.
- Erfunden wirkende oder nicht belegte Beispielknoten – etwa `SOLAR-DESKTOP-01`, `EDGE-PI-02` oder `WORKSHOP-NODE-03` – dürfen nicht als tatsächlich vorhandene Geräte ausgegeben werden.
- Ein beispielhafter Hash-Ausschnitt oder eine erfundene Sequenznummer ist kein Nachweis und darf nicht in den echten Tagesbericht oder das produktive Ledger übernommen werden.

## Reality-First-Schlussregel

**CLAIM ≠ EVIDENCE.** Eine Aussage gilt nur in dem Umfang als belegt, den Quelle, Zugriff und reproduzierbares Ergebnis tatsächlich tragen. `UNBEKANNT` ist ein gültiges Prüfergebnis, wenn Grund und nächster sicherer Klärungsschritt genannt werden. Statuszeichen, Modellbestätigung oder erfolgreiche CI-Läufe belegen für sich allein keinen Produktivbetrieb.
