# LLM Performance Tracker

A production-grade dashboard for evaluating Large Language Models (LLMs) across multiple providers (OpenAI, Anthropic, etc.) focusing on accuracy, latency, and cost.

This project utilizes the **OpenClaw** paradigm for standardized model interfacing.

## Features

- **Multi-Provider Support**: Track OpenAI, Anthropic, and local models via OpenClaw.
- **Metric Tracking**:
  - Accuracy: Semantic similarity and exact match.
  - Latency: Time to first token and total response time.
  - Cost: Per-token pricing calculations.
- **Dashboard**: Interactive data visualization of model performance.
- **Automated Benchmarking**: Run suites of prompts against multiple models simultaneously.

## Architecture

1. **Evaluator Core**: Python-based engine that sends prompts and collects telemetry.
2. **OpenClaw Wrapper**: Standardized interface for model interactions.
3. **Database**: SQLite/JSON backend for storing historical run data.
4. **API**: FastAPI backend to serve metrics.
5. **Frontend**: Streamlit-based dashboard for visualization.

## Installation

```bash
# Clone the repository
git clone https://github.com/username/llm-eval-dashboard.git
cd llm-eval-dashboard

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your API keys
```

## Usage

### 1. Run Benchmarks
Execute a prompt suite against configured models:
```bash
python scripts/run_benchmark.py --suite generic_tasks
```

### 2. Launch Dashboard
Visualize the results in your browser:
```bash
streamlit run app/dashboard.py
```

## Project Structure

- `core/`: Evaluation logic and metric calculations.
- `models/`: OpenClaw model definitions.
- `data/`: Local storage for benchmark results.
- `app/`: Streamlit dashboard code.
- `tests/`: Unit tests for evaluation logic.

## Contributing
Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## License
MIT
