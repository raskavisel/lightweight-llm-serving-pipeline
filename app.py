from fastapi import FastAPI
import time

from model import generate_text
from metrics import log_inference, get_average_latency
from drift import is_drift_detected
from retrain import retrain_model

app = FastAPI()

@app.post("/generate")
def generate(prompt: str):
    start = time.time()
    response = generate_text(prompt)
    latency = log_inference(start)
    avg_latency = get_average_latency()

    if is_drift_detected(avg_latency):
        retrain_model()

    return {
        "response": response,
        "latency": latency,
        "avg_latency": avg_latency
  }
