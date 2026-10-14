import json
import unittest
from pathlib import Path

from tools.validate_learning_contract import validate

CONTRACT_PATH = Path(__file__).resolve().parents[1] / "contracts" / "v91_learning_contract.json"


class LearningContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.contract = json.loads(CONTRACT_PATH.read_text(encoding="utf-8"))

    def test_current_contract_is_valid(self):
        self.assertEqual(validate(self.contract), [])

    def test_missing_safety_principle_is_rejected(self):
        changed = json.loads(json.dumps(self.contract))
        del changed["principles"]["claim_is_not_evidence"]
        self.assertTrue(any("claim_is_not_evidence" in item for item in validate(changed)))

    def test_false_safety_principle_is_rejected(self):
        changed = json.loads(json.dumps(self.contract))
        changed["principles"]["no_merge_without_explicit_authorization"] = False
        self.assertTrue(any("no_merge_without_explicit_authorization" in item for item in validate(changed)))

    def test_evidence_progression_cannot_be_reordered(self):
        changed = json.loads(json.dumps(self.contract))
        changed["evidence_states"] = list(reversed(changed["evidence_states"]))
        self.assertTrue(any("evidence progression" in item for item in validate(changed)))


if __name__ == "__main__":
    unittest.main()
