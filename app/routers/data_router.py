from fastapi import APIRouter
from app.get_data import PopulationDataPipeline
from app.print_data import RegionDataProcessor
from app.config import SOURCE_URL

router = APIRouter()


@router.post("/get_data")
def get_data():
    pipeline = PopulationDataPipeline(SOURCE_URL)
    pipeline.run()
    return {"status": "Data fetched and stored successfully."}


@router.get("/print_data")
def print_data():
    processor = RegionDataProcessor()
    processor.display_region_data()
    processor.close()
    return {"status": "Data printed successfully."}
