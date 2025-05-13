# flights.py
import requests
import os

API_VIAJE_URL = os.getenv("API_VIAJE_URL", "http://IP:5003/flight")

def create_flight(flight: dict):
    try:
        response = requests.post(f"{API_VIAJE_URL}flight", json=flight)
        if response.status_code == 201:
            return {"message": "flight created", "data": response.json()}
        return {"error": "flight wasn't created", "details": response.text}
    except Exception as e:
        return {"error": f"error: {e}"}

def get_flight_by_id(id_flight: int):
    try:
        response = requests.get(f"{API_VIAJE_URL}/{id_flight}")
        if response.status_code == 200:
            return response.json()
        return {"error": "flight not found", "details": response.text}
    except Exception as e:
        return {"error": f"error: {e}"}

def get_all_flights():
    try:
        response = requests.get(f"{API_VIAJE_URL}flight/all")
        if response.status_code == 200:
            return response.json()
        return {"error": "could not fetch flights", "details": response.text}
    except Exception as e:
        return {"error": f"error: {e}"}

def update_flight(id_flight: int, flight: dict):
    try:
        response = requests.put(f"{API_VIAJE_URL}flight/{id_flight}", json=flight)
        if response.status_code == 200:
            return response.json()
        return {"error": "could not update flight", "details": response.text}
    except Exception as e:
        return {"error": f"error: {e}"}

def delete_flight(id_flight: int):
    try:
        response = requests.delete(f"{API_VIAJE_URL}flight/{id_flight}")
        if response.status_code == 204:
            return {"message": "flight deleted successfully"}
        return {"error": "could not delete flight", "details": response.text}
    except Exception as e:
        return {"error": f"error: {e}"}
