import streamlit as st
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
            box-sizing: border-box;
        }

        body {
            font-family: Manrope, "Noto Sans", sans-serif;
            background-color: black;
            color: white;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
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
        border-bottom: 1px solid var(--border-color);
        padding: 1rem;
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
            padding: 2rem 1rem;
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
            padding: 2rem;
            display: flex;
            flex-direction: column;
            justify-content: flex-end;
            gap: 1.5rem;
            min-height: 450px;
        }

        .hero h1 {
            font-size: 2rem;
            font-weight: 900;
        }

        .hero p {
            font-size: 1rem;
            max-width: 720px;
        }

        .why-use {
            padding: 2rem 0;
        }

        .why-use h2 {
            font-size: 2rem;
            font-weight: 900;
            margin-bottom: 1rem;
            text-align: center;
        }

        .why-use p {
            font-size: 1rem;
            text-align: center;
            margin-bottom: 1.5rem;
        }

        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 1rem;
        }

        .feature {
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .feature-img {
            aspect-ratio: 16/9;
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
            padding: 3rem 0;
        }

        .cta h2 {
            font-size: 2rem;
            font-weight: 900;
            margin-bottom: 1rem;
        }

        .cta p {
            font-size: 1rem;
            margin-bottom: 1.5rem;
        }
              .small {
            display: none;
        }

        /* Responsiveness */
        @media (max-width: 768px) {
            header {
                flex-direction: row;
                gap: 0.5rem;
                align-items: center;
            }
            
            .logo h1 {
                display: none;
}
            .hero h1 {
                font-size: 1.75rem;
            }
                    .small {
            display: block;
            font-weight: 500;
            font-size: 1.2rem;
        }
        
        nav ul {
            flex-direction: row;
            align-items: flex-start;
            gap: 1rem;
            display: flex;
            align-items: center;
        }

            .hero p {
                font-size: 0.875rem;
            }

            .cta h2 {
                font-size: 1.75rem;
            }

            .cta p {
                font-size: 0.875rem;
            }

            main {
                padding: 1rem;
            }

            .content {
                padding: 1rem;
            }
        }

        @media (max-width: 480px) {
            .hero h1 {
                font-size: 1.5rem;
            }

            .hero p {
                font-size: 0.75rem;
            }

            .cta h2 {
                font-size: 1.5rem;
            }

            .cta p {
                font-size: 0.75rem;
            }
        }
    </style>
</head>

<body>
    <div class="layout-container">


        <main>
            <div class="content">
                <section class="hero">
                    <h1>Predict your medical insurance costs</h1>
                    <p>Get an estimate of your monthly health insurance premium based on your age, gender, location,
                        income, etc. No personal information required.</p>
                </section>

                <section class="why-use">
                    <h2>Why use our tool?</h2>
                    <p>Our tool provides an estimate of your monthly health insurance premium without requiring personal
                        data, and it's completely free.</p>

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
                    <p>Get an estimate of your monthly health insurance premium today.</p>
                    <button class="btn">Get started</button>
                </section>
            </div>
        </main>
    </div>
</body>
</html>
"""

st.html(html_page)
