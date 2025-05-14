from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from your API!"}

@app.get("/diagnostics")
def get_diagnostics(vehicle_id: str):
    return {
        "vehicle_id": vehicle_id,
        "status": "OK",
        "battery": "Good",
        "recommendations": ["Oil change", "Brake check"]
    }