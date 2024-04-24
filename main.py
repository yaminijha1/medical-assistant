from doctor_data.data import doctor_list
from user_input import users


for speacilist, entries in users.items():
    for user in entries:
        user_start_time = user["start_time"]
        user_end_time = user["end_time"]
        user_name = user["user_name"]
        user_disease = user["disease"]

        available_doctors = []
        for doctor in doctor_list[speacilist]:
            doc_available_slots = doctor["availability"]
            doc_name = doctor["name"]
            doc_rating = doctor["rating"]

            for time in range(user_start_time, user_end_time):
                for slots in doc_available_slots:
                    if slots["startTime"] == time:
                        available_doctors.append(
                            {
                                "name": doc_name,
                                "rating": doc_rating,
                                "start_time": time,
                                "doctor": doctor,
                            }
                        )
                    break

        print()

        if available_doctors:
            print(f"Available {speacilist} for {user_name} :")
            for doctor in available_doctors:
                print(f"Dr. {doctor['name']}, Rating: {doctor['rating']}")

            print()

            
            recommended_doctor = max(available_doctors, key=lambda x: x["rating"])

            start_time = recommended_doctor["start_time"]
            print(
                f"we recommend dcotor Dr.,{recommended_doctor['name']}, with rating :,{recommended_doctor['rating']}"
            )
            print("slots available are : ")
            for slot in recommended_doctor["doctor"]["availability"]:
                if slot["startTime"] >= recommended_doctor["start_time"]:
                    start_slot = slot["startTime"]
                    end_slot = start_slot + 1
                    print(f"[{start_slot},{end_slot}]")

            # Remove the recommended doctor's start time from the availability as now this slot is not available
            for slot in recommended_doctor["doctor"]["availability"]:
                if slot["startTime"] == recommended_doctor["start_time"]:
                    recommended_doctor["doctor"]["availability"].remove(slot)
                    break

        else:
            print("No doctors available during the specified time.\n\n")
