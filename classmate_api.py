
import requests

BASE_URL = "https://jasminerose-2.onrender.com"

endpoints = [
    "/",
    "/student",
    "/hello?name=Myranie",
    "/course",
    "/status"
]

print("===== CLASSMATE API ENDPOINT TEST =====")

for endpoint in endpoints:
    url = BASE_URL + endpoint

    try:
        response = requests.get(url, timeout=60)

        print("\nEndpoint:", endpoint)
        print("Status Code:", response.status_code)

        if response.status_code == 200:
            try:
                print("JSON Response:", response.json())
            except requests.exceptions.JSONDecodeError:
                print("Response:", response.text[:300])
        else:
            print("Response:", response.text[:150])

    except requests.RequestException as error:
        print("Connection error:", error)
