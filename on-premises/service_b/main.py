from fastapi import FastAPI
import requests
import os

app = FastAPI()

CONSUL_URL = os.getenv("CONSUL_URL", "http://localhost:8500")

@app.get("/get-greeting")
def get_greeting():
    service_a_info = requests.get(f"{CONSUL_URL}/v1/catalog/service/service_a").json()
    if service_a_info:
        address = service_a_info[0]['ServiceAddress']
        port = service_a_info[0]['ServicePort']
        response = requests.get(f"http://{address}:{port}/greet")
        return response.json()
    return {"error": "Service A not found"}

@app.on_event("startup")
def register_with_consul():
    service_id = os.getenv("SERVICE_ID", "service_b")
    registration = {
        "ID": service_id,
        "Name": "service_b",
        "Address": os.getenv("SERVICE_HOST", "service_b"),
        "Port": int(os.getenv("SERVICE_PORT", 8002)),
        "Check": {
            "HTTP": f"http://{os.getenv('SERVICE_HOST', 'service_b')}:{os.getenv('SERVICE_PORT', 8002)}/get-greeting",
            "Interval": "10s"
        }
    }
    requests.put(f"{CONSUL_URL}/v1/agent/service/register", json=registration)