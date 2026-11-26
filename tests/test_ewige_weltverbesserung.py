"""Tests fuer den Lernblock V91 EWIGE WELTVERBESSERUNG (26.11.2026).

Pinnen nach dem Kodex-Muster (Core #533/#566/#595/#598): Doku
existiert und ist klein, Kernsaetze wortgenau (umbruch-normalisiert),
KEINE Umsetzungsbehauptung, Verweis-Ziele existieren,
Negativsonde gegen Endzustands- und Daemon-Claims.
LERNBLOCK != VERTRAG, PROZEDUR != VOLLZUG.
"""
from __future__ import annotations

import pathlib
import re
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]

DOC = ROOT / "learning-blocks" / "V91_EWIGE_WELTVERBESSERUNG_LERNBLOCK_2026-11-26.md"
KANON = ROOT / "MAX-BEST-AGATHON.md"
ECOLOGY = ROOT / "V91_MAX_BEST_LEARNING_AND_ECOLOGY.md"


def flat(text: str) -> str:
    """Umbruch- und Leerraum-normalisiert (Lektion #547)."""
    return re.sub(r"\s+", " ", text)


class EwigeWeltverbesserungLernblockTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.text = DOC.read_text(encoding="utf-8")
        cls.flat = flat(cls.text)

    def test_doc_exists_and_small(self):
        self.assertTrue(DOC.exists(), "Lernblock fehlt")
        self.assertLess(DOC.stat().st_size, 8 * 1024,
                        "Lernblock ueberschreitet die 8-KiB-Grenze")

    def test_status_markiert(self):
        self.assertIn("LERNBLOCK / DAUERPROTOKOLL", self.flat)
        self.assertIn("KEIN VERTRAG", self.flat)
        self.assertIn("KEINE NEUE BEFUGNIS", self.flat)

    def test_provenienz_direktive(self):
        self.assertIn("BETREIBER-DIREKTIVE 26.11.2026", self.flat)

    def test_reihenfolge_fuenf_schritte(self):
        for satz in (
            "Unnötige Verschwendung, technische Fehler, Abhängigkeiten und schädliche Strukturen reduzieren",
            "Versorgung, Energie, Wasser, Nahrung, Gesundheit, Wissen und Sicherheit stärken",
            "Menschenwürde, Selbstbestimmung",
            "unterstützen, nicht behindern",
            "Tatsächliche Verbesserungen messen und verbleibende Fehler offenlegen",
        ):
            self.assertIn(satz, self.flat, "Schritt fehlt: " + satz)

    def test_zyklus_ohne_endzustand(self):
        self.assertIn("KEINEN Endzustand", self.flat)
        self.assertIn("Dauerregeln + append-only-Zyklus", self.flat)

    def test_wiederholung_ehrlich_ohne_daemon_fiktion(self):
        self.assertIn("Standing-Freigabe vom 24.11.2026", self.flat)
        self.assertIn("24/7-Daemon existiert NICHT", self.flat)
        self.assertIn("SCRIPTED != RUNNING", self.flat)
        self.assertIn("WIEDERHOLUNG != DURCHGEFUEHRT", self.flat)

    def test_gemeinwohl_wortnah(self):
        for satz in (
            "duerfen NICHT ausgeschlossen werden",
            "werden respektiert",
            "technische Grundanforderungen",
            "Leistungsfähigkeit mit menschlichem Wert verwechseln",
            "Unterstützung statt Bevormundung",
            "Selbstbestimmung statt Zwang",
        ):
            self.assertIn(satz, self.flat, "Gemeinwohl-Satz fehlt: " + satz)

    def test_modelle_ergaenzen_sich(self):
        self.assertIn("ergänzen", self.flat)
        self.assertIn("OHNE andere Systeme unrechtmäßig zu blockieren",
                      self.flat)

    def test_epistemik_drei_ebenen(self):
        self.assertIn("VISION != UMSETZUNG != VERIFIZIERT", self.flat)
        self.assertIn("NICHT als erledigt ausgegeben", self.flat)

    def test_nicht_belegt_genannt(self):
        self.assertIn("NICHT_BELEGT", self.flat)
        self.assertIn("Messdaten #101/#103 fehlen", self.flat)

    def test_schaeden_sind_keine_erfolge(self):
        self.assertIn("SCHAEDEN und keine Erfolge", self.flat)

    def test_verweis_ziele_existieren(self):
        for pfad, name in ((KANON, "MAX-BEST-AGATHON"),
                           (ECOLOGY, "Learning and Ecology")):
            self.assertTrue(pfad.exists(), "Verweisziel fehlt: " + name)

    def test_negativsonde_keine_vollzugsbehauptung(self):
        self.assertNotIn("Welt gerettet", self.flat)
        self.assertNotIn("Endzustand erreicht", self.flat)
        self.assertNotIn("läuft dauerhaft im Hintergrund", self.flat)


if __name__ == "__main__":
    unittest.main()
