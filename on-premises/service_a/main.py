from fastapi import FastAPI
import requests
import os

app = FastAPI()

@app.get("/greet")
def greet():
    return {"message": "Hello from Service A!"}

@app.on_event("startup")
def register_with_consul():
    consul_url = os.getenv("CONSUL_URL", "http://localhost:8500")
    service_id = os.getenv("SERVICE_ID", "service_a")
    registration = {
        "ID": service_id,
        "Name": "service_a",
        "Address": os.getenv("SERVICE_HOST", "service_a"),
        "Port": int(os.getenv("SERVICE_PORT", 8001)),
        "Check": {
            "HTTP": f"http://{os.getenv('SERVICE_HOST', 'service_a')}:{os.getenv('SERVICE_PORT', 8001)}/greet",
            "Interval": "10s"
        }
    }
    requests.put(f"{consul_url}/v1/agent/service/register", json=registration)