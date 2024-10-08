import requests
from datetime import datetime
import os


GENDER = "male"
WEIGHT_KG = 78
HEIGHT_CM = 183
AGE = 29

APP_ID = os.environ.get("DAY38_APP_ID")
API_KEY = os.environ.get("DAY38_API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/f3dc910f5d8ebfeed570d7c34881bd27/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")
# exercise_text = "Ran 5k and cycled for 20 minutes."

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"result: {result}")

today_date = datetime.today().strftime("%d/%m/%Y")
now_time = datetime.today().strftime("%H:%M:%S")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

#No Authentication
# sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)

#Basic Authentication
sheet_response = requests.post(
  sheet_endpoint,
  json=sheet_inputs,
  auth=(
      "anan",
      "helloWorld",
  )
)

print(sheet_response.text)

