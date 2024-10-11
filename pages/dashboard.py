from streamlit_echarts import st_echarts
import streamlit as st
import pandas as pd
import json
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit.components.v1 import html

st.Page("pages/dashboard.py", title="Medical Insurance Dashboard")


# load data
def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                data = json.load(f)
                return pd.DataFrame(data)
            except json.JSONDecodeError:
                return pd.DataFrame()
    return pd.DataFrame()

def load_dash():
    st.set_page_config(
        page_title="Medical Insurance Dashboard",
        page_icon="🏥",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    file_path = "data.json"
    # file_path = "predicted_data.json"
    df = load_data(file_path)
    # df = pd.read_csv("/home/addo/dev/projects/mip/dumped_stuff/assets/insurance_new.csv")
    st.title("Insurance Prediction Dashboard")
    # Display data table
    st.subheader("Data Table")
    st.dataframe(df)
    col1, col2 = st.columns(2)
    # column = "charges"
    column = "predicted_amount"
    with col1:
        st.subheader("Frequency Distribution of Predicted Amounts")
        hist_values, bin_edges = np.histogram(df[column], bins=10)
        bin_labels = [
            f"${int(bin_edges[i])} - ${int(bin_edges[i+1])}"
            for i in range(len(bin_edges) - 1)
        ]
        hist_values_list = hist_values.tolist()
        advanced_chart_options = {
            "tooltip": {"trigger": "axis", "axisPointer": {"type": "shadow"}},
            "legend": {"data": ["Frequency", "Trend"], "top": "10%"},
            "xAxis": {
                "type": "category",
                "data": bin_labels,
                "axisLabel": {
                    "rotate": 45,
                },
            },
            "yAxis": {"type": "value", "name": "Frequency"},
            "series": [
                {
                    "name": "Frequency",
                    "type": "bar",
                    "data": hist_values_list,
                    "barWidth": "50%",
                    "itemStyle": {"color": "#6495ED"},
                },
                {
                    "name": "Trend",
                    "type": "line",
                    "data": hist_values_list,
                    "smooth": True,
                    "lineStyle": {"color": "#FF6347", "width": 2},
                    "markLine": {
                        "data": [{"type": "average", "name": "Avg"}],
                        "lineStyle": {"type": "dashed", "color": "#FF6347"},
                    },
                },
            ],
        }
        st_echarts(options=advanced_chart_options, height="500px")

    with col2:
        st.subheader("Average Predicted Amount by Age")
        age_group = df.groupby("age")[column].mean().reset_index()
        age_chart_options = {
            "xAxis": {
                "type": "category",
                "data": list(age_group["age"]),
            },
            "yAxis": {"type": "value"},
            "series": [
                {
                    "data": age_group[column].astype(float).tolist(),
                    "type": "line",
                    "smooth": True,
                    "color": "green",
                }
            ],
        }
        st_echarts(options=age_chart_options)
    with col2:
        st.subheader("Gender Distribution")
        gender_count = df["gender"].value_counts()
        gender_pie_options = {
            "series": [
                {
                    "name": "Gender",
                    "type": "pie",
                    "radius": "50%",
                    "data": [
                        {"value": int(gender_count["female"]), "name": "Female"},
                        {
                            "value": int(gender_count.get("male", 0)),
                            "name": "Male",
                        },  
                    ],
                    "label": {"formatter": "{b}: {d}%"},
                }
            ]
        }
        st_echarts(options=gender_pie_options)
    with col1:
        st.subheader("Predicted Amount by Region")
        region_group = df["region"].value_counts()
        region_pie_options = {
            "series": [
                {
                    "name": "Region",
                    "type": "pie",
                    "radius": "50%",
                    "data": [
                        {"value": int(region_group["africa"]), "name": "Africa"},
                        {"value": int(region_group.get("asia", 0)), "name": "Asia"},
                        {"value": int(region_group.get("europe", 0)), "name": "Europe"},
                        {
                            "value": int(region_group.get("northamerica", 0)),
                            "name": "North America",
                        },
                        {
                            "value": int(region_group.get("southamerica", 0)),
                            "name": "South America",
                        },
                        {
                            "value": int(region_group.get("australia", 0)),
                            "name": "Australia",
                        },
                    ],
                    "label": {"formatter": "{b}: {d}%"},
                    "emphasis": {"itemStyle": {"shadowBlur": 10, "shadowOffsetX": 0, "shadowColor": "rgba(0, 0, 0, 0.5)"}},
                }
            ]
        }
        st_echarts(options=region_pie_options)
    st.subheader("BMI vs Age")
    bmi_data = df["bmi"].round(0).tolist()
    bmi_vs_amount_options = {
        "xAxis": {
            "type": "category",
            "data": bmi_data,
            "axisLabel": {
                "rotate": 45,
            },
        },
        "yAxis": {"type": "value", "name": "Age"},
        "series": [
            {
                "data": df["age"].astype(int).tolist(),
                "type": "line",
                "smooth": True,
                "lineStyle": {
                    "color": "red",
                },
            }
        ],
        "tooltip": {
            "trigger": "axis",
        },
    }
    st_echarts(options=bmi_vs_amount_options)
    if st.button("Logout"):
        st.switch_page("streamlit_app.py")
        st.session_state["logged_in"] = False
        st.query_params.clear()

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.session_state["logged_in"]:
    load_dash()
else:
    st.switch_page("pages/login.py")
