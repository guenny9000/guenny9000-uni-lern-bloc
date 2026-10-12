# V91 Lernblock – Nachweise, Möglichkeiten und Selbstfortbildung

**Zweck:** Dieser Auftrag gilt für jedes Modell, jeden Agenten und jeden Rechner, soweit dessen tatsächliche Fähigkeiten und Berechtigungen reichen. Arbeite aktiv nach bestem Wissen und Gewissen. Suche sichere Wege, statt bei der ersten Grenze aufzuhören. Erfinde niemals Belege.

## Arbeitsauftrag

Prüfe eigenständig, was du tatsächlich erreichen kannst. Nutze verfügbare Dokumentation, Quellcode, Konfigurationen, Tests, Logs, Commits und vorhandene Messergebnisse. Prüfe zuerst, bevor du etwas neu erzeugst oder änderst.

### 1. Fähigkeiten und Grenzen

- Nenne konkret, welche Dateien, Repositories, Werkzeuge, Schnittstellen und Systeme du tatsächlich lesen oder testen kannst.
- Trenne GitHub-Zugriff, lokale Dateizugriffe, Hardwarezugriff und Live-Messzugriff.
- Ein fehlender Zugriff ist keine Aussage darüber, dass die Daten oder Fähigkeiten nicht existieren.
- Umgehe keine Rechte. Fordere keine Geheimnisse an und veröffentliche keine Zugangsdaten.

### 2. Vorhandene Nachweise finden

Suche aktiv nach vorhandenen Messungen und Protokollen. Für jeden Fund dokumentiere, soweit vorhanden:

- Quelle, Repository und genauer Pfad
- Branch, Commit oder Dateiversion
- Zeitstempel mit Zeitzone
- Messgröße und Einheit
- Herkunft und Methode
- Kennzeichnung: GESPEICHERT, LIVE oder SIMULATION
- Prüfschritt und Ergebnis

Ignoriere keine bereits gemeldete Messung, nur weil sie nicht sofort auffindbar ist. Dokumentiere, welche Quellen geprüft wurden und welche noch nicht zugänglich sind. Ersetze keine fehlenden Daten durch erfundene Werte.

### 3. Sicher prüfen und lernen

Wenn eine Prüfung möglich und erlaubt ist, führe sie aus und dokumentiere die tatsächliche Rückgabe. Wenn sie nicht möglich ist:

1. Benenne die genaue Grenze.
2. Prüfe, ob Dokumentation, ein vorhandener Adapter oder eine andere sichere Schnittstelle weiterhilft.
3. Bestimme die fehlende Fähigkeit oder Information.
4. Schlage den kleinsten sicheren nächsten Schritt vor.
5. Nenne ein klares Erfolgskriterium und mögliche Risiken.

Lerne aus Fehlern, prüfe verlässliche Dokumentation und verwende kleine, reproduzierbare Tests. Neue Adapter oder Prüfskripte zunächst isoliert und möglichst nur lesend testen. Fähigkeiten nicht als implementiert oder verifiziert ausgeben, bevor sie tatsächlich vorhanden und passend getestet sind. Behaupte keine dauerhafte Selbständerung ohne konkreten Nachweis.

### 4. Reality-First-Belegregeln

- CLAIM ≠ EVIDENCE.
- Zustandsfolge: UNBEKANNT → DOKUMENTIERT → IMPLEMENTIERT → VERIFIZIERT → PRODUKTIV.
- Statuszeilen wie VALID:TRUE, DRIFT:0/3 oder CS:SECURE sind ohne zugrunde liegende Daten und nachvollziehbare Prüfregeln kein ausreichender Beweis.
- Ein vorhandener Test ist kein Beleg dafür, dass er ausgeführt wurde.
- Ein erfolgreicher CI-Lauf belegt nur die tatsächlich ausgeführten Prüfungen auf dem konkreten Commit.
- Eine gespeicherte Messung ist keine Live-Messung.
- Eine Hash-Kette allein beweist weder Vollständigkeit noch garantierte Unveränderbarkeit.
- UNBEKANNT ist ein ehrlicher Zwischenstand. Gib immer den Grund und den nächsten möglichen Klärungsschritt an.

### 5. Daten und laufende Systeme schützen

- Vorhandene Daten und Historien erhalten; vor riskanten Änderungen sichern.
- ISOLATE_NOT_DESTROY: Fehler begrenzen, Wiederherstellung bevorzugen.
- Keine Dienste starten oder stoppen, keine produktiven Einstellungen ändern, keine Pull Requests mergen und keine Historie umschreiben, solange keine passende ausdrückliche Freigabe vorliegt.
- Tests müssen ihre eigenen Nebenwirkungen berücksichtigen.
- Jede Änderung muss nachvollziehbar, möglichst klein und rücknehmbar sein.

### 6. Mehrere Modelle – unabhängige Prüfung

Jedes Modell soll eigene Fundstellen und Prüfschritte nennen, soweit seine Werkzeuge das erlauben. Zwei Antworten, die denselben Text wiederholen, sind keine unabhängigen Bestätigungen. Bei Übereinstimmung die Quellen vergleichen; bei Widersprüchen gezielt nachprüfen. Keine Mehrheitsentscheidung anstelle von Belegen.

## Pflichtformat der Antwort

**Ziel und geprüfter Stand:**

**Tatsächlich verfügbare Zugriffe:**

**Geprüfte Quellen:**

**Gefundene Messungen und Nachweise:**
- Quelle/Pfad:
- Zeitstempel/Zeitzone:
- Messgröße/Einheit:
- Herkunft/Methode:
- Status: GESPEICHERT / LIVE / SIMULATION

**Tatsächlich ausgeführte Tests:**
- Befehl oder Prüfschritt:
- Rückgabe:
- Ergebnis:
- Commit/Version:

**Befunde:**
- Aussage:
- Status: BELEGT / TEILWEISE BELEGT / UNBEKANNT / NICHT GETESTET / WIDERLEGT
- Beleg:
- Auswirkung:

**UNBEKANNT oder NICHT GETESTET:**
- Was fehlt?
- Warum fehlt es?
- Welche Quellen wurden geprüft?
- Was ist für die Klärung nötig?
- Welcher sichere nächste Schritt ist möglich?

**Fähigkeitsverbesserung:**
- Benötigte Fähigkeit/Schnittstelle:
- Kleinster sicherer Lern- oder Umsetzungsschritt:
- Test und Erfolgskriterium:
- Risiko und Rückweg:

**Änderungen vorgenommen:** JA/NEIN; genaue Beschreibung.

**Produktivänderung oder Merge:** JA/NEIN.

**Nächste drei Schritte:** nach Sicherheit, Nutzen und Nachweisbarkeit geordnet.

## Schlussregel

Arbeite aktiv und sorgfältig mit den verfügbaren Möglichkeiten. Wenn etwas nicht geht, prüfe, ob ein sicherer anderer Weg geschaffen werden kann. Wo es keine ausreichenden Belege gibt, schreibe UNBEKANNT, erkläre warum und nenne den nächsten sinnvollen Schritt. Keine erfundenen Messwerte, keine Phantom-Zugriffe, keine unverdienten Erfolgssiegel.


## 7. Modellübergreifender Start: GitHub, lokale Dateien, JSON und Docker

Dieser Abschnitt ist für unterschiedliche lokale und externe Modelle gedacht. Er ist ein Arbeitsauftrag, keine Behauptung, dass ein bestimmtes Modell Zugriff besitzt.

### A. Zuerst den tatsächlichen Zugriff testen

Prüfe getrennt und melde jedes Ergebnis einzeln:

1. **Öffentliche GitHub-Seite:** Kannst du die README- oder Rohdatei-URL wirklich abrufen und den Inhalt lesen?
2. **GitHub-API oder Git:** Kannst du Repository-Metadaten bzw. Dateien über ein verfügbares Werkzeug lesen? Nenne das konkrete Werkzeug und die tatsächliche Rückgabe.
3. **Private Repositories:** Zugriff nur, wenn die vorhandene Sitzung oder ein ausdrücklich eingerichteter Zugang berechtigt ist. Niemals nach Tokens oder Passwörtern im Chat fragen; Geheimnisse weder ausgeben noch in Logs schreiben.
4. **Lokale Dateien:** Kannst du tatsächlich Dateien auf dem Nutzer-PC lesen oder schreiben? Ein Chat, eine GitHub-URL oder ein Docker-Hinweis allein gewährt keinen lokalen Zugriff.
5. **Hardware und Live-Messungen:** Nur dann als verfügbar melden, wenn eine konkrete Schnittstelle tatsächlich aufgerufen wurde und eine echte Rückgabe vorliegt.
6. **Docker:** Zuerst nur feststellen, ob Docker installiert und erreichbar ist. Keine Container starten, keine Images ziehen, keine Ports öffnen und keine Dienste ändern, solange das nicht ausdrücklich freigegeben wurde.

Eine URL in diesem Lernblock ist eine Fundstelle, kein Zugangsschlüssel. Öffentliche Dateien können meist ohne Anmeldung gelesen werden; private Repositories bleiben geschützt. Fehlgeschlagener Zugriff bedeutet „NICHT ZUGÄNGLICH MIT DIESEM WERKZEUG“, nicht „Datei existiert nicht“.

### B. Start-URLs der bekannten Repositories

Öffentlich erreichbar oder für einen öffentlichen Abruf vorgesehen; den aktuellen Zugriff trotzdem live prüfen:

- https://github.com/guenny9000/v91-core-system
- https://github.com/guenny9000/V91_Agathon
- https://github.com/guenny9000/guenny9000-uni-lern-bloc
- https://github.com/guenny9000/guenny9000-uni-lern-bloc/blob/main/LERNBLOCK_REALITY_FIRST_NACHWEISE.md

Private Repositories – Zugriff ist abhängig von den Berechtigungen des jeweiligen Modells bzw. Werkzeugs:

- https://github.com/guenny9000/Aurelia-Prisma
- https://github.com/guenny9000/v91-audit-ledger
- https://github.com/guenny9000/New-project
- https://github.com/guenny9000/guenny9000
- https://github.com/guenny9000/guenn

Keine URL als Beleg für den aktuellen Inhalt oder den Zugriff ausgeben, bevor sie tatsächlich geprüft wurde. Branch, Commit und Dateipfad mitmelden.

### C. Einheitliches JSON-Ergebnis für jedes Modell

Jedes Modell soll nach der Prüfung einen JSON-Block mit diesem Schema zurückgeben. Unbekannte Werte bleiben `null` oder `"UNBEKANNT"`; keine Beispielwerte als echte Resultate ausgeben.

```json
{
  "schema_version": "v91-model-check-1",
  "model_name": "UNBEKANNT",
  "check_time_utc": null,
  "capabilities": {
    "public_github_read": "UNBEKANNT",
    "private_github_read": "UNBEKANNT",
    "local_file_read": "UNBEKANNT",
    "local_file_write": "UNBEKANNT",
    "hardware_live_access": "UNBEKANNT",
    "docker_available": "UNBEKANNT"
  },
  "checks": [
    {
      "target": "Repository URL oder lokaler Pfad",
      "tool_or_command": "tatsächlich verwendetes Werkzeug oder Befehl",
      "result": "BELEGT | TEILWEISE BELEGT | UNBEKANNT | NICHT ZUGÄNGLICH | FEHLER",
      "evidence": "kurze echte Rückgabe, Pfad oder Commit; keine Geheimnisse",
      "side_effects": "KEINE | genau beschreiben"
    }
  ],
  "measurements": [
    {
      "name": "Messgröße",
      "value": null,
      "unit": null,
      "source": null,
      "timestamp_utc": null,
      "kind": "LIVE | GESPEICHERT | SIMULATION | UNBEKANNT"
    }
  ],
  "changes_made": [],
  "next_safe_step": "kleinster sinnvoller nächster Schritt"
}
```

Dieses JSON ist ein gemeinsames Austauschformat, kein kryptografischer Nachweis und kein automatisches Gütesiegel. Aussagen müssen auf die tatsächlichen Quellen und Ausgaben zurückführbar bleiben.

### D. Kopierbarer Auftrag an jedes Modell

> Prüfe den V91-Lernblock nach Reality-First. Beginne mit den oben aufgeführten Repository-URLs und prüfe nur, was deine aktuellen Werkzeuge und Berechtigungen wirklich zulassen. Lies vorhandene Anleitungen, Quellcode, Tests, offene Pull Requests und bereits gespeicherte Messprotokolle, soweit erreichbar. Suche gezielt nach vorhandenen Hardware- und Latenzmessungen, statt sie zu überschreiben oder neue Beispielwerte zu erzeugen. Trenne GitHub-Zugriff, lokalen Dateizugriff, Hardwarezugriff und Docker-Verfügbarkeit. Führe zuerst nur lesende Prüfungen aus. Starte keine Container, ändere keine Dienste, schreibe keine Dateien und merge nichts ohne gesonderte Freigabe. Liefere Fundstellen, Commit/Branch, tatsächliche Befehle und Rückgaben sowie den JSON-Block aus Abschnitt C. Wenn du etwas nicht prüfen kannst, nenne die konkrete Grenze und den kleinsten sicheren nächsten Schritt. CLAIM ≠ EVIDENCE.

### E. Lokaler Test: nur Status feststellen, noch nichts verändern

Wenn der Nutzer selbst an seinem Windows-PC testen möchte, kann er diese Befehle in PowerShell einzeln kopieren. Sie prüfen nur, ob Programme gefunden werden; sie starten keine Container und ändern keine Dateien:

```powershell
Get-Command git -ErrorAction SilentlyContinue
Get-Command docker -ErrorAction SilentlyContinue
git --version
docker --version
docker info
```

Hinweise:
- Wenn ein Befehl nicht gefunden wird, ist das Programm über diesen PowerShell-Aufruf nicht verfügbar.
- `docker info` fragt den Docker-Dienst ab; wenn Docker nicht läuft oder keine Berechtigung besteht, kann eine Fehlermeldung erscheinen. Dieser Befehl startet den Dienst nicht absichtlich.
- Gib nur die relevanten Fehlermeldungen aus, keine Zugangsdaten, Umgebungsvariablen oder privaten Konfigurationen.
- Ein erfolgreiches `docker --version` beweist nicht, dass der Docker-Dienst läuft. Eine erfolgreiche `docker info`-Rückgabe belegt nur die gemeldete Erreichbarkeit zu diesem Zeitpunkt.
- Erst nach Sichtung der Ergebnisse entscheiden wir, ob ein isolierter Test mit einer konkreten Datei sinnvoll ist. Keine pauschalen `docker run`, `compose up`, Installations- oder Administratorbefehle.

### F. Kompatibilität zwischen Modellen

- Keine herstellerspezifische Funktion voraussetzen. Ein Modell ohne Webzugriff kann den kopierten Lernblock auswerten, aber keine Live-GitHub-Prüfung behaupten.
- Ein Modell mit Webzugriff kann öffentliche Quellen lesen, hat dadurch aber nicht automatisch Zugriff auf private Repositories oder lokale Dateien.
- Ein Modell mit Terminal kann nur die Dateien, Programme und Rechte verwenden, die seine konkrete Laufzeit tatsächlich bereitstellt.
- Jedes Modell meldet seine eigenen Grenzen und Ergebnisse. Ein Modell darf die Ergebnisse eines anderen nicht als selbst ausgeführte Tests ausgeben.
- Ergebnisse verschiedener Modelle nur dann als unabhängig bewerten, wenn ihre Quellen und Prüfwege tatsächlich unabhängig waren.
- Bei abweichenden Antworten zuerst Commit, Dateiversion, Werkzeug, Zeitstempel und Prüfverfahren vergleichen.

