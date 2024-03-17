import requests

inputs = {"total_day_minutes": 10.2,
    "total_day_calls":4,
    "num_customer_service_calls": 1}

resp = requests.post(
    "http://127.0.0.1:8000/churn",
    json = inputs)

print(resp.json())