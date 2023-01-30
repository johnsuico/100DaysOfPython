import os, requests as req
from dotenv import load_dotenv
from datetime import datetime as dt

load_dotenv()

API_KEY = os.getenv('DAY38_API_KEY')
API_ID = os.getenv('DAY38_API_ID')
URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')

headers = {
    'x-app-id': API_ID,
    'x-app-key': API_KEY,
}

answer = input('What did you do today?: ')
today_date = dt.now().strftime("%d/%m/%Y")
now_time = dt.now().strftime("%X")

body = {
    'query': answer,
    'gender': 'male',
    'weight_kg': 77.11,
    'height_cm': 172.72
}

res = req.post(url=URL, headers=headers, json=body)
exercise_data = res.json()['exercises'][0]
exercise_activity = exercise_data['name'].capitalize()
exercise_duration = exercise_data['duration_min']
exercise_calories = exercise_data['nf_calories']
exercise_time = now_time

sheety_auth_headers = {
    'Authorization': 'Bearer secret_pass'
}

sheety_add_row = {
    'workout': {
        'date': today_date,
        'time': now_time,
        'exercise': exercise_activity,
        'duration': exercise_duration,
        'calories': exercise_calories
    }
}

res_sheety = req.post(url=SHEETY_ENDPOINT, json=sheety_add_row, headers=sheety_auth_headers)
print(res_sheety.json())