from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    data = requests.get('https://api.coinbase.com/v2/exchange-rates?currency=BTC').json()
    data = {"message": data["data"]["rates"]["BIT"]}
    return data