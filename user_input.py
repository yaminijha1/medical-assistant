# from disease_vs_doctor import symptom_specialist_map
import pandas as pd
from predictionAlgorithm import predict_speciality


# Input number of users

users = {}

# Input user data


user_name = input("Enter user name: ")


disease, doctor = predict_speciality()

# Input start and end time
print("Please note doctor are not availble from 10 PM to 8 AM")
start_time, end_time = map(
    int,
    input(
        "Please Enter start time and end time in 24 hr format: \nExample 8 12   \n "
    ).split(),
)

# Store user data
if doctor not in users:
    users[doctor] = []
users[doctor].append(
    {
        "user_name": user_name,
        "disease": disease,
        "start_time": start_time,
        "end_time": end_time,
    }
)
