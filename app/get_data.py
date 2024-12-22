import re
import requests
from bs4 import BeautifulSoup
from app.database import SessionLocal
from app.models import Country


class PopulationDataCleaner:
    @staticmethod
    def clean_population(population_str):
        """
        Cleans population data by removing non-numeric characters and converting to an integer.
        Returns None if the input is invalid.
        """
        cleaned_str = re.sub(r'[^\d]', '', population_str)
        return int(cleaned_str) if cleaned_str.isdigit() else None


class PopulationDataFetcher:
    def __init__(self, source_url):
        self.source_url = source_url

    def fetch_data(self):
        """
        Fetches data from the source URL and parses it into a list of dictionaries.
        """
        try:
            response = requests.get(self.source_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from source URL: {e}")
            return []

        soup = BeautifulSoup(response.content, "html.parser")
        rows = soup.select("table.wikitable tbody tr")
        data = []

        for row in rows:
            columns = row.find_all("td")
            if len(columns) < 6:
                continue

            country_name = columns[0].text.strip()
            population_2023 = PopulationDataCleaner.clean_population(columns[2].text.strip())
            region = columns[4].text.strip() or "Unknown"

            if not country_name or not population_2023:
                print(f"Skipping invalid row: {row}")
                continue

            data.append({
                "name": country_name,
                "region": region,
                "population": population_2023,
            })

        return data


class PopulationDataSaver:
    def __init__(self):
        self.session = SessionLocal()

    def save_data(self, data):
        """
        Saves the cleaned data into the database.
        """
        if not data:
            print("No valid data to insert.")
            return

        try:
            self.session.query(Country).delete()
            self.session.bulk_insert_mappings(Country, data)
            self.session.commit()
            print(f"Successfully inserted {len(data)} countries.")
        except Exception as e:
            self.session.rollback()
            print(f"Error during database operation: {e}")
        finally:
            self.session.close()


class PopulationDataPipeline:
    def __init__(self, source_url):
        self.fetcher = PopulationDataFetcher(source_url)
        self.saver = PopulationDataSaver()

    def run(self):
        """
        Executes the data pipeline: fetch -> clean -> save.
        """
        data = self.fetcher.fetch_data()
        self.saver.save_data(data)
