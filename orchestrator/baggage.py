import requests
import os

API_EQUIPAJE_URL = os.getenv("API_EQUIPAJE_URL", "http://api_2:5002/e")

def create_equipment(equipment: dict):
    try:
        response = requests.post(API_EQUIPAJE_URL, json=equipment)
        if response.status_code == 201:
            return {"message": "equipment created", "data": response.json()}
        return {"error": "equipment wasn't created", "details": response.text}
    except Exception as e:
        return {"error": f"error: {e}"}

def get_equipment(id: str):
    try:
        response = requests.get(f"{API_EQUIPAJE_URL}/equipment/{id}")
        if response.status_code == 200:
            return response.json()
        return {"error": "equipment not found", "details": response.text}
    except Exception as e:
        return {"error": f"error: {e}"}
