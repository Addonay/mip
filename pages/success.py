import json
import os
import pickle
from pydantic import BaseModel
import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Success",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed",
)

everything: dict = st.session_state["data"]    
model = pickle.load(open("rf_model.pkl", "rb"))
weight = everything.get("weight")
height = everything.get("height")
bmi = float(weight) / (float(height) * float(height)) * 10000
def gg(value: str, category: str):
    mapping = {
        "gender": {"male": 1, "female": 0},
        "smoker": {"no": 0, "yes": 1},
        "history": {"no": 0, "yes": 1},
    }
    return mapping[category].get(
        value.lower(), -1
    )  
def one_hot_encode(inputs, bmi, label=False):
    region_categories = [
        "asia",
        "europe",
        "northamerica",
        "southamerica",
        "oceania",
        "africa",
        "antarctica",
    ]
    occupation_categories = [
        "salaried",
        "unemployed",
        "student",
        "business",
        "retired",
        "part-time",
        "consultant",
    ]
    region_encoded = [
        1 if everything.get("region") == cat else 0 for cat in region_categories
    ]
    occupation_encoded = [
        1 if everything.get("occupation") == cat else 0
        for cat in occupation_categories
    ]
    label_encoded_gender = gg(everything.get("gender"), "gender")
    label_encoded_smoker = gg(everything.get("smoker"), "smoker")
    label_encoded_hdhistory = gg(everything.get("heartDisease"), "history")
    feature_list = (
        [
            int(everything.get("age")),
            label_encoded_gender,
            float(bmi),
            int(everything.get("child_count")),
            label_encoded_smoker,
        ]
        + region_encoded
        + [label_encoded_hdhistory]
        + occupation_encoded
    )
    if label:
        return {
            "age": int(everything.get("age")),
            "gender": label_encoded_gender,
            "bmi": float(bmi),
            "child_count": int(everything.get("child_count")),
            "smoker": label_encoded_smoker,
            "region": region_encoded,
            "heart_disease_history": label_encoded_hdhistory,
            "occupation": occupation_encoded,
        }
    return feature_list
X = one_hot_encode(everything, bmi)
print(X)
print(everything)
salary = model.predict([X])
html(
    f"""
<head>
<link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet" />
<link href="https://fonts.googleapis.com/css2?family=Tillana:wght@400;500;600;700;800&display=swap" rel="stylesheet" />
</head>
<body class="bg-transparent font-sans">
<div class="container mx-auto mt-10 rounded-lg p-6">
    <div class="mb-4 flex animate-bounce items-center justify-center text-6xl text-green-500">💰</div>
    <div style="font-family: Tillana;" class="flex items-center justify-center rounded-lg text-3xl font-semibold text-green-600">The Estimated Insurance Amount is {" "} <strong class="text-4xl ml-3">   ${int(salary[0]):,} </strong></div>
    <div class="mt-8 text-left">
    <h3 class="text-3xl mt-24 font-bold text-gray-800">Insurance Charges Estimation Factors</h3>
    <p class="mt-4 text-xl text-gray-100">The estimated insurance charges are based on several factors. Here's how these factors generally affect your insurance charges:</p>
    <ul class="mt-4 text-lg list-disc pl-6 text-gray-300">
        <li><strong>Age:</strong> Typically, older individuals may have higher insurance charges.</li>
        <li><strong>BMI:</strong> A higher BMI often correlates with higher insurance charges.</li>
        <li><strong>Children:</strong> The number of children can affect your insurance charges.</li>
        <li><strong>Smoking:</strong> Smokers generally face higher insurance charges.</li>
        <li><strong>Region:</strong> Insurance charges can vary by region due to differences in healthcare costs.</li>
        <li><strong>Gender:</strong> In some cases, gender may influence insurance charges.</li>
    </ul>
    <p class="mt-4 text-xl text-gray-100">Remember, this is an estimation based on a predictive model and may not reflect actual charges from insurance providers.</p>
    </div>
</div>
</body>
    """,
    height=600,
)
st.html(
    f"""
    <head>
        <style>
            .button {{
                display: inline-block;
                padding: 15px 40px;
                color: #ffffff;
                background-color: #ffff;
                border-radius: 15px;
                text-decoration: none;
                transition: background-color 0.3s ease, transform 0.2s ease;
                margin-top: 5px;
            }}
            .button:hover {{
                background-color: #1565c0;
                transform: scale(1.05);
            }}
            .btn {{
                display: flex;
                align-items: center;
                justify-content: center;
                height: 10vh;
            }}
        </style>
    </head>
    <body>
        <div class="btn">
            <a href="/app2" class="button">Start Over</a>
        </div>
    </body>
    """
)
data_dict = everything
file_path = "data.json"
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        try:
            existing_data = json.load(f)
        except json.JSONDecodeError:
            existing_data = []
else:
    existing_data = []
predicted_amount = int(salary[0])
data_dict["predicted_amount"] = predicted_amount
data_dict["bmi"] = bmi
existing_data.append(data_dict)
with open(file_path, "w") as f:
    json.dump(existing_data, f, indent=4)
