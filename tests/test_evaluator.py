import unittest
from llm_evals import Evaluator

class TestEvaluator(unittest.TestCase):
    def setUp(self):
        self.evaluator = Evaluator(model='test-model', dataset='test-dataset')

    def test_run_evaluation(self):
        results = self.evaluator.run_evaluation()
        self.assertIn('accuracy', results)
        self.assertIn('f1_score', results)
        self.assertIsInstance(results['accuracy'], float)
        self.assertIsInstance(results['f1_score'], float)

    def test_generate_report(self):
        results = {'accuracy': 0.95, 'f1_score': 0.93}
        try:
            self.evaluator.generate_report(results)
        except Exception as e:
            self.fail(f"generate_report raised an exception {e}")

if __name__ == '__main__':
    unittest.main()