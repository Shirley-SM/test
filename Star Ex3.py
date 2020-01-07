from flask import Flask
import threading
import time
import requests


counter = 1
app = Flask(__name__)

@app.route("/")
def hello():
    global counter
    counter += 1
    return str(counter)


if __name__ == "__main__":
    threading.Thread(target=app.run).start()
    time.sleep(0.5)
    response = requests.get('http://127.0.0.1:5000')
if response.status_code == 200:
    print('OK')
else:
    print('Error')
