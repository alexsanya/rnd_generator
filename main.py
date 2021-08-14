import requests
import threading
from flask import Flask

app = Flask(__name__)

number = 0

def roulete():
    global number
    while True:
        number = (number+1) % MAX
spinning_roulete = threading.Thread(target=roulete)
spinning_roulete.start()

ENDPOINT_URL = os.environ.get("ENDPOINT_URL")

@app.route("/getRandom/{max:int}")
def get_random(max):
    requests.get(ENDPOINT_URL)
    return {"number": number}
