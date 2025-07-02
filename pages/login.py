import streamlit as st


def display_login_ui():
    st.html(
        """
<head>
    <link href="https://fonts.googleapis.com/css2?family=Tillana:wght@400;500;600;700;800&display=swap" rel="stylesheet" />

</head>
<body>
<style>
body {
    font-family: 'Tillana', sans-serif;
    background-color: #1f2937; /* Dark background for contrast */
    color: #e5e7eb; /* Light gray text */
    margin: 0;
}

.container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-height: 50vh;
    padding: 3rem 1.5rem; /* Adjust padding for all screens */
}

.header {
    text-align: center;
    margin-bottom: 2.5rem; /* Space below header */
}

.logo {
    height: 4rem; /* Logo height */
    width: auto; /* Keep aspect ratio */
}

.title {
    margin-top: 2.5rem; /* Space above title */
    font-size: 2rem; /* Larger title font size */
    font-weight: bold; /* Bold text */
}

.form-container {
    margin-top: 0rem; /* Space above form container */
    max-width: 25rem; /* Limit form width */
    margin-left: auto;
    margin-right: auto;
}

.login-form {
    display: flex;
    flex-direction: column;
    gap: 2rem; /* Space between form elements */
}

.form-group {
    display: flex;
    flex-direction: column;
}

.label {
    font-size: 1.125rem; /* Larger text for labels */
    font-weight: 500; /* Medium weight */
    margin-bottom: 0.5rem; /* Space below label */
}

.input {
    padding: 0.5rem 0.75rem; /* Padding inside inputs */
    border: 1px solid #9ca3af; /* Light gray border */
    border-radius: 0.375rem; /* Rounded corners */
    background: transparent; /* Transparent background */
    color: #e5e7eb; /* Light gray text */
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1); /* Soft shadow */
    transition: border-color 0.2s ease; /* Transition effect */
    width: 100%; /* Ensure the input takes full width */
    min-width: 400px; /* Set a minimum width */
}

.input::placeholder {
    color: #a1a1aa; /* Gray placeholder text */
}

.input:focus {
    outline: none; /* Remove default outline */
    border-color: #6366f1; /* Indigo border on focus */
}

.submit-button {
    display: flex;
    justify-content: center;
    width: 100%;
    padding: 0.5rem 1rem; /* Padding for button */
    border-radius: 0.375rem; /* Rounded corners */
    background-color: #4338ca; /* Indigo background */
    color: white; /* White text */
    font-size: 1.125rem; /* Larger button text */
    font-weight: 600; /* Semi-bold */
    transition: background-color 0.2s ease; /* Transition effect */
}

.submit-button:hover {
    background-color: #3730a3; /* Darker indigo on hover */
}

@media (min-width: 640px) {
    .container {
        padding: 3rem; /* More padding for larger screens */
    }

    .title {
        font-size: 2.25rem; /* Increase title size */
    }

    .input {
        font-size: 1rem; /* Larger input text */
    }

    .submit-button {
        padding: 0.75rem 1.5rem; /* Larger button padding */
    }
}

</style>
    <div class="container">
        <div class="header">
            <img class="logo" src="https://tailwindui.com/plus/img/logos/mark.svg?color=indigo&shade=600" alt="Your Company">
            <h2 class="title">Sign in to your account</h2>
        </div>

        <div class="form-container">
            <form class="login-form" id="login-form">
                <div class="form-group">
                    <label for="email" class="label">Email address</label>
                    <input id="email" name="email" type="email" autocomplete="email" required class="input" />
                </div>

                <div class="form-group">
                    <label for="password" class="label">Password</label>
                    <input id="password" name="password" type="password" autocomplete="current-password" required class="input" />
                </div>

                <div>
                    <button type="submit" class="submit-button">Sign in</button>
                </div>
            </form>
        </div>
    </div>
</body>


    """
    )
print(st.query_params)

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if st.query_params == {}:
    st.session_state["logged_in"] = False
elif (
    st.query_params["email"] == "crazy@ss.bitch" or "admin@mail.com"
    and st.query_params["password"] == "admin"
):
    st.session_state["logged_in"] = True


if st.session_state["logged_in"]:
    print("logged in")
    st.switch_page("pages/dashboard.py")
else:
    display_login_ui()

