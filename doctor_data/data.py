import random


with open(r"doctor_data\name.txt") as file:
    names = file.read().splitlines()


with open(r"doctor_data\doctor_type.txt") as file:
    doctor_types = file.read().splitlines()


doctor_list = {}

for doctor_type in doctor_types:

    num_doctors = random.randint(3, 9)
    doctors = []
    for _ in range(num_doctors):
        name = random.choice(names)
        rating = round(random.uniform(2, 5.0), 1)

        start_time = random.randint(8, 16)
        end_time = random.randint(17, 22)

        availability = [
            {"startTime": i, "endTime": i + 1} for i in range(start_time, end_time)
        ]
        doctor = {"name": name, "rating": rating, "availability": availability}
        doctors.append(doctor)
    doctor_list[doctor_type] = doctors


