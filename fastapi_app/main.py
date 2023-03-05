from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def hello():
    # return {"message": "Pogoda zaebis!"}
    data = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m').json()
    # data = {"message": data["current_weather"]["windspeed"]}
    data = {"message": data["generationtime_ms"]}
    return data
