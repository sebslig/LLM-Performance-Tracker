import time
from dataclasses import dataclass
from typing import Dict, Any, Optional

@dataclass
class EvalResult:
    model_id: str
    prompt: str
    response: str
    latency_ms: float
    input_tokens: int
    output_tokens: int
    cost_usd: float
    accuracy_score: float = 0.0
    timestamp: float = field(default_factory=time.time)

@dataclass
class ModelConfig:
    name: str
    provider: str
    cost_per_1k_input: float
    cost_per_1k_output: float
    api_key_env: str
