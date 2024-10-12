import streamlit as st
import requests
header = """
<body>
<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  background-color: #f5f5f5;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 40px;
  border-bottom: 1px solid #e7edf3;
  color: #ffffff;
}

.logo-container {
  display: flex;
  align-items: center;
  gap: 15px;
}

.logo svg {
  width: 40px;
  height: 40px;
  color: #ffffff;
}

.logo h2 {
  font-size: 1.25rem;
  color: #d8d8d8;
  font-weight: bold;
}

.nav-links {
  display: flex;
  align-items: center;
  gap: 30px;
}

.menu {
  display: flex;
  align-items: center;
  gap: 20px;
}

.menu a {
  text-decoration: none;
  font-size: 0.95rem;
  color: #d8d8d8;
  font-weight: 500;
}

a {
  text-decoration: none;
  font-size: 0.95rem;
  color: #d8d8d8;
  font-weight: 500;
}
.cta button {
  padding: 8px 20px;
  background-color: #1980e6;
  color: #fff;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  font-size: 0.95rem;
  font-weight: bold;
}

.cta button:hover {
  background-color: #1466b0;
}

.avatar {
  width: 40px;
  height: 40px;
  background-size: cover;
  background-position: center;
  border-radius: 50%;
}

</style>
<header class="header">
  <div class="logo-container">
    <h2>Medical Insurance Predictor</h2>
  </div>
  <div class="nav-links">
    <div class="menu">
      <a href="/">Home</a>
      <a href="/about">About Us</a>
      <a href="mailto:oaddonay@gmail.com">Contact</a>
    </div>
    <div class="cta">
      <button><a href="/app2">Get Started</a></button>
    </div>
  </div>
</header>
</body>

"""
st.html(header)
html_page = """
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Medical Insurance Calculator</title>
    <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;700;800&family=Noto+Sans:wght@400;500;700;900&display=swap"
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
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }

        .flex-group {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        input[type="number"],
        select {
            width: 30%;
            padding: 0.75rem;
            border: 1px solid var(--border-color);
            border-radius: 0.5rem;
            background-color: transparent;
            color: var(--text-color);
            font-size: 1rem;
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
                            <input type="number" id="height" step="any" name="height" placeholder="Enter height " required>
                        </div>
                        <div class="form-item">
                            <label for="weight">Weight in Kg's</label>
                            <input type="number" step="any" id="weight" name="weight" placeholder="Enter weight" required>
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
                            <option value="retired">Retired</option>
                            <option value="part-time">Part-time</option>
                            <option value="consultant">Consultant</option>
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

</html>
"""
st.html(html_page)


if st.query_params == {}:
    st.session_state["data"] = None

else:
    st.session_state["data"] = st.query_params.to_dict()
    print(st.session_state["data"])
    st.switch_page("pages/success.py")
