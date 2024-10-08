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

You can check the live [demo](https://check-this-out.streamlit.app) by clicking on this link

## Installation

To set up the project, you will need to install the required dependencies using **Poetry**. Follow these steps:

1. **Install Poetry** (if not already installed):

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

2. **Clone the Repository**:

   ```bash
   git clone https://github.com/addonayosoro/mip.git
   cd mip
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
   streamlit run src/main.py
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


The presentation will be 10-12 minutes with these items:

- Brief background of the case study selected which would discuss the objective for
the project, for example: vividly describe a furniture store whose owner would want
DAT 2102 [July 2024] Semester Project || Page 2
to predict the costs of different types of wood. This case study can be based on a
real-life example or a fictional case prepared as a group
- Description of the dataset used in the project: rows, columns, brief descriptive
statistics etc.
- Data cleaning techniques used e.g. dropping columns, log transformation for
normalisation
- Modelling approach applied: algorithm used, train/test split ratio, algorithm and
model validation approach/results e.g. k-fold cross validation.
- Live demo of application (include the link to your application in this slide as you
demonstrate the working of the app)
- Conclusion to business objective set i.e. does the wood cost predictor application
achieve what the store owner wanted? What features can be added to this
application to ensure full functionality..

in my case i used random forest regressor and gridsearchcv instead of a simple linear regression. somem of the columns in my dataset include age, bmi,sex, region,smoker, children,occupation and heart_disease_history. the last column and the one being predicted is charges.
