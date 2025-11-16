import pandas as pd

def transform_generation(raw_data):
    """
    Takes raw generation API data (list of dicts with 'startTime' and 'data' containing fuelType generations)
    and returns a DataFrame with one row per day:
    - 'date' (datetime)
    - 'total_generation' (sum of all fuel types)
    """
    rows = []
    for entry in raw_data:
        date = pd.to_datetime(entry["startTime"]).tz_localize(None).normalize()
        total = sum(item["generation"] for item in entry.get("data", []))
        rows.append({"date": date, "total_generation_gw": total/1000})  # Convert MW to GW
    
    df = pd.DataFrame(rows)
    return df
