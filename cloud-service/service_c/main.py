from fastapi import FastAPI
import requests
import os

app = FastAPI()

@app.get("/greet")
def greet():
    return {"message": "Hello from Service C!"}

@app.on_event("startup")
def register_with_consul():
    consul_url = os.getenv("CONSUL_URL", "http://localhost:8500")
    service_id = os.getenv("SERVICE_ID", "service_c")
    registration = {
        "ID": service_id,
        "Name": "service_c",
        "Address": os.getenv("SERVICE_HOST", "service_c"),
        "Port": int(os.getenv("SERVICE_PORT", 9001)),
        "Check": {
            "HTTP": f"http://{os.getenv('SERVICE_HOST', 'service_c')}:{os.getenv('SERVICE_PORT', 8001)}/greet",
            "Interval": "10s"
        }
    }
    requests.put(f"{consul_url}/v1/agent/service/register", json=registration)