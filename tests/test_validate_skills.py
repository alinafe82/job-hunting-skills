import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "validate_skills.py"
SPEC = importlib.util.spec_from_file_location("validate_skills", SCRIPT)
assert SPEC and SPEC.loader
validator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validator)


class ManifestValidationTests(unittest.TestCase):
    def validate(self, payload):
        with tempfile.TemporaryDirectory() as directory:
            manifest = Path(directory) / "manifest.json"
            manifest.write_text(json.dumps(payload), encoding="utf-8")
            original = validator.MANIFEST
            validator.MANIFEST = manifest
            try:
                errors = []
                validator.check_manifest([], errors)
                return errors
            finally:
                validator.MANIFEST = original

    def test_rejects_duplicate_skill_names(self):
        errors = self.validate(
            {
                "skills": [
                    {"name": "same", "summary": "a"},
                    {"name": "same", "summary": "b"},
                ]
            }
        )
        self.assertTrue(any("duplicate skill names: same" in error for error in errors))

    def test_rejects_non_object_skill_entries(self):
        errors = self.validate({"skills": ["not-an-object"]})
        self.assertTrue(any("skill entries must be objects" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
