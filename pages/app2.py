import json
import os
import pickle
import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Prediction",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed",
)
if st.query_params == {}:

    html_page = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Medical Insurance Calculator</title>
        <link
            href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&family=Noto+Sans:wght@400;500;700;900&display=swap"
            rel="stylesheet">
        <style>
            :root {
                --primary-color: #1980e6;
                --text-color: #ffffff;
                --border-color: #d0dbe7;
                --placeholder-color: #4e7397;
                --background-color: #000000;
            }

            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }

            body {
                font-family: 'Manrope', 'Noto Sans', sans-serif;
                background-color: var(--background-color);
                color: var(--text-color);
                line-height: 1.6;
                min-height: 100vh;
            }

            .container {
                margin: 0 auto;
                padding: 0 20px;
                display: flex;
                flex-direction: column;
                flex-grow: 1;
            }

            header {
                display: flex;
                justify-content: space-between;
                align-items: center;
                border-bottom: 1px solid var(--border-color);
            }

            .logo {
                display: flex;
                align-items: center;
                gap: 1rem;
            }

            .logo svg {
                width: 2rem;
                height: 2rem;
            }

            .logo h1 {
                font-size: 1.5rem;
                font-weight: 800;
            }

            nav ul {
                display: flex;
                gap: 2rem;
                list-style-type: none;
                align-items: center;
            }

            nav a {
                color: var(--text-color);
                text-decoration: none;
                font-weight: 500;
                transition: color 0.3s ease;
            }

            nav a:hover {
                color: var(--primary-color);
            }

            .btn {
                background-color: var(--primary-color);
                color: var(--text-color);
                padding: 0.75rem 1.5rem;
                border: none;
                border-radius: 0.5rem;
                font-weight: 700;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }

            .btn:hover {
                background-color: #1565c0;
            }

            main {
                padding: 2rem 0;
            }

            .calculator {
                max-width: 600px;
                margin: 0 auto;
                border-radius: 1rem;
                padding: 2rem;
            }

            h2 {
                font-size: 2rem;
                margin-bottom: 1rem;
                text-align: center;
            }

            .form-group {
                margin-bottom: 1.5rem;
                gap: 1rem;
            }

            .form-item {
                display: flex;
                flex-direction: column;
                width: 100%;
                /* Ensures both inputs take up equal space */
            }

            label {
                display: block;
                margin-bottom: 0.5rem;
                font-weight: 500;
            }

            .flex-group {
                display: flex;
                align-items: center;
                /* Align items vertically in the center */
                gap: 1rem;
                /* Space between elements */
            }

            input[type="number"],
            select {
                width: 30%;
                /* Set a width for each input and select */
                padding: 0.75rem;
                /* Consistent padding */
                border: 1px solid var(--border-color);
                border-radius: 0.5rem;
                background-color: transparent;
                color: var(--text-color);
                font-size: 1rem;
            }

            #height-inches {
                display: none;
                /* Initially hidden; will show via JavaScript */
            }



            input[type="text"],
            input[type="number"],
            select {
                width: 100%;
                padding: 0.75rem;
                border: 1px solid var(--border-color);
                border-radius: 0.5rem;
                background-color: transparent;
                color: var(--text-color);
                font-size: 1rem;
            }

            input[type="text"]::placeholder,
            input[type="number"]::placeholder,
            select::placeholder {
                color: var(--placeholder-color);
            }

            .radio-group {
                display: flex;
                gap: 1rem;
            }

            .radio-option {
                display: flex;
                align-items: center;
                gap: 0.5rem;
            }

            input[type="radio"] {
                appearance: none;
                width: 1.25rem;
                height: 1.25rem;
                border: 2px solid var(--border-color);
                border-radius: 50%;
                outline: none;
                cursor: pointer;
            }

            input[type="radio"]:checked {
                border-color: var(--primary-color);
                background-color: var(--primary-color);
                box-shadow: inset 0 0 0 3px var(--background-color);
            }

            .submit-btn {
                display: block;
                width: 50%;
                padding: 1rem;
                font-size: 1.1rem;
                margin-top: 1rem;
            }
            .sub {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100%;
                width: 100%;
            }
    footer {
        text-align: center;
        color: var(--text-color);
        font-size: 0.8rem;
        margin-bottom: 0.5rem;
        padding: 1rem 0;
    }
        </style>
    </head>

    <body>
        <div class="container">
            <header>
                <div class="logo">
                    <svg viewBox="0 0 48 48" fill="currentColor" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M44 11.2727C44 14.0109 39.8386 16.3957 33.69 17.6364C39.8386 18.877 44 21.2618 44 24C44 26.7382 39.8386 29.123 33.69 30.3636C39.8386 31.6043 44 33.9891 44 36.7273C44 40.7439 35.0457 44 24 44C12.9543 44 4 40.7439 4 36.7273C4 33.9891 8.16144 31.6043 14.31 30.3636C8.16144 29.123 4 26.7382 4 24C4 21.2618 8.16144 18.877 14.31 17.6364C8.16144 16.3957 4 14.0109 4 11.2727C4 7.25611 12.9543 4 24 4C35.0457 4 44 7.25611 44 11.2727Z">
                        </path>
                    </svg>
                    <h1>Medical Insurance Predictor</h1>
                </div>
                <nav>
                    <ul>
                        <li><a href="/">Home</a></li>
                        <li><a href="/app2">Calculator</a></li>
                        <li><button class="btn">Get Started</button></li>
                    </ul>
                </nav>
            </header>

            <main>
                <div class="calculator">
                    <h2>Predict Your Health Insurance Costs</h2>
                    <form id="insurance-form">
                        <div class="form-group">
                            <label for="age">Age</label>
                            <input type="number" id="age" name="age" placeholder="Enter age" required>
                        </div>

                        <div class="form-group">
                            <label>Gender</label>
                            <div class="radio-group">
                                <div class="radio-option">
                                    <input type="radio" id="female" name="gender" value="female" checked>
                                    <label for="female">Female</label>
                                </div>
                                <div class="radio-option">
                                    <input type="radio" id="male" name="gender" value="male">
                                    <label for="male">Male</label>
                                </div>
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="children">Number of children</label>
                            <input type="number" id="children" name="child_count" placeholder="Enter number of children" required>
                        </div>

                        <div class="form-group">
                            <label>Are you an Active Smoker?</label>
                            <div class="radio-group">
                                <div class="radio-option">
                                    <input type="radio" id="non-smoker" name="smoker" value="no" checked>
                                    <label for="non-smoker">No</label>
                                </div>
                                <div class="radio-option">
                                    <input type="radio" id="smoker" name="smoker" value="yes">
                                    <label for="smoker">Yes</label>
                                </div>
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="region">What region do you come from?</label>
                            <select id="region" name="region" required>
                                <option value="">Select region</option>
                                <option value="asia">Asia</option>
                                <option value="europe">Europe</option>
                                <option value="africa">Africa</option>
                                <option value="northamerica">North America</option>
                                <option value="southamerica">South America</option>
                                <option value="australia">Australia</option>
                            </select>
                        </div>

                        <div class="form-group flex-group">

                                <div class="form-item">
                                    <label for="height">Height in cm</label>
                                    <input type="number" id="height" step="any" name="height" placeholder="Enter height "
                                    required>
                                </div>
                                <div class="form-item">
                                    <label for="height">Weight in Kg's</label>
                                    <input type="number" step="any" id="weight" name="weight" placeholder="Enter weight"
                                    required>
                                </div>
                        </div>


                    

                        <div class="form-group">
                            <label>Do you have any Heart Disease History?</label>
                            <div class="radio-group">
                                <div class="radio-option">
                                    <input type="radio" id="no-heart-disease" name="heartDisease" value="no" checked>
                                    <label for="no-heart-disease">No</label>
                                </div>
                                <div class="radio-option">
                                    <input type="radio" id="heart-disease" name="heartDisease" value="yes">
                                    <label for="heart-disease">Yes</label>
                                </div>
                            </div>
                        </div>

                        <div class="form-group">
                            <label for="occupation">Occupation</label>
                            <select id="occupation" name="occupation" required>
                                <option value="">Select occupation</option>
                                <option value="student">Student</option>
                                <option value="salaried">Salaried</option>
                                <option value="business">Business</option>
                                <option value="unemployed">Unemployed</option>
                            </select>
                        </div>
    <div class="sub">
                        <button type="submit" class="btn submit-btn">Predict</button>
    </div>     
                    </form>
                </div>
            </main>
        </div>
        <footer>
            <p>&copy; 2024 Health Insurance Predictor. All rights reserved.</p>
        </footer>

    </body>

    </html>"""
    st.html(html_page)
else:

    model = pickle.load(open("rf_model.pkl", "rb"))
    everything = st.query_params.keys()
    default_keys = [
        "age",
        "gender",
        "child_count",
        "smoker",
        "region",
        "height",
        "weight",
        "heartDisease",
        "occupation",
    ]

    for key in default_keys:
        if key not in everything:
            st.error(f"Please enter {key}")
            st.stop()
            st.query_params.clear()
            st.rerun()

    weight = st.query_params.get("weight")
    height = st.query_params.get("height")

    bmi = float(weight) / (float(height) * float(height)) * 10000

    def gg(value: str, category: str):
        mapping = {
            "gender": {"male": 0, "female": 1},
            "smoker": {"no": 0, "yes": 1},
            "region": {
                "asia": 2,
                "europe": 3,
                "northamerica": 4,
                "southamerica": 6,
                "oceania": 5,
                "africa": 0,
                "antarctica": 1,
            },
            "history": {"no": 0, "yes": 1},
            "occupation": {"salaried": 1, "unemployed": 3, "student": 2, "business": 0},
        }
        return mapping[category].get(value.lower())

    inp1 = int(st.query_params.age)
    inp2 = gg(st.query_params.gender, "gender")
    inp3 = float(bmi)
    inp4 = int(st.query_params.child_count)
    inp5 = gg(st.query_params.smoker, "smoker")
    inp6 = gg(st.query_params.region, "region")
    inp7 = gg(st.query_params.occupation, "occupation")
    inp8 = gg(st.query_params.heartDisease, "history")

    X = [inp1, inp2, inp3, inp4, inp5, inp6, inp7, inp8]
    salary = model.predict([X])
    from streamlit.components.v1 import html

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

    data_dict = st.query_params.to_dict()

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
    data_dict["bmi"] = inp3

    existing_data.append(data_dict)

    with open(file_path, "w") as f:
        json.dump(existing_data, f, indent=4)
