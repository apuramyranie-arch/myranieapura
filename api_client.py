
import requests

BASE_URL = "https://myranieapura.onrender.com"


def test_student():
    print("\n===== STUDENT ENDPOINT =====")

    try:
        response = requests.get(
            f"{BASE_URL}/student",
            timeout=60
        )

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            data = response.json()

            print("Student ID:", data["student_id"])
            print("Name:", data["name"])
            print("Program:", data["program"])
            print("Year:", data["year"])
            print("Section:", data["section"])
        else:
            print("Request failed:", response.text[:300])

    except (requests.RequestException, ValueError, KeyError) as error:
        print("Error:", error)


def test_hello():
    print("\n===== HELLO ENDPOINT =====")

    name = input("Enter your first name: ")

    try:
        response = requests.get(
            f"{BASE_URL}/hello",
            params={"name": name},
            timeout=60
        )

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            print(data["message"])
        else:
            print("Request failed:", response.text[:300])

    except (requests.RequestException, ValueError, KeyError) as error:
        print("Error:", error)


def test_course():
    print("\n===== COURSE ENDPOINT =====")

    try:
        response = requests.get(
            f"{BASE_URL}/course",
            timeout=60
        )

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            data = response.json()

            print("Course:", data["course"])
            print("Department:", data["department"])
            print("Year:", data["year"])
        else:
            print("Request failed:", response.text[:300])

    except (requests.RequestException, ValueError, KeyError) as error:
        print("Error:", error)


if __name__ == "__main__":
    test_student()
    test_hello()
    test_course()
