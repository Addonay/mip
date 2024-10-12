import streamlit as st
from streamlit.components.v1 import html


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
<html>
  <head>
    <link rel="preconnect" href="https://fonts.gstatic.com/" crossorigin="" />
    <link
      rel="stylesheet"
      as="style"
      onload="this.rel='stylesheet'"
      href="https://fonts.googleapis.com/css2?display=swap&amp;family=Manrope%3Awght%40400%3B500%3B700%3B800&amp;family=Noto+Sans%3Awght%40400%3B500%3B700%3B900"
    />

    <title>Galileo Design</title>
    <link rel="icon" type="image/x-icon" href="data:image/x-icon;base64," />

    <script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
  </head>
  <body>
    <div class="relative flex size-full min-h-screen flex-col bg-[#0e1117] group/design-root overflow-x-hidden" style='font-family: Manrope, "Noto Sans", sans-serif;'>
      <div class="layout-container flex h-full grow flex-col">

        <div class="px-40 flex flex-1 justify-center py-5">
          <div class="layout-content-container flex flex-col max-w-[960px] flex-1">
            <div class="@container">
              <div class="@[480px]:p-4">
                <div
                  class="flex min-h-[480px] flex-col gap-6 bg-cover bg-center bg-no-repeat @[480px]:gap-8 @[480px]:rounded-xl items-center justify-center p-4"
                  style='background-image: linear-gradient(rgba(0, 0, 0, 0.1) 0%, rgba(0, 0, 0, 0.4) 100%), url("https://cdn.usegalileo.ai/sdxl10/f7e87ec4-8281-497d-8489-7065f10ebe5d.png");'
                >
                  <div class="flex flex-col gap-2 text-center">
                    <h1
                      class="text-white text-4xl font-black leading-tight tracking-[-0.033em] @[480px]:text-5xl @[480px]:font-black @[480px]:leading-tight @[480px]:tracking-[-0.033em]"
                    >
                      Understand your health and financial future
                    </h1>
                    <h2 class="text-white text-sm font-normal leading-normal @[480px]:text-base @[480px]:font-normal @[480px]:leading-normal">
                      Our predictive modeling helps you make informed decisions about health and wellness by estimating future medical insurance charges based on your health data
                      and lifestyle choices.
                    </h2>
                  </div>
                 
                </div>
              </div>
            </div>
            <div class="flex flex-col gap-10 px-4 py-10 @container">
              <div class="flex flex-col gap-4">
                <h1
                  class="text-[#d8d8d8] tracking-light text-[32px] font-bold leading-tight @[480px]:text-4xl @[480px]:font-black @[480px]:leading-tight @[480px]:tracking-[-0.033em] max-w-[720px]"
                >
                  How it works
                </h1>
                <p class="text-[#d8d8d8] text-base font-normal leading-normal max-w-[720px]">
                  Our app uses predictive modeling to estimate your future healthcare costs based on your health data and lifestyle choices. We analyze a variety of factors,
                  including your age, gender, location, and health history, as well as your diet, exercise habits, and other lifestyle choices. Our predictive model estimates your
                  future healthcare costs based on these factors, so you can make informed decisions about your health and finances.
                </p>
              </div>
              <div class="grid grid-cols-[repeat(auto-fit,minmax(158px,1fr))] gap-3">
                <div class="flex flex-col gap-3 pb-3">
                  <div
                    class="w-full bg-center bg-no-repeat aspect-video bg-cover rounded-xl"
                    style='background-image: url("https://cdn.usegalileo.ai/sdxl10/9cf3409b-b82e-4370-abf3-8808cbab86bd.png");'
                  ></div>
                  <div>
                    <p class="text-[#d8d8d8] text-base font-medium leading-normal">Estimate future healthcare costs</p>
                    <p class="text-[#4e7397] text-sm font-normal leading-normal">
                      Our predictive model estimates how much you'll spend on medical care in the next year based on your current health data and lifestyle choices.
                    </p>
                  </div>
                </div>
                <div class="flex flex-col gap-3 pb-3">
                  <div
                    class="w-full bg-center bg-no-repeat aspect-video bg-cover rounded-xl"
                    style='background-image: url("https://cdn.usegalileo.ai/stability/c4c0033d-9272-4935-8a5a-5987c10b9c8a.png");'
                  ></div>
                  <div>
                    <p class="text-[#d8d8d8] text-base font-medium leading-normal">Understand the financial impact of your health choices</p>
                    <p class="text-[#4e7397] text-sm font-normal leading-normal">
                      We help you understand how your health and wellness choices can impact your future medical costs, so you can make informed decisions about your health and
                      finances.
                    </p>
                  </div>
                </div>
                <div class="flex flex-col gap-3 pb-3">
                  <div
                    class="w-full bg-center bg-no-repeat aspect-video bg-cover rounded-xl"
                    style='background-image: url("https://cdn.usegalileo.ai/sdxl10/6162e54b-4e89-42f8-8430-83c5c81175ad.png");'
                  ></div>
                  <div>
                    <p class="text-[#d8d8d8] text-base font-medium leading-normal">Get personalized recommendations for improving your health</p>
                    <p class="text-[#4e7397] text-sm font-normal leading-normal">
                      Our app uses your health data and lifestyle choices to provide personalized recommendations for improving your health and reducing your future medical costs.
                    </p>
                  </div>
                </div>
              </div>
            </div>
            <h2 class="text-[#d8d8d8] text-[22px] font-bold leading-tight tracking-[-0.015em] px-4 pb-3 pt-5">Why HealthView</h2>
            <div class="grid grid-cols-[repeat(auto-fit,minmax(158px,1fr))] gap-3 p-4">
              <div class="flex flex-1 gap-3 rounded-lg border border-[#d0dbe7] p-4 flex-col">
                <div class="text-[#d8d8d8]" data-icon="ShieldCheck" data-size="24px" data-weight="regular">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                    <path
                      d="M208,40H48A16,16,0,0,0,32,56v58.78c0,89.61,75.82,119.34,91,124.39a15.53,15.53,0,0,0,10,0c15.2-5.05,91-34.78,91-124.39V56A16,16,0,0,0,208,40Zm0,74.79c0,78.42-66.35,104.62-80,109.18-13.53-4.51-80-30.69-80-109.18V56H208ZM82.34,141.66a8,8,0,0,1,11.32-11.32L112,148.68l50.34-50.34a8,8,0,0,1,11.32,11.32l-56,56a8,8,0,0,1-11.32,0Z"
                    ></path>
                  </svg>
                </div>
                <div class="flex flex-col gap-1">
                  <h2 class="text-[#d8d8d8] text-base font-bold leading-tight">Understand your health and financial future</h2>
                  <p class="text-[#4e7397] text-sm font-normal leading-normal">
                    Our predictive modeling helps you make informed decisions about health and wellness by estimating future medical insurance charges based on your health data and
                    lifestyle choices.
                  </p>
                </div>
              </div>
              <div class="flex flex-1 gap-3 rounded-lg border border-[#d0dbe7]  p-4 flex-col">
                <div class="text-[#d8d8d8]" data-icon="ChartBar" data-size="24px" data-weight="regular">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                    <path
                      d="M224,200h-8V40a8,8,0,0,0-8-8H152a8,8,0,0,0-8,8V80H96a8,8,0,0,0-8,8v40H48a8,8,0,0,0-8,8v64H32a8,8,0,0,0,0,16H224a8,8,0,0,0,0-16ZM160,48h40V200H160ZM104,96h40V200H104ZM56,144H88v56H56Z"
                    ></path>
                  </svg>
                </div>
                <div class="flex flex-col gap-1">
                  <h2 class="text-[#d8d8d8] text-base font-bold leading-tight">Estimate future healthcare costs</h2>
                  <p class="text-[#4e7397] text-sm font-normal leading-normal">
                    Our predictive model estimates how much you'll spend on medical care in the next year based on your current health data and lifestyle choices.
                  </p>
                </div>
              </div>
              <div class="flex flex-1 gap-3 rounded-lg border border-[#d0dbe7]  p-4 flex-col">
                <div class="text-[#d8d8d8]" data-icon="Users" data-size="24px" data-weight="regular">
                  <svg xmlns="http://www.w3.org/2000/svg" width="24px" height="24px" fill="currentColor" viewBox="0 0 256 256">
                    <path
                      d="M117.25,157.92a60,60,0,1,0-66.5,0A95.83,95.83,0,0,0,3.53,195.63a8,8,0,1,0,13.4,8.74,80,80,0,0,1,134.14,0,8,8,0,0,0,13.4-8.74A95.83,95.83,0,0,0,117.25,157.92ZM40,108a44,44,0,1,1,44,44A44.05,44.05,0,0,1,40,108Zm210.14,98.7a8,8,0,0,1-11.07-2.33A79.83,79.83,0,0,0,172,168a8,8,0,0,1,0-16,44,44,0,1,0-16.34-84.87,8,8,0,1,1-5.94-14.85,60,60,0,0,1,55.53,105.64,95.83,95.83,0,0,1,47.22,37.71A8,8,0,0,1,250.14,206.7Z"
                    ></path>
                  </svg>
                </div>
                <div class="flex flex-col gap-1">
                  <h2 class="text-[#d8d8d8] text-base font-bold leading-tight">Get personalized recommendations for improving your health</h2>
                  <p class="text-[#4e7397] text-sm font-normal leading-normal">
                    Our app uses your health data and lifestyle choices to provide personalized recommendations for improving your health and reducing your future medical costs.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <footer class="flex justify-center">
          <div class="flex max-w-[960px] flex-1 flex-col">
            <footer class="flex flex-col gap-6 px-5 py-10 text-center @container">
              <div class="flex flex-wrap items-center justify-center gap-6 @[480px]:flex-row @[480px]:justify-around">
                <a class="text-[#4e7397] text-base font-normal leading-normal min-w-40" href="/about">About</a>
                <a class="text-[#4e7397] text-base font-normal leading-normal min-w-40" href="/app2">Calculate</a>
                <a class="text-[#4e7397] text-base font-normal leading-normal min-w-40" href="/dashboard">Dashboard</a>
                <a class="text-[#4e7397] text-base font-normal leading-normal min-w-40" href="mailto:oaddonay@gmail.com">Contact</a>
              </div>
            </footer>
          </div>
        </footer>
      </div>
    </div>
  </body>
</html>

"""

html(html_page, height=1900)
# st.html(html_page)
