import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder


SYMPTOMS_LIST_FILENAME = "assets/symptoms.txt"
DISEASE_SPECIALIST_MAPPING_FILENAME = "assets/Doctor_Versus_Disease.csv"


model = joblib.load(r"assets/model.joblib")
disease_to_specialist_mapping = pd.read_csv(
    DISEASE_SPECIALIST_MAPPING_FILENAME, names=["Disease", "Specialist"]
)

label_encoder = LabelEncoder()
label_encoder.fit_transform(disease_to_specialist_mapping["Disease"])

with open(SYMPTOMS_LIST_FILENAME, "r") as f:
 
    test_col = [x[:-1] for x in f.readlines()]


def predict_speciality():
    """
    Use the trained Random Forest model to predict the disease
    from the given symptoms and predict the specialist type the
    user should visit
    """
    symptoms = []

    num_symptoms = int(input("Enter the number of symptoms you have: "))
    for i in range(1, 1 + num_symptoms):
        user_input = input(f"Enter Symptoms #{i}: ")
        symptoms.append(user_input)
    print()

    print("Symptoms you have:", symptoms)
    test_data = {}
    for column in test_col:
        test_data[column] = 1 if column in symptoms else 0
    test_df = pd.DataFrame(test_data, index=[0])
    predicted_disease = model.predict(test_df)
    predicted_disease = label_encoder.inverse_transform(predicted_disease).flat[0]
    specialist_type = disease_to_specialist_mapping[
        disease_to_specialist_mapping["Disease"] == predicted_disease
    ]["Specialist"].item()
    print("We have predicted that you should visit", specialist_type )
    print()
    return predicted_disease, specialist_type
