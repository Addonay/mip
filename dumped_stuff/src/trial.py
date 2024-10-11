import polars as pl
import random


def determine_heart_disease_history(age: int, bmi: float, smoker: str) -> str:
    """
    Determine heart disease history based on age, BMI, and smoking status.

    :param age: Age of the individual.
    :param bmi: Body Mass Index of the individual.
    :param smoker: Smoking status of the individual ('yes' or 'no').
    :return: 'yes' or 'no' indicating heart disease history.
    """
    if age < 30 and bmi < 25:
        return "no"
    elif 30 <= age < 40 and smoker == "yes":
        return random.choice(["no", "yes"])  # Young smokers have some risk
    elif 30 <= age < 50 and 25 <= bmi < 30:
        return random.choice(["no", "yes"])  # Moderate risk
    elif 41 <= age < 50 and (bmi > 30 or smoker == "yes"):
        return "yes"  # Higher risk group
    elif 51 <= age < 60 and smoker == "yes":
        return "yes"  # Increased risk for older smokers
    elif age >= 60:
        return random.choice(["yes", "no"])  # High variability in older individuals
    else:
        return "no"  # Default case


def add_heart_disease_history(df: pl.DataFrame) -> pl.DataFrame:
    """
    Add a heart disease history column to the DataFrame based on the individual's attributes.

    :param df: Polars DataFrame containing the attributes.
    :return: Updated DataFrame with a new column for heart disease history.
    """
    return df.with_columns(
        pl.struct(["age", "bmi", "smoker"])
        .map_elements(
            lambda row: determine_heart_disease_history(
                row["age"], row["bmi"], row["smoker"]
            )
        )
        .alias("heart_disease_history")
    )

def determine_occupation(age: int, children: int) -> str:
    if age < 18:
        return "student"
    elif 18 <= age < 25:
        return random.choice(["student", "unemployed", "part-time"])
    elif 25 <= age < 30:
        if children == 0:
            return random.choice(["salaried", "business", "unemployed"])
        elif children > 0:
            return random.choice(["salaried", "unemployed", "business", "part-time"])
    elif 30 <= age < 40:
        if children == 0:
            return random.choice(["salaried", "business"])
        elif children > 0:
            return random.choice(["salaried", "unemployed", "business", "part-time"])
    elif 40 <= age < 60:
        if children > 0:
            return random.choice(["salaried", "business"])
        else:
            return random.choice(["salaried", "consultant", "unemployed"])
    else:  # 60 and above
        return random.choice(["retired", "unemployed"])


def add_occupation(df: pl.DataFrame) -> pl.DataFrame:
    return df.with_columns(
        pl.struct(["age", "children"])
        .map_elements(lambda row: determine_occupation(row["age"], row["children"]))
        .alias("occupation")
    )


def replace_region_with_continent(df: pl.DataFrame) -> pl.DataFrame:
    continents = [
        "Africa",
        "Asia",
        "Europe",
        "North America",
        "South America",
        "Oceania",
        "Antarctica",
    ]
    return df.with_columns(
        pl.Series([random.choice(continents) for _ in range(len(df))]).alias("region")
    )


# Read the CSV file
df = pl.read_csv("dumped_stuff/assets/insurance_2.csv")

df = add_heart_disease_history(df)
df = add_occupation(df)
df = replace_region_with_continent(df)

print(df.head())

df.write_csv("dumped_stuff/assets/insurance_new.csv")


# import polars as pl
# import random


# def determine_occupation(age: int, children: int) -> str:
#     if age < 23:
#         if children == 0:
#             return "student"
#         elif children == 1:
#             return random.choice(["unemployed", "salaried"])
#     return random.choice(["salaried", "student", "unemployed", "business"])


# def generate_rows(n: int) -> pl.DataFrame:
#     data = {
#         "age": [random.randint(18, 65) for _ in range(n)],
#         "sex": [random.choice(["male", "female"]) for _ in range(n)],
#         "bmi": [round(random.uniform(18.5, 40.0), 1) for _ in range(n)],
#         "children": [random.randint(0, 5) for _ in range(n)],
#         "smoker": [random.choice(["yes", "no"]) for _ in range(n)],
#         "region": [
#             random.choice(
#                 [
#                     "Africa",
#                     "Asia",
#                     "Europe",
#                     "North America",
#                     "South America",
#                     "Oceania",
#                     "Antarctica",
#                 ]
#             )
#             for _ in range(n)
#         ],
#         "charges": [round(random.uniform(1000, 50000), 2) for _ in range(n)],
#         "heart_disease_history": [random.choice(["yes", "no"]) for _ in range(n)],
#     }

#     df = pl.DataFrame(data)

#     # Add occupation using the determine_occupation function
#     df = df.with_columns(
#         occupation=pl.struct(["age", "children"]).map_elements(
#             lambda row: determine_occupation(row["age"], row["children"])
#         )
#     )

#     return df


# # Read the existing CSV file
# existing_df = pl.read_csv("dumped_stuff/assets/insurance.csv")

# # Generate 200 new rows
# new_rows = generate_rows(7275)

# # Combine existing data with new rows
# combined_df = pl.concat([existing_df, new_rows])

# # Display the first few rows of the updated dataset
# print(combined_df.head())

# # Display the total number of rows
# print(f"Total number of rows: {len(combined_df)}")

# # Save the updated dataset
# combined_df.write_csv("dumped_stuff/assets/hehe_2.csv")
