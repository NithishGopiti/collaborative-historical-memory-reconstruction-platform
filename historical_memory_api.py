from fastapi import FastAPI

from historical_dependency_mapper import (
    validate_circular_dependency
)

app = FastAPI()

@app.get("/health")
def health():
    return {
        "status": "historical_platform_running"
    }

@app.get("/dependency-status")
def dependency_status():
    return {
        "dependency_graph_valid":
        validate_circular_dependency()
    }
