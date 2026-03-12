from core.base_claw import BaseOpenClawModel
import random

class MockClawModel(BaseOpenClawModel):
    """A mock implementation of OpenClaw for local testing."""
    
    def generate(self, prompt: str) -> str:
        # Simulate network latency
        import time
        time.sleep(random.uniform(0.2, 0.8))
        return f"Mock response for: {prompt[:20]}..."

class OpenAIClawModel(BaseOpenClawModel):
    """Wrapper for OpenAI via OpenClaw interface."""
    
    def generate(self, prompt: str) -> str:
        # In a real scenario, this uses the openai python client
        # with self.config.api_key_env
        return "Simulated OpenAI response"
