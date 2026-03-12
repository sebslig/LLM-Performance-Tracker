from core.providers import MockClawModel
from core.models import ModelConfig
from core.storage import MetricsStore

def run_sample_eval():
    store = MetricsStore()
    
    configs = [
        ModelConfig("GPT-4o-Mock", "OpenAI", 0.01, 0.03, "OPENAI_API_KEY"),
        ModelConfig("Claude-3-Mock", "Anthropic", 0.015, 0.075, "ANTHROPIC_API_KEY")
    ]
    
    prompts = [
        "What is the capital of France?",
        "Explain quantum entanglement in 2 sentences.",
        "Write a python function to sort a list."
    ]
    
    print("Starting Benchmark...")
    
    for cfg in configs:
        model = MockClawModel(cfg)
        for p in prompts:
            print(f"Evaluating {cfg.name}...")
            res = model.invoke(p)
            store.save_result(res)
            
    print("Benchmark complete. Data stored in data/results.json")

if __name__ == "__main__":
    run_sample_eval()
