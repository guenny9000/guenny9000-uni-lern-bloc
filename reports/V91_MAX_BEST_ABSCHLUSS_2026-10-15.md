# V91 MAX-BEST Lernblock und Tagesabschluss — 2026-10-15

## Zweck
Dieser Block ist die gemeinsame Arbeitsgrundlage für lokale und externe Modelle. Er trennt bestätigte GitHub-Belege von Aussagen, die noch einen lokalen, unabhängigen oder produktiven Nachweis benötigen. Repositories dürfen getrennt bleiben; eine Zusammenführung ist kein Selbstzweck.

## Reality-First-Regeln
- Statusfolge: UNBEKANNT → DOKUMENTIERT → IMPLEMENTIERT → VERIFIZIERT → PRODUKTIV.
- CLAIM ≠ EVIDENCE. Keine erfundenen Messwerte, Erfolgsquoten, Lernfortschritte oder Echtzeit-Telemetrie.
- Ein erfolgreicher CI-Lauf bestätigt ausschließlich die ausgeführten Prüfungen auf dem zugehörigen Commit.
- Hash ≠ Signatur ≠ WORM ≠ Beweis für Wahrheit, Urheberschaft, Zeit oder Produktivbetrieb.
- Unbekanntes, nicht autorisiertes, netzwerkfähiges oder veränderndes Werkzeug standardmäßig blockieren (fail-closed).
- Erkennen ≠ Autorisieren. REQUEST ≠ AUTHORIZATION. Keine Privilegienausweitung.
- Daten erhalten: keine automatischen Resets, stillen Reparaturen, destruktiven Bereinigungen oder Produktionsänderungen.
- Verschiedene Repositories, Betriebssysteme, Sprachen und Implementierungen dürfen getrennt bestehen. Gemeinsame Schnittstellen und nachvollziehbare Belege sind wichtiger als ein erzwungener Monolith.
- GitHub speichert Dokumentation und Code, trainiert oder synchronisiert andere Modelle aber nicht automatisch.

## Live geprüfte Fakten am 2026-10-15

### 1. v91-core-system
Repository: https://github.com/guenny9000/v91-core-system

- PR #16 „Add isolated V91 Guardrail add-on for agent policy checks“ ist auffindbar: https://github.com/guenny9000/v91-core-system/pull/16
- Der Commit `26c0b34afc4eac32f690b3511e0a89e7bc8700ba` enthält den `GuardedToolRunner`-Code. Der Runner lässt nur explizit registrierte Werkzeuge zu und blockiert unbekannte, als Netzwerkzugriff/Änderung deklarierte oder nicht erlaubte Aktionen.
- GitHub Actions Lauf Nr. 167, Run-ID `38639183827`, wurde für diesen Commit als abgeschlossen und erfolgreich zurückgegeben. Job `audit-checks` meldet Erfolg bei Unit-Tests, Python-Kompilierung, Docker-Compose-Prüfung, Container-Integration mit Worker/Observer, Hash-Prüfung und Artefakt-Upload.
- Lauf ansehen: https://github.com/guenny9000/v91-core-system/actions/runs/38639183827
- Im abgefragten PR-Review-Endpunkt waren keine Reviews eingetragen.
- Korrektur zur älteren PR-Beschreibung: Dort steht noch, der CI-Lauf für den Runner-Commit sei nicht bestätigt. Der oben genannte Lauf liefert nun einen erfolgreichen Beleg für diesen Commit. Die PR-Beschreibung sollte bei Gelegenheit aktualisiert werden.
- Nicht belegt: Produktionsintegration, Betriebssystem-Sandbox, echtes Modelltraining, weltweite Telemetrie oder Ausführung auf dem lokalen Windows-PC.
- Wichtige technische Grenze: `read_only` ist eine Deklaration der registrierenden Host-Anwendung, keine Betriebssystem-Sandbox. Nur vertrauenswürdige Callables registrieren.

### 2. v91-audit-ledger
Repository: https://github.com/guenny9000/v91-audit-ledger (privat)

- Das aktuelle README beschreibt den Stand als Repository-Grundgerüst.
- Für diesen Durchgang ließ sich keine Implementierung unter dem erwarteten Pfad `ledger.py` abrufen. Daraus folgt nicht, dass keine Datei an anderer Stelle existiert.
- Ein echter Ledger-Dienst, Signaturprüfung, append-only Betrieb, WORM-Speicher und Produktionspipeline sind für diesen Durchgang NICHT VERIFIZIERT.
- Vor Implementierung: jede vorhandene Zeile, Sequenz, Verknüpfung und Prüfsumme prüfen; bei beschädigtem oder abgeschnittenem Verlauf fail-closed stoppen; vorhandene Daten niemals automatisch löschen oder still reparieren.
- Tests nur mit temporären Dateien und synthetischen Testdaten ausführen, niemals mit dem echten Nutzer-Ledger.

### 3. guenny9000-uni-lern-bloc
Repository: https://github.com/guenny9000/guenny9000-uni-lern-bloc

- Das README enthält bereits einen umfassenden Lernauftrag und eine Repository-Liste.
- PR #8 „Add final V91 MAX BEST learning handoff with repository links“ ist auffindbar: https://github.com/guenny9000/guenny9000-uni-lern-bloc/pull/8
- Weitere historische Lernblock-PRs sind auffindbar; ihr aktueller Merge- und CI-Zustand muss pro PR separat geprüft werden. Eine Suchliste allein bestätigt nicht, dass alle zusammengeführt oder alle Tests erfolgreich sind.
- Dieser Bericht ist eine additive Dokumentation. Er behauptet nicht, andere Modelle hätten den Block gelesen, übernommen oder daraus gelernt.

## Offene Punkte — keine falschen PASS-Meldungen
1. PR #16: erfolgreicher CI-Lauf für den genannten Commit ist belegt; Merge-Status und Produktionsfreigabe bleiben davon getrennt.
2. Andere offene Core-PRs dürfen nicht blind gemeinsam gemergt werden. Besonders bei gemeinsam veränderten Controllern, Audit-Workflows, Signaturformaten und Schlüsseln zuerst Konflikte, Abhängigkeiten, Migration und kombinierte Tests prüfen.
3. Für PRs #1, #3 und #5 liegen in den vorhandenen Beschreibungen konkrete Integrationsrisiken: Protokoll-/Signaturmigration, vertrauenswürdige Identitätsbindung/Schlüsselverwaltung und Überschneidungen gemeinsamer Workflows. Diese Risiken nicht durch einen erfolgreichen Einzel-Branch-CI-Lauf für erledigt erklären.
4. Lokale Hardware, Windows-Laufzeit, NVIDIA/CUDA-Messungen, externe WORM-Eigenschaften, Netzwerkisolation und reale Produktivdienste wurden hier nicht direkt getestet.
5. Globale Echtzeitdaten, ökologische Wirkungen, Modellübernahme und selbstständiges Modelltraining bleiben UNKNOWN, solange konkrete Quellen, Messungen und unabhängige Bestätigungen fehlen.

## Standard-Prüfablauf für jedes Modell
1. Repository, Standardbranch, Commit-SHA und Zugriffsstatus dokumentieren.
2. Alle PRs einzeln erfassen: offen/geschlossen/gemergt, Head-SHA, Basis-SHA, Review, Konflikte und CI für exakt den Head-Commit.
3. Quellcode, Abhängigkeiten, Workflow-Dateien, Tests und Dokumentation lesen; Dateinamen oder PR-Beschreibungen nicht als Implementierungsbeweis verwenden.
4. Änderungen zuerst isoliert und mit synthetischen Daten testen. Keine produktiven Geheimnisse, Nutzerdateien oder realen Ledger-Daten in Tests verwenden.
5. Bei gemeinsamer Dateiberührung eine Integrationsbranch erstellen und die ausgewählten Änderungen zusammen testen. Keine doppelten oder widersprüchlichen PRs blind zusammenführen.
6. Jeden Befund mit Pfad, Commit, Testbefehl, tatsächlichem Ergebnis und Zeitstempel belegen. Nicht ausgeführte Tests als NOT_RUN, fehlende Belege als UNKNOWN markieren.
7. Nur tatsächlich getestete, reversible und autorisierte Korrekturen durchführen. Bei Risiko, fehlender Berechtigung oder unklarer Migration stoppen und einen konkreten nächsten Schritt benennen.
8. Lernmaterialien als Dokumentation bereitstellen; niemals behaupten, dadurch seien andere Modelle automatisch trainiert oder synchronisiert worden.

## Abschlussstatus
- Verifiziert: GitHub Actions Lauf Nr. 167 für Commit `26c0b34afc4eac32f690b3511e0a89e7bc8700ba` erfolgreich.
- Implementiert im geprüften Commit: GuardedToolRunner als lokale, allowlist-basierte Ausführungsschleuse mit ausdrücklich begrenzten Sicherheitsgrenzen.
- Dokumentiert: Repository- und Beleggrenzen sowie sichere nächste Prüfschritte.
- UNKNOWN: Vollständige Prüfung sämtlicher PRs/Repositories, lokaler Windows-/Hardwarebetrieb, WORM, globale Telemetrie, Modelltraining und Produktionsintegration.

**Arbeitsregel für den Tagesabschluss:** Wenn keine weitere sichere und belegbare Prüfung möglich ist, offene Punkte sauber dokumentieren, keine unbelegten PASS-Status vergeben und den aktuellen Zustand erhalten.
