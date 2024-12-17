import requests
from bs4 import BeautifulSoup
from app.database import SessionLocal
from app.models import Country
from app.config import SOURCE_URL

def fetch_and_store_data():
    response = requests.get(SOURCE_URL)
    soup = BeautifulSoup(response.content, "html.parser")

    rows = soup.select("table.wikitable tbody tr")[1:]
    data = []
    for row in rows:
        columns = row.find_all("td")
        if not columns:
            continue
        country_name = columns[1].text.strip()
        region = columns[2].text.strip()
        population = int(columns[3].text.replace(",", "").strip())

        data.append({"name": country_name, "region": region, "population": population})

    session = SessionLocal()
    session.query(Country).delete()  # Очистка старих даних
    session.bulk_insert_mappings(Country, data)
    session.commit()
