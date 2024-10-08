from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class DataModel(BaseModel):
    age: int
    gender: str
    children: int
    smoker: str
    region: str
    bmi: float
    heartDisease: str
    occupation: str


@app.post("/")
def get_data(data: DataModel):
    data_dict = data.model_dump()  # Use dict() instead of model_dump() for compatibility

    # Check if the file exists, and read the existing data
    file_path = "/home/addo/dev/projects/mip/assets/data.json"
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                existing_data = json.load(f)  # Load existing data
            except json.JSONDecodeError:
                existing_data = (
                    []
                )  # If the file is empty or invalid JSON, start with an empty list
    else:
        existing_data = []  # If the file does not exist, start with an empty list

    # Append the new data to the existing data
    existing_data.append(data_dict)

    # Write the updated data back to the file
    with open(file_path, "w") as f:
        json.dump(existing_data, f, indent=4)  # Write with indentation for readability

    return {"message": "Data saved successfully", "data": data_dict}
