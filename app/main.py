from fastapi import FastAPI

from app.config import SOURCE_URL
from app.database import engine, Base
from app.get_data import PopulationDataPipeline
from app.print_data import RegionDataProcessor

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/get_data")
def get_data():
    pipeline = PopulationDataPipeline(SOURCE_URL)
    pipeline.run()
    return {"status": "Data fetched and stored successfully."}


@app.get("/print_data")
def print_data():
    processor = RegionDataProcessor()
    processor.display_region_data()
    processor.close()
    return {"status": "Data printed successfully."}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
