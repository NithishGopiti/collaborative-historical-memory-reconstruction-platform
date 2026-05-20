import subprocess

services = [
    ["python", "initialize_historical_tables.py"],
    ["uvicorn", "historical_memory_api:app", "--host", "0.0.0.0", "--port", "8040"]
]

for service in services:
    subprocess.Popen(service)

input()
