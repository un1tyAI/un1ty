import unittest
from src.hybr1d.input_orchestrator import InputOrchestrator

class TestInputOrchestrator(unittest.TestCase):
    def test_classify_input(self):
        orchestrator = InputOrchestrator(tokenizer, model)
        result = orchestrator.classify_input("Write a Python script.")
        self.assertEqual(result, "code_generation")

if __name__ == "__main__":
    unittest.main()