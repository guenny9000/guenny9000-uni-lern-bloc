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
- [ ] Vor automatischer Wiederherstellung, Dienstneustarts oder sonstigen Änderungen an laufenden Systemen prüfen: ausdrückliche Autorisierung, betroffene Dienste, Auslösebedingungen, Begrenzung der Versuche, Protokollierung, anschließende Gesundheitsprüfung und Rückweg. Ein vorhandener Schalter oder ein erfolgreicher Skript-Exitcode ersetzt diese Prüfung nicht.
- [ ] Keine automatische Zusammenführung, Bereitstellung oder produktive Änderung aus dieser Checkliste ableiten.

## 5. Ledger und Audit prüfen

- [ ] Vorhandene Ledger-Datei und Verifikationsfunktion anhand des tatsächlichen Repository- oder lokalen Dateipfads identifizieren.
- [ ] Prüfen, was `verify_chain()` wirklich validiert: Reihenfolge, Vorgänger-Hashes, berechnete Hashes, Pflichtfelder und gegebenenfalls Zeitstempel.
- [ ] Prüfbefehl, Codeversion, Eingabedatei, unveränderte Ausgabe und Exit-Code festhalten.
- [ ] Ein Tagesbericht darf vorhandene Daten ergänzen, aber keine fehlenden Ereignisse rückdatieren oder erfinden.
- [ ] SHA-256 und `fsync()` allein machen einen Speicher nicht unveränderbar. Für einen WORM-Nachweis braucht es zusätzlich eine tatsächlich durchgesetzte Schreib-/Löschsperre oder unveränderbare Speicherung sowie einen unabhängig prüfbaren Nachweis.
- [ ] Einen Bericht nicht ungeprüft in ein WORM-Ledger schreiben. Erst Schema, Berechtigung, Append-Verfahren und Auswirkungen prüfen; bevorzugt zunächst einen getrennten Bericht außerhalb des Ledgers erstellen.
- [ ] Keine Ledger-Historie überschreiben, zurücksetzen oder neu versiegeln, um einen Test grün erscheinen zu lassen.

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


## Laufender Reality-First-Umsetzungsbericht – 2026-10-14

**Arbeitsumfang:** Reale Fehler korrigiert und in getrennten Review-Branches dokumentiert. Keine Änderungen direkt in `main` übernommen; keine Pull Requests gemergt; kein Zugriff auf den Windows-PC des Nutzers und keine Live-Steueraktion auf dessen Rechner ausgeführt.

### 1. v91-core-system – PR #10

- PR: https://github.com/guenny9000/v91-core-system/pull/10
- Geprüfter Commit: `6c16d753a1644523e6962093c07fcdb4b6218af7`
- CI: https://github.com/guenny9000/v91-core-system/actions/runs/38585438842 — **success**
- Tatsächlich bestandene Schritte: Compose-Konfiguration, Unit-Tests, Python-Kompilierung, Container-Build, Container-Integrationstest, Hash-Artefakte.
- Geändert: passiver Worker-Platzhalter ersetzt; echte Offline-Warteschlangenaufgaben für Status, SHA-256 und SHA-256-Vergleich; Pflichtfelder `purpose` und `expected_effect`; Audit-Ereignis vor der Ausführung; echte Warteschlangenbeobachtung; Größen- und Pfadgrenzen; read-only Arbeitsbereich; internes Docker-Netz ohne externe Route; Windows-Hilfsskript für Beispielaufgabe; Host-Steuerung nur mit ausdrücklicher Freigabe und begrenzter Worker-Skalierung.
- Integrationstest belegt die konkrete Datei-Hash-Aufgabe im CI-Container. Er belegt nicht den Betrieb auf dem lokalen Windows-PC.
- Offen: Host-Steuerung wurde hier nicht live ausgeführt; JSONL ist kein WORM und nicht signiert; anwendungsbezogene Fehler-/Latenzmessung und Produktivbetrieb sind nicht nachgewiesen.

### 2. V91_Agathon – PR #2

- PR: https://github.com/guenny9000/V91_Agathon/pull/2
- Geprüfter Commit: `2ed7e14b5eecdc3514bd7ca545f349b18f153e8e`
- CI: https://github.com/guenny9000/V91_Agathon/actions/runs/38586188548 — **success**
- Tatsächlich bestandene Schritte: Paketinstallation, Quell-/Test-Kompilierung, Tests und Paketmetadaten.
- Behobene Mismatches: Hash-Chain-Logger fehlte trotz Testimport; AuditDeep fehlte Chain-Verifikation und vollständige Ed25519-Schnittstelle; `__init__.py` importierte nicht vorhandene Komponenten; `core.py` enthielt ungültigen Python-Text; Packaging verwies auf einen Platzhalterpaketnamen; README zeigte auf ein fehlendes Beispiel.
- Explizit nicht implementiert: Semgrep-Scan/Policy-Erzeugung, Multi-Node-Lifecycle, persistente Schlüsselverwaltung, Hardware-Telemetrie und produktiver Ledger.

### 3. v91-audit-ledger – PR #2

- PR: https://github.com/guenny9000/v91-audit-ledger/pull/2
- Geprüfter Commit: `a023df6bc2e9d08697d0d56238a3ab6d47297ab8`
- CI: https://github.com/guenny9000/v91-audit-ledger/actions/runs/38586397764 — **success**
- Implementiert: lokale JSONL-Hash-Kette, Sequenz-/Vorgängerprüfung, Verifikation vor Append, fail-closed bei beschädigten Daten, Lock-Konflikten und Symlinks; Tests verwenden temporäre Dateien.
- Grenzen: Hash-Kette allein ist weder WORM noch Beweis für Wahrheit, Identität oder vertrauenswürdige Zeit. Keine Netzwerkdienste und kein Produktivbetrieb.

### 4. Aurelia-Prisma – PR #234

- PR: https://github.com/guenny9000/Aurelia-Prisma/pull/234
- Aktueller geprüfter Head-Commit: `c81c64a373c5d8b293dc758121ad4b8c02c7f658`
- CI: https://github.com/guenny9000/Aurelia-Prisma/actions/runs/38587522550 und https://github.com/guenny9000/Aurelia-Prisma/actions/runs/38587522735 — beide **success** auf diesem Head.
- Zusätzlich korrigiert: Das vorherige Restart-Skript enthielt weiterhin `-ExecutionPolicy Bypass`, beendete beliebige Prozesse auf Zielports mit Force und startete V94 auf `0.0.0.0`, obwohl die PR-Dokumentation etwas anderes behauptete. Das Skript ist jetzt auf explizites Opt-in begrenzt, prüft Prozessidentität, lässt fremde Listener unangetastet, dokumentiert Grund und erwarteten Effekt, bindet die drei Dienste an Loopback, prüft Health-Endpunkte und versucht eine begrenzte Rückkehr zur vorherigen Dienstmenge.
- Der globale Starthelfer bindet V91/Flowise lokal, lädt keine fehlenden Images automatisch herunter und behauptet keine implementierte Autoskalierung mehr.
- **Nicht getestet:** PowerShell-Skript wurde nicht auf Windows ausgeführt; die CI prüft die Python-Logik, kompiliert die Python-Module, baut das V94-Image und prüft Sicherheitsinvarianten statisch. Keine Dienste wurden gestartet oder neu gestartet.

### 5. Repository-Zugriff und Status

- `v91-core-system`, `V91_Agathon`, `v91-audit-ledger` und `guenny9000-uni-lern-bloc` waren über die verbundenen GitHub-Werkzeuge lesbar.
- `Aurelia-Prisma` war über die verbundene GitHub-Sitzung lesbar, obwohl das Repository privat ist.
- Weitere erreichbare Repositories wurden in der Repository-Liste gesehen; sie wurden in dieser Runde nicht vollständig inhaltlich geprüft. Für `Aurelia-Prisma` wurde hier der relevante PR-Diff geprüft, nicht der gesamte Repository-Bestand.
- Die hier aufgeführten Änderungen liegen auf Review-Branches/Pull Requests. **Keine davon ist durch diesen Bericht als in `main` übernommen zu verstehen.**

### Gesamtstatus nach Reality-First

- **BELEGT:** Die genannten GitHub-CI-Läufe meldeten Erfolg auf den genannten Commits.
- **BELEGT:** Die drei neuen PRs sind getrennt und offen; die ursprünglichen Default-Branches wurden nicht direkt geändert.
- **TEILWEISE BELEGT:** Die Kern-Container können in CI reale lokale Aufgaben verarbeiten und protokollieren.
- **UNBEKANNT:** Ob dieselben Stände auf dem Windows-PC des Nutzers laufen, wie dort Ressourcenwerte aussehen und ob die lokale Docker-Umgebung korrekt konfiguriert ist.
- **NICHT PRODUKTIV VERIFIZIERT:** Hardwarezugriff, lokale Modelle, allgemeines autonomes Handeln, dauerhafte/extern verankerte Audit-Unveränderbarkeit und anwendungsbezogene Leistungsverbesserung.

**Nächster sinnvoller Schritt:** PR-Diffs und CI-Ausgaben prüfen, dann die offenen PRs einzeln bewusst übernehmen. Anschließend den lokalen Windows-Start mit unveränderten Logs und konkreter Task-Ausgabe prüfen. Eine lokale Live-Messung darf erst nach tatsächlichem Zugriff behauptet werden.


### Korrektur zur GitHub-Historie – 2026-10-14

Eine neue statische Regressionstest-Datei wurde versehentlich einmal direkt auf dem Default-Branch von `Aurelia-Prisma` angelegt. Der Fehler wurde unmittelbar korrigiert: Die Datei wurde wieder entfernt und ausschließlich auf dem Review-Branch neu angelegt. Aktuell ist `tests/test_v95_restart_script_safety.py` auf `main` nicht vorhanden; die Git-Historie enthält den Additions-Commit und den anschließenden Revert-Commit. Es wurden keine Laufzeitdateien, Daten oder Dienste verändert. Diese Abweichung von der vorgesehenen PR-only-Arbeitsweise wird ausdrücklich dokumentiert statt verschwiegen.
