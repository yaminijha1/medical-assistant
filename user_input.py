# from disease_vs_doctor import symptom_specialist_map
import pandas as pd
from predictionAlgorithm import predict_speciality


# Input number of users
users = {}
# Input user data

user_name = input("Enter user name: ")


disease, doctor = predict_speciality()

# Input start and end time
print("Please note doctors are not available from 10 PM to 8 AM")
start_time, end_time = map(
    int,
    input(
        "Enter start time and end time in 24 hr format (Example: 8 12 for 8AM to 12PM): "
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
