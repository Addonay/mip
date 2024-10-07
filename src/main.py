import pickle
import streamlit as st
from streamlit.components.v1 import html

model = pickle.load(open("rf_model.pkl", "rb"))

st.set_page_config(
    page_title="Medical Insurance Prediction",
    page_icon="🏥",
    layout="wide",
)

st.markdown(
    "<h1 style='text-align: center;'>Medical Insurance Prediction</h1>",
    unsafe_allow_html=True,
)
st.write("---")

gender = st.selectbox("Pick your Gender", ["Male", "Female"])
age = st.text_input("Enter your age", 0)
region = st.selectbox(
    "Where are you from?", ["SouthEast", "SouthWest", "NorthEast", "NorthWest"]
)
smoker = st.radio("Are you an active Smoker?", ["No", "Yes"])
children = st.slider("How many Children do you have", 0, 10)
bmi = st.text_input("Enter your Body Mass Index (BMI)")


col10, col11, col12, col13, col14 = st.columns(5)
with col10:
    st.write("")
with col11:
    st.write("")
with col12:
    predict_btn = st.button("Predict Amount")
with col13:
    st.write("")
with col14:
    st.write("")


def gg(value: str, category: str):
    mapping = {
        "gender": {"male": 0, "female": 1},
        "smoker": {"no": 0, "yes": 1},
        "region": {"northeast": 0, "southeast": 1, "northwest": 2, "southwest": 3},
    }
    return mapping[category].get(value.lower())


if predict_btn:
    try:
        inp1 = int(age)
        inp2 = gg(gender, "gender")
        inp3 = float(bmi)
        inp4 = int(children)
        inp5 = gg(smoker, "smoker")
        inp6 = gg(region, "region")

        if None in [inp2, inp5, inp6]:
            st.error("Invalid input detected. Please check your inputs.")
        else:
            X = [inp1, inp2, inp3, inp4, inp5, inp6]
            salary = model.predict([X])

            html_content = f"""
            <head>
                <link rel="preconnect" href="https://fonts.googleapis.com">
                <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
                <link href="https://fonts.googleapis.com/css2?family=Tillana:wght@400;500;600;700;800&display=swap" rel="stylesheet">
            </head>
            <body>
                <style>
                .prediction {{
                    font-family: "Tillana", sans-serif;
                    font-size: 24px;
                    color: #4CAF50;
                    text-align: center;
                    padding: 20px;
                    border-radius: 10px;
                }}
                </style>
                <div class="prediction">
                    The Estimated Insurance Amount is <strong>${int(salary[0]):,}</strong>
                </div>
            </body>
            """
            html(html_content, height=200)
    except ValueError:
        st.error("Please enter valid numeric values for age and BMI.")

