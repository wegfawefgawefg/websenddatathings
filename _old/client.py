# do request at http://localhost:5000/ and time how long it takes
import requests
import time
import requests


while True:
    now = time.time()
    response = requests.get("http://localhost:5000/")
    print(response.json())
    # print in milliseconds
    print((time.time() - now) * 1000)
