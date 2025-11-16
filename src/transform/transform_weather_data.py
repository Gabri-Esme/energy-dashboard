import pandas as pd

def transform_weather(raw_data):
    """
    Transform raw weather JSON into a DataFrame with date and temperature.
    - 'date': normalized, naive datetime (no timezone, time set to 00:00)
    - 'temp': temperature in Celsius
    """
    data = raw_data.get('data', [])
    return pd.DataFrame([
        {'date': pd.to_datetime(item['measurementDate']).tz_localize(None).normalize(),
         'temp': item['temperature']}
        for item in data
    ])
