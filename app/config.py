import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/population_db")
SOURCE_URL = os.getenv("SOURCE_URL", "https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1215058959")
