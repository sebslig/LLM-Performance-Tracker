import json
import os
from typing import List
from core.models import EvalResult

class MetricsStore:
    def __init__(self, file_path: str = "data/results.json"):
        self.file_path = file_path
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                json.dump([], f)

    def save_result(self, result: EvalResult):
        data = self.load_all()
        # Convert dataclass to dict
        res_dict = result.__dict__.copy()
        data.append(res_dict)
        with open(self.file_path, "w") as f:
            json.dump(data, f, indent=2)

    def load_all(self) -> List[dict]:
        with open(self.file_path, "r") as f:
            return json.load(f)
