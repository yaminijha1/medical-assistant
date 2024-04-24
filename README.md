# Medical Assistant

Submission for the Google Girls Hackathon 2024.

## Problem Statement

Medical Assistant: Develop a healthcare recommendation system that analyzes user symptoms leveraging symptom data (using mock data), healthcare provider databases, and user ratings, recommends doctors with matching specialties and aligned schedules

## Introduction

To address the challenge of efficiently connecting patients with the appropriate medical specialists, I have developed a
Python CLI application. This application utilizes a Random Forest classifier to predict potential diseases based on user-input symptoms. It then matches these diseases with corresponding specialists and filters available doctors by the patient's preferred appointment times and suggests the best-rated doctor to choose.

## Repro Steps

1. Clone the repository.

```
git clone https://github.com/yaminijha1/medical-assistant.git
```

2. Install the dependencies.

```
pip install -r requirements.txt
```

3. Run the `main.py` to access the application.

```
python main.py
```

## Supported Symptom Types

The list of supported symptoms for this application is given in the [symptoms.txt](assets\symptoms.txt). Please use symptoms from the list only.

## Screenshot

![Output Image](assets/output.jpeg)
