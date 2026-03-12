import unittest
from core.models import ModelConfig
from core.providers import MockClawModel

class TestEvalCore(unittest.TestCase):
    def setUp(self):
        self.config = ModelConfig("test-model", "test-prov", 0.01, 0.01, "KEY")
        self.model = MockClawModel(self.config)

    def test_cost_calculation(self):
        # 1000 in, 1000 out at 0.01 rate should be 0.02
        cost = self.model.calculate_cost(1000, 1000)
        self.assertAlmostEqual(cost, 0.02)

    def test_invoke_structure(self):
        result = self.model.invoke("Hello")
        self.assertEqual(result.model_id, "test-model")
        self.assertTrue(result.latency_ms > 0)
        self.assertIsNotNone(result.response)

if __name__ == "__main__":
    unittest.main()
