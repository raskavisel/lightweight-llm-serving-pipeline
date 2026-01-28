ji# Mini LLM Serving & Retraining Pipeline

**End-to-end lightweight pipeline for serving, monitoring and retraining open-source LLMs.**

## Overview

This project demonstrates a **production-inspired framework** for managing large language models (LLMs) in a compact and versatile setup. The system:

- Serves a **mini LLM** using FastAPI.
- Tracks **inference telemetry** including latency and request statistics.
- Detects **model drift** based on performance thresholds.
- Triggers **automated retraining** when drift is detected.
- Supports **model versioning** and reproducible experiments.

This is designed to emulate modern GenAI infrastructure practices and is fully compatible with Python environments, including Android (via Pydroid) and desktop platforms.

---

## Features

| Feature                         | Description |
|---------------------------------|-------------|
| **LLM Serving**                  | Handles text input and generates responses via a mini LLM simulation. |
| **Inference Metrics**            | Logs request count, latency and average latency. |
| **Drift Detection**              | Monitors performance degradation and triggers retraining. |
| **Automated Retraining**         | Simulates retraining workflow and version logging. |
| **Cross-Platform**               | Runs on mobile (Pydroid) and desktop Python environments. |

---

## Tech Stack

- **Python 3.13**
- **FastAPI** – REST API serving the model
- **Uvicorn** – ASGI server for running FastAPI
- **MLflow** – Model experiment tracking (simulated in mobile setup)
- **Standard Python libraries** – random, time

---
## **Installation & Setup**

### **1. Clone the repository**
```bash
git clone <your-github-repo-url>
cd mini-llm-serving-pipeline

2. Install dependencies

Bash
pip install -r requirements.txt
Note: On mobile (Pydroid), MLflow installation can be skipped due to Rust/build dependency limitations.
3. Start the API server

Bash
python -m uvicorn app:app --reload
4. Send a POST request to generate a response

Python
import requests

r = requests.post(
    "http://127.0.0.1:8000/generate",
    params={"prompt": "Hello from LLM"}
)
print(r.json())
Usage
The API endpoint /generate accepts a prompt string and returns:

Json
{
  "response": "Prompt: Hello from LLM\nResponse: This response demonstrates LLM serving behavior.",
  "latency": 0.0012,
  "avg_latency": 0.0012
}
When average latency exceeds the threshold, drift is detected, and retraining is triggered automatically.
Folder Structure


mini-llm-serving-pipeline/
│
├── app.py           # FastAPI server & API endpoints
├── model.py         # Mini LLM simulation
├── metrics.py       # Inference telemetry (latency & request logging)
├── drift.py         # Drift detection logic
├── retrain.py       # Simulated retraining workflow
├── requirements.txt # Python dependencies
└── README.md        # Project documentation
Future Enhancements
Integrate real LLMs (LLaMA, Alpaca, GPT-like models)
Add full MLflow tracking & model registry
Support multi-entity model storage
Implement token usage monitoring
Deploy on cloud infrastructure for production readiness
