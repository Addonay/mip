import streamlit as st
from streamlit.components.v1 import html

st.set_page_config(
    page_title="Medical Insurance Predictor",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_page = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medical Insurance Predictor</title>
    <link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin>
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
        }


        body {
            font-family: Manrope, "Noto Sans", sans-serif;
            background-color: black;
            color: white;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            
        }

        .layout-container {
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #e7edf3;
        }

        .logo {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .logo svg {
            width: 1rem;
            height: 1rem;
        }

        nav {
            display: flex;
            gap: 2rem;
        }

        .get-started {
            background-color: #1980e6;
            color: white;
            border: none;
            border-radius: 0.75rem;
            padding: 0.5rem 1rem;
            font-size: 0.875rem;
            font-weight: 700;
            cursor: pointer;
        }

        main {
            padding: 1.25rem 10rem;
            display: flex;
            justify-content: center;
            flex-grow: 1;
        }

        .content {
            max-width: 960px;
            width: 100%;
        }

        .hero {
            background-image: linear-gradient(rgba(0, 0, 0, 0.1) 0%, rgba(0, 0, 0, 0.4) 100%), url("https://cdn.usegalileo.ai/sdxl10/020ce414-3617-4b30-97ec-f1f5c55cdc4a.png");
            background-size: cover;
            background-position: center;
            border-radius: 0.75rem;
            padding: 2.5rem;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            gap: 2rem;
            min-height: 480px;
        }

        .hero h1 {
            font-size: 3rem;
            font-weight: 900;
            line-height: 1.2;
        }

        .hero p {
            font-size: 1rem;
            max-width: 720px;
        }

        .search-container {
            display: flex;
            max-width: 480px;
            height: 4rem;
        }

        .search-icon {
            background-color: transparent;
            border: 1px solid #d0dbe7;
            border-right: none;
            border-radius: 0.75rem 0 0 0.75rem;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 0 1rem;
        }

        .search-icon svg {
            width: 1.25rem;
            height: 1.25rem;
            color: #4e7397;
        }

        input[type="text"] {
            flex-grow: 1;
            border: 1px solid #d0dbe7;
            border-left: none;
            background-color: transparent;
            border-right: none;
            padding: 0 0.5rem;
            font-size: 1rem;
            
        }
input[type="text"]:focus {
    outline: none; /* Ensures the outline is also removed */
}
                .btn {
            background-color: #fffff;
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
            color: var(--text-color);
        }

        .calculate-btn {
            background-color: #1980e6;
            color: white;
            border: none;
            border-radius: 0 0.75rem 0.75rem 0;
            padding: 0 1.25rem;
            font-size: 1rem;
            font-weight: 700;
            cursor: pointer;
        }

        .why-use {
            padding: 2.5rem 1rem;
        }

        .why-use h2 {
            font-size: 2.5rem;
            font-weight: 900;
            margin-bottom: 1rem;
            max-width: 720px;
        }

        .why-use p {
            font-size: 1rem;
            max-width: 720px;
            margin-bottom: 2.5rem;
        }

        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(158px, 1fr));
            gap: 0.75rem;
        }

        .feature {
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
        }

        .feature-img {
            aspect-ratio: 16 / 9;
            background-size: cover;
            background-position: center;
            border-radius: 0.75rem;
        }

        .feature p {
            font-size: 1rem;
            font-weight: 500;
        }

        .cta {
            text-align: center;
            padding: 5rem 2.5rem;
        }

        .cta h2 {
            font-size: 2.5rem;
            font-weight: 900;
            margin-bottom: 1rem;
        }

        .cta p {
            font-size: 1rem;
            margin-bottom: 2rem;
        }

                h2 {
            font-size: 2rem;
            margin-bottom: 1rem;
            text-align: center;
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
            text-decoration: #ffffff;
            font-weight: 500;
            transition: color 0.3s ease;
        }

        nav a:hover {
            color: var(--text-color);
        }
    </style>
</head>

<body>
    <div class="layout-container">
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
                    <li>
                    <button class="btn"> <a href="/app2">Get started</a></button>
                    
                    </li>
                </ul>
            </nav>
        </header>
        <main>
            <div class="content">
                <section class="hero">
                    <h1>Predict your medical insurance costs</h1>
                    <p>Get an estimate of your monthly health insurance premium based on your age, gender, location,
                        income, etc. No personal information required.</p>
                   
                </section>
                <section class="why-use">
                    <h2>Why use our tool?</h2>
                    <p>Our tool can help you get an estimate of your monthly health insurance premium based on your age,
                        gender, location, and income. We don't store any personal information and our tool is completely
                        free to use.</p>
                    <div class="features">
                        <div class="feature">
                            <div class="feature-img"
                                style="background-image: url('https://cdn.usegalileo.ai/stability/28b98442-6d6a-4216-a44b-1f0f629a908f.png');">
                            </div>
                            <p>Fast and easy</p>
                        </div>
                        <div class="feature">
                            <div class="feature-img"
                                style="background-image: url('https://cdn.usegalileo.ai/stability/8c9bd11e-c443-4198-9f0f-6e7c1611fe65.png');">
                            </div>
                            <p>No personal data</p>
                        </div>
                        <div class="feature">
                            <div class="feature-img"
                                style="background-image: url('https://cdn.usegalileo.ai/stability/636d623c-f0e0-45f4-9a0e-0db771b99f6b.png');">
                            </div>
                            <p>Free to use</p>
                        </div>
                    </div>
                </section>
                <section class="cta">
                    <h2>Try our Medical Insurance Predictor</h2>
                    <p>Get an estimate of your monthly health insurance premium based on your age, gender, location, and
                        income.</p>
                    <button class="btn"> <a href="/app2">Get started</a></button>
                </section>
            </div>
        </main>
    </div>

</body>

</html>
"""


st.html(html_page)
