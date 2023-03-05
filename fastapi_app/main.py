from fastapi import FastAPI
import requests
from jose import jwt

from shemas import User


app = FastAPI()

DB_user = {
    'login': 'johan',
    'password': '123'
}

@app.get("/")
async def hello():
    # return {"message": "Pogoda zaebis!"}
    data = requests.get('https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m').json()
    # data = {"message": data["current_weather"]["windspeed"]}
    data = {"message": data["generationtime_ms"]}
    return data


@app.post("/login")
async def login(user: User):
    login = user.login
    password = user.password
    if login == DB_user['login'] and password == DB_user['password']:
        token = jwt.encode(payload={'login': login}, key='SecRet', algorithm='HS256')
        return token
    return {"error": "not valid"}
