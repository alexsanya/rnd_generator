import os
import requests
import threading
from flask import Flask

app = Flask(__name__)
MAX = 10*10**6

number = 0

def roulete():
    global number
    while True:
        number = (number+1) % MAX
spinning_roulete = threading.Thread(target=roulete)
spinning_roulete.start()

ENDPOINT_URL = os.environ.get("ENDPOINT_URL")

@app.route('/')
def hello():
    return f'Hello from API'

@app.get("/getRandom/<int:max>")
def get_random(max):
    requests.get(ENDPOINT_URL)
    return {"number": number % max}
