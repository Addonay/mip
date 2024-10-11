import pickle
import random
import json
# Load the pre-trained model
model = pickle.load(open("dumped_stuff/model/rf_model.pkl", "rb"))

def gg(value: str, category: str):
    mapping = {
            "gender": {"male": 1, "female": 0},
            "smoker": {"no": 0, "yes": 1},
            "history": {"no": 0, "yes": 1},
        }
    return mapping[category].get(
            value.lower(), -1
        )  # Return -1 if the value is not found


def gg(value: str, category: str):
    mapping = {
        "gender": {"male": 1, "female": 0},
        "smoker": {"no": 0, "yes": 1},
        "history": {"no": 0, "yes": 1},
    }
    return mapping[category].get(
        value.lower(), -1
    )  # Return -1 if the value is not found


def one_hot_encode(user_data, bmi, label=False):
    # Define the categories for one-hot encoding
    region_categories = [
        "asia",
        "europe",
        "northamerica",
        "southamerica",
        "oceania",
        "africa",
        "antarctica",
    ]
    occupation_categories = [
        "salaried",
        "unemployed",
        "student",
        "business",
        "retired",
        "part-time",
        "consultant",
    ]

    # Create one-hot encoded vectors for non-label encoded features
    region_encoded = [
        1 if user_data["region"] == region else 0 for region in region_categories
    ]
    occupation_encoded = [
        1 if user_data["occupation"] == occupation else 0
        for occupation in occupation_categories
    ]

    # Get label-encoded values using the `gg` function
    label_encoded_gender = gg(user_data["gender"], "gender")
    label_encoded_smoker = gg(user_data["smoker"], "smoker")
    label_encoded_hdhistory = gg(user_data["heartDisease"], "history")

    # Combine all features into one list
    feature_list = (
        [
            int(user_data["age"]),
            label_encoded_gender,
            float(bmi),
            int(user_data["child_count"]),
            label_encoded_smoker,
        ]
        + region_encoded
        + [label_encoded_hdhistory]
        + occupation_encoded
    )

    # If label is True, return a dictionary for easier debugging and printing
    if label:
        return {
            "age": int(user_data["age"]),
            "gender": label_encoded_gender,
            "bmi": float(bmi),
            "child_count": int(user_data["child_count"]),
            "smoker": label_encoded_smoker,
            "region": region_encoded,
            "heart_disease_history": label_encoded_hdhistory,
            "occupation": occupation_encoded,
        }

    # Return list of features if label is False (for model prediction)
    return feature_list


# Random data generation logic
def generate_fake_user_data():
    ages = list(range(18, 80))
    genders = ["male", "female"]
    child_counts = list(range(0, 5))
    smoker_status = ["no", "yes"]
    regions = [
        "africa",
        "asia",
        "europe",
        "northamerica",
        "southamerica",
        "oceania",
        "antarctica",
    ]
    occupations = [
        "student",
        "salaried",
        "business",
        "unemployed",
        "retired",
        "part-time",
        "consultant",
    ]
    heart_disease_status = ["no", "yes"]

    data = {
        "age": random.choice(ages),
        "gender": random.choice(genders),
        "child_count": random.choice(child_counts),
        "smoker": random.choice(smoker_status),
        "region": random.choice(regions),
        "height": random.uniform(140, 200),  # Height in cm
        "weight": random.uniform(45, 120),  # Weight in kg
        "heartDisease": random.choice(heart_disease_status),
        "occupation": random.choice(occupations),
    }

    return data


# Function to calculate BMI
def calculate_bmi(height, weight):
    return float(weight) / (float(height) * float(height)) * 10000  # BMI formula


# Generate and predict charges for 100 fake instances
def generate_and_predict(model, num_instances=100, output_file="predicted_data.json"):
    predictions = []

    for _ in range(num_instances):
        # Generate random user data
        user_data = generate_fake_user_data()

        # Calculate BMI
        bmi = calculate_bmi(user_data["height"], user_data["weight"])

        # One-hot encoding and label encoding of input features
        X = one_hot_encode(user_data, bmi)

        # Make prediction using the model
        predicted_amount = model.predict([X])[0]

        # Add BMI and predicted amount to user data
        user_data["predicted_amount"] = int(predicted_amount)
        user_data["bmi"] = bmi

        # Append the user data with prediction to the list
        predictions.append(user_data)

    # Dump the predictions into a JSON file
    with open(output_file, "w") as json_file:
        json.dump(predictions, json_file, indent=4)

    print(f"Predictions saved to {output_file}")


# Run the function to generate 100 instances and save the predictions
generate_and_predict(model)
