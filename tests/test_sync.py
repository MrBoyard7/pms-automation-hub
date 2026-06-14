import unittest
from main import PMSAutomationHub

class TestPMSAutomation(unittest.TestCase):
    def setUp(self):
        # Initialize engine bypassing network calls where mockable
        self.hub = PMSAutomationHub()

    def test_properties_loaded(self):
        """Verify internal structural config map imports correctly."""
        self.assertTrue(len(self.hub.properties) > 0)
        self.assertIn("prop_001", self.hub.properties)

    def test_cleaning_template_assignment(self):
        """Validate metadata routing mapping engine configuration matches expectations."""
        studio_meta = self.hub.properties["prop_001"]
        self.assertEqual(studio_meta["cleaning_template"], "CLEANING_PROP_SMALL")

if __name__ == "__main__":
    unittest.main()