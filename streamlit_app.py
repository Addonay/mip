import streamlit as st
from streamlit.components.v1 import html
from st_pages import get_nav_from_toml

st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
)


about_page = st.Page(
    page="pages/about.py",
    title="About",
    icon=":material/account_circle:",
)

dash_page = st.Page(
    page="pages/dashboard.py",
    title="Dashboard",
    icon=":material/bar_chart:",
)

calc_page = st.Page(
    page="pages/app2.py",
    title="Calculator",
    icon=":material/account_balance:",
)

success_page = st.Page(
    page="pages/success.py",
    title="Success",
    icon=":material/check_circle:",
)

login_page = st.Page(
    page="pages/login.py",
    title="Login",
    icon=":material/account_circle:",
)

home_page = st.Page(
    page="pages/home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)

pg = st.navigation(
    [home_page, about_page, login_page, dash_page, calc_page, success_page]
)
# st.logo("https://cdn.usegalileo.ai/sdxl10/101f5617-1def-49ab-9188-c2575daeb32f.png")
st.sidebar.text("Made with 💙 by Group 12")

pg.run()
# st.session_state["data"] = {}
st.session_state["logged_in"] = False
