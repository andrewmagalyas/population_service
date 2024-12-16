from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from app.models import Country
from app.database import engine

Session = sessionmaker(bind=engine)

def print_region_data():
    session = Session()

    query = session.query(
        Country.region,
        func.sum(Country.population).label("total_population"),
        func.max(Country.population).label("max_population"),
        func.min(Country.population).label("min_population"),
    ).group_by(Country.region)

    for row in query:
        largest_country = session.query(Country).filter_by(region=row.region, population=row.max_population).first()
        smallest_country = session.query(Country).filter_by(region=row.region, population=row.min_population).first()

        print(f"""
        Region: {row.region}
        Total Population: {row.total_population}
        Largest Country: {largest_country.name} ({largest_country.population})
        Smallest Country: {smallest_country.name} ({smallest_country.population})
        """)
