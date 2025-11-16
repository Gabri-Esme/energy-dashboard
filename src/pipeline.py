import pandas as pd
from extract.api_extractor import fetch_api
from transform.transform_generation_data import transform_generation
from transform.transform_weather_data import transform_weather
from load.load import load_to_sqlite
import yaml

# Load configuration from YAML
with open("config/settings.yaml") as f:
    config = yaml.safe_load(f)

# Map source names to their corresponding transform functions
mapping = {
    "elexon_generation": transform_generation,
    "elexon_weather": transform_weather
}

# Get API rate limit delay (default 1 second)
delay = config.get("extract", {}).get("rate_limit_delay", 1)

# Loop over each data source defined in config
for source, urls in config["sources"].items():
    transform_function = mapping.get(source)
    urls_list = urls["url"] # Get the appropriate transform

    for url in urls_list:
        raw_data = fetch_api(url, delay) # Fetch raw JSON data

        transform_function = mapping.get(source)
        if transform_function:
            df = transform_function(raw_data) # Transform raw data into DataFrame
            load_to_sqlite(df, table_name=source) # Save DataFrame to SQLite
