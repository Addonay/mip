# import polars as pl
# import random


# def add_heart_disease_history(df: pl.DataFrame) -> pl.DataFrame:
#     return df.with_columns(
#         heart_disease_history=pl.Series(
#             [random.choice(["yes", "no"]) for _ in range(len(df))]
#         )
#     )


# def determine_occupation(age: int, children: int) -> str:
#     if age < 23:
#         if children == 0:
#             return "student"
#         elif children == 1:
#             return random.choice(["unemployed", "salaried"])
#     return random.choice(["salaried", "student", "unemployed", "business"])


# def add_occupation(df: pl.DataFrame) -> pl.DataFrame:
#     return df.with_columns(
#         occupation=pl.struct(["age", "children"]).map_elements(
#             lambda row: determine_occupation(row["age"], row["children"])
#         )
#     )


# def replace_region_with_continent(df: pl.DataFrame) -> pl.DataFrame:
#     continents = [
#         "Africa",
#         "Asia",
#         "Europe",
#         "North America",
#         "South America",
#         "Oceania",
#         "Antarctica",
#     ]
#     return df.with_columns(
#         region=pl.Series([random.choice(continents) for _ in range(len(df))])
#     )


# # Read the CSV file
# df = pl.read_csv("insurance_2.csv")

# # Add new columns
# df = add_heart_disease_history(df)
# df = add_occupation(df)
# df= replace_region_with_continent(df)

# # Display the first few rows of the updated dataset
# print(df.head())

# # Save the updated dataset
# df.write_csv("insurance_new.csv")


import polars as pl
import random


def determine_occupation(age: int, children: int) -> str:
    if age < 23:
        if children == 0:
            return "student"
        elif children == 1:
            return random.choice(["unemployed", "salaried"])
    return random.choice(["salaried", "student", "unemployed", "business"])


def generate_rows(n: int) -> pl.DataFrame:
    data = {
        "age": [random.randint(18, 65) for _ in range(n)],
        "sex": [random.choice(["male", "female"]) for _ in range(n)],
        "bmi": [round(random.uniform(18.5, 40.0), 1) for _ in range(n)],
        "children": [random.randint(0, 5) for _ in range(n)],
        "smoker": [random.choice(["yes", "no"]) for _ in range(n)],
        "region": [
            random.choice(
                [
                    "Africa",
                    "Asia",
                    "Europe",
                    "North America",
                    "South America",
                    "Oceania",
                    "Antarctica",
                ]
            )
            for _ in range(n)
        ],
        "charges": [round(random.uniform(1000, 50000), 2) for _ in range(n)],
        "heart_disease_history": [random.choice(["yes", "no"]) for _ in range(n)],
    }

    df = pl.DataFrame(data)

    # Add occupation using the determine_occupation function
    df = df.with_columns(
        occupation=pl.struct(["age", "children"]).map_elements(
            lambda row: determine_occupation(row["age"], row["children"])
        )
    )

    return df


# Read the existing CSV file
existing_df = pl.read_csv("assets/hehe.csv")

# Generate 200 new rows
new_rows = generate_rows(7275)

# Combine existing data with new rows
combined_df = pl.concat([existing_df, new_rows])

# Display the first few rows of the updated dataset
print(combined_df.head())

# Display the total number of rows
print(f"Total number of rows: {len(combined_df)}")

# Save the updated dataset
combined_df.write_csv("assets/hehe_2.csv")
