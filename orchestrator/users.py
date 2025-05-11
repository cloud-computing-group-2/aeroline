# users.py
import requests
import os

API_USUARIOS_URL = os.getenv("API_USUARIOS_URL", "http://api_1:5001/user")

def create_user(user: dict):
    try:
        response = requests.post(API_USUARIOS_URL, json=user)
        if response.status_code == 201:
            return {"message": "user created", "data": response.json()}
        return {"error": "user not found", "details": response.text}
    except Exception as e:
        return {"error": f"error: {e}"}

def get_user(id: str):
    try:
        response = requests.get(f"{API_USUARIOS_URL}/{id}")
        if response.status_code == 200:
            return response.json()
        return {"error": "user not found", "details": response.text}
    except Exception as e:
        return {"error": f"error: {e}"}
