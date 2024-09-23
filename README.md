# Medical Insurance Prediction

Welcome to the **Medical Insurance Prediction** project! This application utilizes machine learning techniques to predict medical insurance charges based on various user inputs. Follow the steps below to set up the environment, train the model, and run the application.

## Table of Contents

1. [Overview](#overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Model Training](#model-training)
5. [Testing the Application](#testing-the-application)
6. [Contributing](#contributing)
7. [License](#license)

## Overview

This project aims to develop a machine learning model that predicts insurance charges based on features such as age, gender, BMI, number of children, smoking status, and region. By leveraging the Random Forest Regressor algorithm, we can provide accurate predictions that can assist users in understanding their potential medical costs.

## Installation

To set up the project, you will need to install the required dependencies using **Poetry**. Follow these steps:

1. **Install Poetry** (if not already installed):

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/medical-insurance-prediction.git
   cd medical-insurance-prediction
   ```

3. **Install Dependencies**:

   ```bash
   poetry install
   ```

4. **Activate the Virtual Environment**:

   ```bash
   poetry shell
   ```

## Usage

Before running the application, ensure that the model is trained and the `rf_model.pkl` file is generated. Follow the steps below to train the model and run the application.

## Model Training

1. Navigate to the `model_train` notebook in your environment.
2. Select the Poetry kernel in your Jupyter environment.
3. Execute all cells in the notebook. This will preprocess the data, train the Random Forest model, and save the model as `rf_model.pkl`.

## Testing the Application

Once the model is trained, you can test the application:

1. Run the Streamlit application:

   ```bash
   streamlit run main.py
   ```

2. Open your web browser and navigate to `http://localhost:8501` to access the application interface.

3. Enter the required details (age, gender, BMI, number of children, smoking status, and region) in the input fields.

4. Click on the "Predict Amount" button to see the estimated insurance charges based on your inputs.

## Contributing

Contributions to the project are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
