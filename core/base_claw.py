import abc
import time
from core.models import EvalResult

class BaseOpenClawModel(abc.ABC):
    """Base interface for OpenClaw-compatible models."""
    
    def __init__(self, config):
        self.config = config

    @abc.abstractmethod
    def generate(self, prompt: str) -> str:
        pass

    def calculate_cost(self, in_tokens: int, out_tokens: int) -> float:
        in_cost = (in_tokens / 1000) * self.config.cost_per_1k_input
        out_cost = (out_tokens / 1000) * self.config.cost_per_1k_output
        return in_cost + out_cost

    def invoke(self, prompt: str) -> EvalResult:
        start_time = time.time()
        # Simulated token counting for standard interface
        # Actual implementation would use provider response
        response = self.generate(prompt)
        end_time = time.time()
        
        latency = (end_time - start_time) * 1000
        in_tokens = len(prompt.split()) * 1.3 # Rough approximation
        out_tokens = len(response.split()) * 1.3
        
        return EvalResult(
            model_id=self.config.name,
            prompt=prompt,
            response=response,
            latency_ms=latency,
            input_tokens=int(in_tokens),
            output_tokens=int(out_tokens),
            cost_usd=self.calculate_cost(in_tokens, out_tokens)
        )
