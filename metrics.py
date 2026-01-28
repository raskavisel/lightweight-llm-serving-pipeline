import time

stats = {
    "requests": 0,
    "total_latency": 0.0
}

def log_inference(start_time):
    latency = time.time() - start_time
    stats["requests"] += 1
    stats["total_latency"] += latency
    return latency

def get_average_latency():
    if stats["requests"] == 0:
        return 0
    return stats["total_latency"] / stats["requests"]
