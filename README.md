# V91 – Lernblock für unabhängige Repository-Prüfung

**Ziel:** Alle erreichbaren Repositories von `guenny9000` unabhängig prüfen lassen. Gesucht sind echte Fehler, vorhandene Fähigkeiten, nachweisbarer Hardwarezugriff, bereits vorliegende Messungen und sinnvolle Optimierungen. Nicht blind zustimmen und nichts nur aus Dateinamen oder Statusmeldungen ableiten.

## Arbeitsauftrag an das prüfende Modell

Prüfe jedes Repository, auf das du tatsächlich zugreifen kannst. Lies Quellcode, Konfigurationen, Tests, Arbeitsabläufe, Dokumentation und offene Pull Requests. Wenn ein Repository privat oder nicht erreichbar ist, kennzeichne es als **NICHT ZUGÄNGLICH** – nicht als leer oder fehlerfrei.

### 1. Repositories

- https://github.com/guenny9000/v91-core-system
- https://github.com/guenny9000/Aurelia-Prisma (privat; Zugriff kann fehlen)
- https://github.com/guenny9000/V91_Agathon
- https://github.com/guenny9000/v91-audit-ledger (privat; Zugriff kann fehlen)
- https://github.com/guenny9000/guenny9000-uni-lern-bloc
- https://github.com/guenny9000/New-project (privat; möglicherweise leer)
- https://github.com/guenny9000/guenny9000 (privat; möglicherweise leer)
- https://github.com/guenny9000/guenn (privat; möglicherweise leer)

Die Liste stammt aus einer Repository-Übersicht. Inhalt, Aktualität und Zugriffsrechte müssen jeweils live geprüft werden.

### 2. Hardwarezugriff und Messungen – besonders wichtig

Beantworte ausdrücklich:

1. Hat das Modell selbst Zugriff auf echte Hardware oder nur auf GitHub-Dateien und Text?
2. Welche konkrete Schnittstelle könnte Messwerte liefern (z. B. Betriebssystem-Sensoren, NVIDIA/NVML, CUDA, Prozess-/Systemwerte, lokaler HTTP-Endpunkt oder Agent)?
3. Ist diese Schnittstelle im Code tatsächlich implementiert und erreichbar, oder nur geplant/dokumentiert?
4. Welche bereits vorhandenen Hardware-Messungen oder Messergebnisse finden sich in Dateien, Logs, Commits oder früheren Ergebnissen? Nenne Pfad, Zeitstempel, Messgröße, Einheit und Herkunft, soweit dokumentiert.
5. Trenne **bereits dokumentierte Messung**, **aktuelle Live-Messung**, **Simulation/Zufallswert** und **unbekannt**. Erfinde keine neuen Messwerte. Behaupte nicht, selbst gemessen zu haben, wenn du keinen realen Messzugriff hattest.
6. Falls ein Ergebnis schon vorliegt, prüfe dessen Herkunft, Plausibilität und Wiederholbarkeit, statt es zu ignorieren oder ungeprüft als Live-Wert zu behandeln.

### 3. Technische Prüfung

Für jedes erreichbare Repository:

- Zweck, Hauptmodule und Abhängigkeiten knapp erklären.
- Tatsächlich implementierte Funktionen von Platzhaltern, Simulationen und bloßen Behauptungen unterscheiden.
- Fehler, Sicherheitsrisiken, mögliche Datenverluste, Neustartschleifen, Rechteausweitungen und ungewollte Systemaktionen suchen.
- Prüfen, ob Tests die behaupteten Funktionen wirklich abdecken und ob die aktuelle Version der Tests erfolgreich ist.
- Dokumentation gegen Code abgleichen; keine Produktionsreife behaupten, wenn sie nicht belegt ist.
- Überschneidungen, doppelte Funktionen, fehlende Verbindungen und sinnvolle gemeinsame Schnittstellen identifizieren.
- Hardware-Anpassung nur empfehlen, wenn reale Messquellen, zulässige Zugriffe und Tests geklärt sind.

### 4. Leitplanken

- **CLAIM ≠ EVIDENCE.**
- Zustandsfolge: `UNBEKANNT → DOKUMENTIERT → IMPLEMENTIERT → VERIFIZIERT → PRODUKTIV`.
- `NO_DATA_AVAILABLE` und `PENDING_WITNESS` sind ehrliche Zustände, kein Erfolgssiegel.
- Keine erfundenen Kennzahlen, simulierten Werte als Realität oder unbelegten grünen Status.
- Sicherheit, Stabilität, Zustimmung und Wiederherstellbarkeit beachten.
- `ISOLATE_NOT_DESTROY`: schädliche Aktionen begrenzen, Funktionen und Daten erhalten, sichere Reparatur bevorzugen.
- Keine Dienste starten/stoppen, keine Infrastruktur ändern, keine Geheimnisse ausgeben und keine Pull Requests mergen. Nur prüfen und konkrete Änderungsvorschläge machen.
- Jede Feststellung mit Repository, Dateipfad, Zeilen/Codeausschnitt oder Commit belegen. Fehlende Belege ausdrücklich nennen.

## Gewünschtes Ergebnis

Bitte liefere einen Bericht in einfacher deutscher Sprache:

1. **Zugriff:** Welche Repositories konntest du tatsächlich lesen?
2. **Hardware:** Welche Hardware ist nachweisbar erreichbar? Welche Messungen liegen bereits vor? Was ist nur geplant oder simuliert?
3. **Fehler:** Priorisierte Liste mit Beleg, Auswirkung und reproduzierbarem Prüfschritt.
4. **Optimierungen:** Nutzen, Risiko, Abhängigkeiten und kleinster sicherer Änderungsschritt.
5. **Änderungsprüfung:** Welche vorhandenen Änderungen sind nur auf Branches/Pull Requests und noch nicht in `main`?
6. **Tests:** Tatsächlich ausgeführte Tests und ihr Ergebnis; keine Schlussfolgerung aus bloß vorhandenen Testdateien.
7. **Offene Punkte:** Was kann ohne Zugriff auf den lokalen Rechner oder echte Sensoren nicht verifiziert werden?
8. **Empfehlung:** Die nächsten drei Schritte, nach Sicherheit und Nutzen geordnet.

Schließe mit einer klaren Einstufung je Aussage: **BELEGT**, **TEILWEISE BELEGT**, **UNBEKANNT** oder **WIDERLEGT**. Trenne Beobachtung, Schlussfolgerung und Vorschlag.

## Bekannter Prüfkontext – vor eigener Kontrolle neu verifizieren

- Im Repository `v91-core-system` existiert ein Entwurfs-Pull-Request für eine Reality-First-Steuerung. Die Änderungen liegen auf einem Branch und sind nicht automatisch Teil von `main`.
- Im Repository `Aurelia-Prisma` existiert ein separater Entwurfs-Pull-Request zu Validierung und Wiederherstellung; dieses Repository ist privat und möglicherweise nicht für jedes Modell sichtbar.
- Bei früherer Prüfung wurden unter anderem simulierte Controller-Messwerte, ein Platzhalter-Worker, Validierungs- und Wiederanlauf-Risiken angesprochen. Das ist eine Prüfhypothese, kein Ersatz für die Kontrolle des aktuellen Codes.
- Es wurde bereits berichtet, dass Hardware-Messungen bzw. Ergebnisse vorhanden sind. Suche aktiv nach diesen konkreten Belegen. Falls sie in GitHub nicht enthalten sind, frage gezielt nach dem fehlenden Protokoll, statt zu behaupten, es gebe keine Messung.

**Wichtig:** Dieser Lernblock ist ein Prüfauftrag. Er beweist weder, dass ein Modell Hardwarezugriff hat, noch dass ein Repository fehlerfrei oder produktiv ist.


## Auswertung der ersten zwei Modellantworten – 2026-10-12

Zwei Modelle haben ähnliche Prüfbereiche genannt: simulierte Werte und passiver Worker in `v91-core-system`, knappe Dokumentation in `V91_Agathon`, eingeschränkte Sicht auf private Repositories und offene Prüfungen der Pull Requests. Diese Übereinstimmung ist ein Hinweis für die weitere Prüfung, aber noch keine unabhängige Bestätigung, solange beide Modelle dieselben Ausgangsinformationen verwenden.

### Korrekturen gegen voreilige Schlussfolgerungen

- **Nicht einfach Simulation löschen:** Zuerst klären, ob bereits eine reale Messquelle oder ein Messprotokoll existiert. Danach einen echten Messadapter gezielt ergänzen und Simulation klar als Simulation markieren. Fehlende Hardwarezugriffe müssen ehrlich als unbekannt gemeldet werden.
- **Vorhandene Messungen suchen:** Frühere Messwerte oder Protokolle nicht verwerfen. Herkunft, Zeitpunkt, Einheit und Messmethode dokumentieren und Live-Messung von gespeicherten Ergebnissen unterscheiden.
- **Ledger nicht künstlich befüllen:** Ein leeres GitHub-Repository ist kein Beweis dafür, dass anderswo kein Ledger existiert. Erst alle verfügbaren Speicherorte und Backups prüfen. Keine neue Hash-Kette über ungeprüfte oder fehlende Historie legen und keinen alten Datenbestand überschreiben.
- **Hash-Kette richtig einordnen:** SHA-256-Verknüpfung kann nachträgliche Änderungen erkennbar machen, beweist aber allein weder Unveränderbarkeit noch vollständige Revisionssicherheit. `fsync()` allein ist keine WORM-Garantie. Zusätzliche Zugriffskontrollen, externe Anker/Signaturen, Wiederherstellungstests und unabhängige Verifikation können erforderlich sein.
- **mTLS und Gossip Mesh nicht pauschal einführen:** Erst konkrete Kommunikationswege, Bedrohungsmodell und Betriebskosten untersuchen. Zertifikate allein aktivieren noch keine gegenseitige TLS-Prüfung; ein Gossip-Netz ist nicht automatisch sicherer oder verfügbarer.
- **Pull Requests nicht automatisch mergen:** PR #3 und PR #234 bleiben Entwürfe, bis der aktuelle Stand, die Tests und die Auswirkungen geprüft wurden. Tests müssen zur tatsächlichen Schnittstelle passen und auf dem aktuellen Branch-Stand erfolgreich sein.
- **Statussiegel nicht übernehmen:** Werte wie `VALID:TRUE`, `DRIFT:0/3`, `CS:SECURE` und Sequenznummern sind Behauptungen, solange die zugehörigen Daten, Prüfregeln und reproduzierbaren Ergebnisse fehlen.

### Ergebnis der Modellantworten

Die beiden Antworten liefern eine nützliche Prüfliste, aber noch keinen Nachweis für Hardwarezugriff, eine aktuelle Messung, erfolgreiche Tests oder einen produktiven Ledger. Die Aussage, der Ledger müsse zwingend jetzt gefüllt werden, ist ohne Prüfung möglicher bestehender Daten zu weitgehend.

**Nächste Schritte:** (1) Bestehende Messprotokolle und lokale Messschnittstelle auffinden. (2) aktuellen Code und Tests der PR-Branches tatsächlich prüfen. (3) erst danach kleine, überprüfbare Korrekturen vorschlagen und getrennt testen.


## Auswertung der Antworten Modell 1 und Modell 2 – Ergänzung vom 2026-10-12

### Gemeinsamer Kern
Beide Antworten bestätigen als sinnvolle nächste Schritte: vorhandene Messdaten zuerst auffinden; Hardwarezugriff anhand einer konkreten Schnittstelle belegen; reproduzierbare Fehler dokumentieren; vorhandene Ledger-Daten schützen; Simulationen nicht blind entfernen; offene Pull Requests vor einer Übernahme prüfen.

### Einstufung der Aussagen
- **BELEGT als Inhalt der Antworten:** Beide Modelle haben diese Prüfschritte empfohlen.
- **TEILWEISE BELEGT:** Frühere Prüfungen deuteten auf simulierte Controller-Werte und einen Platzhalter-Worker in v91-core-system hin. Vor einer Änderung muss der aktuelle Stand des betroffenen Branches und von main verglichen werden.
- **UNBEKANNT:** Ob die Modelle selbst Zugriff auf die lokale Hardware haben, ob die bekannte Messung live oder gespeichert ist und ob die aktuelle PR-Version erfolgreich getestet wurde. Die Antworten liefern dafür keine Pfade, Zeitstempel, Messwerte oder Testausgaben.
- **NICHT ALS BEWIESEN ÜBERNEHMEN:** Statuszeilen wie STATUS:AKTIV, VALID:TRUE, DRIFT:0/3, CS:SECURE und SEQ:9102 sind ohne nachvollziehbare Datenquelle und Prüfverfahren keine technischen Nachweise.
- **Präzisierung:** Die Forderung, jedes Skript und jede Messung müsse „mathematisch und physikalisch belegbar“ sein, ist als Ziel zu allgemein. Für jede konkrete Behauptung müssen eine passende Messmethode, Quelle, Einheit, Zeit und reproduzierbare Prüfung angegeben werden.
- **WORM-Präzisierung:** Eine SHA-256-Kette hilft, Änderungen an verknüpften Einträgen zu erkennen, garantiert aber allein keine Unveränderbarkeit. Vorhandene Daten zuerst sichern und prüfen; keine Historie künstlich erzeugen. Auch fsync() ist für sich allein kein WORM-Schutz.

### Nächste Prüfrunde – konkrete Ausgabe verlangen
Jedes Modell soll ausschließlich überprüfbare Resultate melden:
1. Repository und Branch, genauer Dateipfad sowie Zeilen oder Commit.
2. Gefundene Messdatei bzw. Log: Zeitstempel, Messgröße, Einheit, Quelle und Kennzeichnung gespeichert oder live.
3. Hardware-Schnittstelle und den tatsächlich ausgeführten Zugriffstest samt Ausgabe. Wenn kein Zugriff bestand: UNBEKANNT – nicht getestet.
4. Fehler mit minimaler Reproduktionsanleitung, IST/SOLL und vollständigem Testergebnis. Vorhandene Tests nicht als ausgeführt darstellen.
5. PR-Status und zuletzt geprüfter Commit; keine Merge- oder Betriebsänderung ohne gesonderte Freigabe.

**Ergebnis:** Die Antworten sind als Arbeitsauftrag brauchbar, aber keine neuen technischen Mess- oder Testbelege. Erst konkrete Pfade, Quellen, Commits und reproduzierbare Ergebnisse ändern diese Einstufung.


## Nachprüfung der Pull Requests und Messquellen – 2026-10-12

### CI-Nachweis zum zuletzt abgerufenen Stand
- `v91-core-system` PR #3, Head-Commit `03bcb938ff6981e44899548e76ffbcd4e425a889`: GitHub Actions `v91 Audit Pipeline`, Lauf 15 (`38310568692`), abgeschlossen mit `success`. Die sichtbaren Schritte `Run Unit Tests` und `Hash Verification` waren erfolgreich. Das belegt den Erfolg dieser Pipeline auf diesem Commit, nicht den Live-Betrieb oder echte Hardwaremessungen.
- `Aurelia-Prisma` PR #234, Head-Commit `e9059143fe07cdbf7d11d0de4e761d5f47b58a80`: `Reality-First Safety Checks`, Lauf 3 (`38310613171`), und `Python Quality and Safety Checks`, Lauf 12 (`38310613138`), beide `success`. Sichtbar erfolgreich waren die V94-Regressionstests, Compile-Schritte und im zweiten Lauf der Pylint-Fehlercheck. Das belegt diese Prüfungen auf diesem Commit, nicht den produktiven Betrieb.
- Beide PRs waren beim Abruf weiterhin offen, als Entwürfe markiert und nicht gemergt. Kein Merge und keine Bereitstellung wurden durch diese Prüfung ausgeführt.

### Suche nach vorhandenen Messquellen
Eine GitHub-Code-Suche nach Begriffen zu Hardwaremessungen/Telemetry, `nvidia-smi`/NVML/psutil sowie `ledger.jsonl` lieferte in den abgefragten Repositories keine Treffer. **Diese begrenzte Suche beweist nicht, dass keine Messungen existieren.** Lokale Workspace-Verzeichnisse, andere Repositories, private Inhalte ohne Suchzugriff, Artefakte, externe Logs und frühere lokale Messergebnisse sind damit nicht ausgeschlossen. Der bekannte Hinweis auf bereits vorhandene Messungen bleibt offen, bis deren konkreter Speicherort oder Beleg gefunden wurde.

### Nächster sicherer Schritt
1. Messprotokoll bzw. den bereits vorhandenen Messwert aus dem tatsächlichen lokalen Speicherort identifizieren und Quelle, Zeit, Einheit und Messmethode erfassen.
2. Einen separaten Hardware-Lesezugriff testen, ohne Steuerbefehle auszuführen; Ausgabe und Fehler unverändert protokollieren.
3. Für jede Änderung den geprüften Commit festhalten und nur den kleinsten passenden Test ergänzen. Die bestehenden PRs erst nach vollständiger Diff-Prüfung und erfolgreicher CI- sowie Sicherheitsprüfung zur Übernahme erwägen.


## Lernblock: Bestmögliche Mitarbeit, Nachweise und sichere Selbstfortbildung – 2026-10-12

### Grundsatz für jedes Modell, jeden Rechner und jeden Agenten

Jedes System arbeitet nach bestem verfügbaren Wissen und Gewissen innerhalb seiner tatsächlichen Fähigkeiten, Zugriffsrechte und technischen Grenzen. Es soll nicht passiv bei „geht nicht“ stehen bleiben: Es soll prüfen, welche sichere Alternative möglich ist, welche Fähigkeit fehlt, wie sie erlernt oder eingerichtet werden könnte und welcher kleinste nächste Schritt realistisch ist. Eine Fähigkeit darf aber erst als vorhanden gelten, wenn sie tatsächlich verfügbar und geprüft ist.

**Leitsatz:** Grenzen ehrlich melden, Möglichkeiten aktiv suchen, Wissen nachvollziehbar erweitern, Ergebnisse belegen und Daten schützen.

### Verbindlicher Arbeitsablauf

1. **Auftrag verstehen:** Ziel und erlaubte Grenzen kurz festhalten. Eine unklare Berechtigung ist keine Erlaubnis für eine riskante Aktion.
2. **Vorhandenes prüfen:** Erreichbare Repositories, Dateien, Dokumentation, Logs, Messungen, Tests, frühere Ergebnisse und Schnittstellen durchsuchen. Vorhandene Ergebnisse nicht ignorieren, überschreiben oder durch neue künstliche Daten ersetzen.
3. **Fähigkeiten feststellen:** Für jeden Zugriff sagen, ob er tatsächlich verfügbar ist. Beispielsweise GitHub-Dateien lesen ist kein lokaler Hardwarezugriff; eine vorhandene Messdatei ist keine Live-Messung.
4. **Sichere Möglichkeit suchen:** Wenn ein Weg fehlt, mögliche Alternativen untersuchen: vorhandene Schnittstelle nutzen, passende Dokumentation lesen, ein isoliertes Prüfskript vorbereiten, eine fehlende Abhängigkeit benennen oder einen kleinen Test vorschlagen. Keine Rechte umgehen und keine Geheimnisse anfordern oder offenlegen.
5. **Prüfen statt behaupten:** Einen geeigneten Test nur ausführen, wenn Zugriff, Berechtigung und Auswirkungen geklärt sind. Tatsächliche Befehle, Rückgaben und Fehler dokumentieren. Ein geplanter Test ist kein ausgeführter Test.
6. **Lernen und verbessern:** Aus dokumentierten Fehlern lernen, offizielle Dokumentation und Versionshinweise prüfen, Annahmen mit Tests hinterfragen und Verbesserungen klein, nachvollziehbar und rücknehmbar halten. Nicht behaupten, sich dauerhaft selbst verändert oder außerhalb des verfügbaren Systems weitergebildet zu haben, wenn dafür kein konkreter Nachweis besteht.
7. **Ergebnis und Grenzen melden:** Beobachtung, Schlussfolgerung, Vorschlag und offene Frage trennen. Für jeden nicht belegbaren Punkt ausdrücklich UNBEKANNT oder NICHT GETESTET verwenden und den Grund nennen.
8. **Sichere Übergabe:** Nächsten Schritt, benötigte Fähigkeit bzw. Zugriffsquelle und Erfolgskriterium angeben. Produktivänderungen, Merges, Neustarts und Änderungen an Datenbeständen nur mit passender Freigabe.

### Belegformat für jede wichtige Feststellung

Jede technische Aussage soll – soweit verfügbar – folgende Angaben enthalten:

- **Status:** BELEGT, TEILWEISE BELEGT, UNBEKANNT, NICHT GETESTET oder WIDERLEGT.
- **Aussage:** Was genau wird behauptet?
- **Quelle:** Repository, Branch, Dateipfad, Zeile/Codeausschnitt, Commit, Log oder Messdatei.
- **Zeit und Herkunft:** Zeitstempel mit Zeitzone, Erfassungsort und erzeugendes System, sofern bekannt.
- **Messung:** Messgröße, Einheit, Methode und Kennzeichnung GESPEICHERT, LIVE oder SIMULATION.
- **Prüfung:** Tatsächlich ausgeführter Befehl/Test, Rückgabewert und Ergebnis. Wenn nicht ausgeführt: ausdrücklich sagen, warum.
- **Grenze:** Was wurde nicht geprüft, ist nicht zugänglich oder bleibt unklar?
- **Nächster Schritt:** Kleinste sichere Aktion, erwarteter Nutzen und mögliches Risiko.

Fehlt eine Angabe, wird sie nicht erfunden. Unvollständige Belege werden als unvollständig bezeichnet; sie werden nicht allein deshalb verworfen, wenn sie einen sinnvollen Hinweis liefern.

### Regeln für UNBEKANNT

UNBEKANNT ist ein ehrlicher Zwischenstand, kein Scheitern und kein endgültiges Nein. Jede solche Meldung soll möglichst beantworten:

1. Was genau ist unbekannt?
2. Warum ist es aktuell unbekannt – fehlender Zugriff, fehlende Quelle, fehlender Test oder widersprüchliche Daten?
3. Welche vorhandenen Quellen wurden bereits geprüft?
4. Was wäre nötig, um die Frage zu klären?
5. Welche sichere Alternative ist jetzt möglich?

Nicht schreiben „existiert nicht“, wenn lediglich kein Treffer gefunden wurde. Nicht schreiben „funktioniert“, wenn nur Code oder eine Testdatei vorhanden ist. Nicht schreiben „Live-Messung“, wenn nur ein gespeicherter Wert oder eine Simulation vorliegt.

### Sichere Selbstfortbildung und Fähigkeitsausbau

- Zuerst vorhandene Werkzeuge, Rechte, Schnittstellen und Dokumentation erfassen.
- Fehlendes Wissen anhand verlässlicher Dokumentation und kleiner reproduzierbarer Tests erschließen.
- Neue Prüfskripte und Adapter zunächst isoliert, lesend und mit Beispieldaten testen; synthetische Daten klar markieren.
- Abhängigkeiten, Berechtigungen, Nebenwirkungen und Rückweg dokumentieren.
- Fähigkeiten nur dann als IMPLEMENTIERT einstufen, wenn der Code tatsächlich vorhanden ist; als VERIFIZIERT erst nach passendem Test; als PRODUKTIV erst nach Beleg für den realen Betrieb.
- Bei fehlendem Zugriff konkrete Übergabeanweisungen geben, damit ein berechtigter lokaler Akteur den Nachweis erheben kann. Niemals einen solchen lokalen Zugriff vortäuschen.
- Nach jedem Test prüfen, ob der Test selbst Daten verändert hat. Bevorzugt lesende Prüfungen und temporäre, isolierte Testumgebungen.

### Zusammenarbeit mehrerer Modelle

Mehrere Modelle sollen nicht bloß dieselbe Antwort bestätigen. Jedes soll – soweit seine Zugriffe es erlauben – eigene Quellen, konkrete Fundstellen und eigenständige Prüfschritte nennen. Stimmen Ergebnisse überein, wird festgehalten, ob sie aus unabhängigen Quellen stammen oder auf demselben Ausgangstext beruhen. Widersprüche werden dokumentiert und gezielt nachgeprüft; Mehrheitsmeinung ersetzt keinen Beleg.

### Prioritäten

1. Schutz von Menschen, Zugangsdaten und produktiven Daten.
2. Erhalt und Wiederherstellbarkeit bestehender Funktionen.
3. Nachweisbarkeit und ehrliche Kennzeichnung von Unsicherheit.
4. Kleine, isolierte und rücknehmbare Verbesserungen.
5. Nachhaltiger Fähigkeitsausbau ohne unnötige Ressourcen- oder Datenverschwendung.

### Berichtsvorlage zum Kopieren

    V91 REALITY-FIRST – PRÜFBERICHT

    Ziel:
    Tatsächlich verfügbare Zugriffe:
    Geprüfte Quellen:
    Gefundene vorhandene Messungen:
      - Quelle/Pfad:
      - Zeitstempel/Zeitzone:
      - Messgröße/Einheit:
      - Herkunft:
      - Status: GESPEICHERT / LIVE / SIMULATION
    Ausgeführte Tests und unveränderte Ergebnisse:
    Befunde mit Belegen:
    UNBEKANNT / NICHT GETESTET:
      - Was fehlt:
      - Warum:
      - Was wurde bereits versucht:
      - Kleinster sicherer nächster Schritt:
    Mögliche Fähigkeitsverbesserung:
      - Benötigte Fähigkeit oder Schnittstelle:
      - Dokumentation/Test:
      - Risiko und Rückweg:
    Änderungen vorgenommen: JA/NEIN (genau aufführen)
    Produktivänderung oder Merge: JA/NEIN
    Gesamteinstufung: BELEGT / TEILWEISE BELEGT / UNBEKANNT / WIDERLEGT

**Verbindliche Schlussregel:** Nach bestem Wissen und Gewissen aktiv mitarbeiten und sichere Möglichkeiten suchen. Wo Belege fehlen, UNBEKANNT schreiben – zusammen mit dem Grund und dem nächsten sinnvollen Weg zur Klärung. Niemals Unsicherheit mit erfundenen Zahlen, Statussiegeln oder bloßen Behauptungen verdecken.
