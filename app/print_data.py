from sqlalchemy import func
from app.database import SessionLocal
from app.models import Country

class RegionDataProcessor:
    def __init__(self):
        self.session = SessionLocal()

    def fetch_region_data(self):
        """
        Fetch aggregated region data from the database.
        """
        return self.session.query(
            Country.region,
            func.sum(Country.population).label("total_population"),
            func.max(Country.population).label("max_population"),
            func.min(Country.population).label("min_population"),
        ).group_by(Country.region).all()

    def get_country_by_population(self, region, population):
        """
        Fetch a country by region and population.
        """
        return self.session.query(Country).filter_by(region=region, population=population).first()

    def format_region_data(self):
        """
        Format the region data into a human-readable format.
        """
        data = []
        for row in self.fetch_region_data():
            largest_country = self.get_country_by_population(row.region, row.max_population)
            smallest_country = self.get_country_by_population(row.region, row.min_population)

            if not largest_country or not smallest_country:
                continue

            data.append({
                "region": row.region,
                "total_population": row.total_population,
                "largest_country": {
                    "name": largest_country.name,
                    "population": largest_country.population,
                },
                "smallest_country": {
                    "name": smallest_country.name,
                    "population": smallest_country.population,
                }
            })
        return data

    def display_region_data(self):
        """
        Print the formatted region data.
        """
        for region_data in self.format_region_data():
            print(f"""
            Region: {region_data['region']}
            Total Population: {region_data['total_population']}
            Largest Country: {region_data['largest_country']['name']} 
            Population of the largest country: {region_data['largest_country']['population']}
            Smallest Country: {region_data['smallest_country']['name']} 
            Population of the smallest country: {region_data['smallest_country']['population']}
            """)

    def close(self):
        """
        Close the database session.
        """
        self.session.close()



