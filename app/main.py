from fastapi import FastAPI
from app.services.get_data import fetch_and_store_data
from app.services.print_data import print_region_data

app = FastAPI()

@app.post("/get_data")
def get_data():
    fetch_and_store_data()
    return {"status": "Data fetched and stored successfully."}

@app.get("/print_data")
def print_data():
    print_region_data()
    return {"status": "Data printed successfully."}
