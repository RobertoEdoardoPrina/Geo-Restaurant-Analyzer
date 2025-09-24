import csv
import re
import pandas as pd
from shapely.geometry import Polygon, Point
from shapely.wkt import loads as load_wkt

# Funzione per pulire e formattare le coordinate
def clean_and_format_coordinate(coord):
    coord = re.sub(r"[^\d\.\-]", "", coord)
    try:
        if coord == "":
            raise ValueError("Stringa vuota dopo la pulizia delle coordinate.")
        return ensure_six_decimals(coord)
    except ValueError:
        return "0.000000"

# Funzione per assicurare 6 decimali
def ensure_six_decimals(number_str):
    try:
        if '.' in number_str:
            integer_part, decimal_part = number_str.split('.')
            decimal_part = decimal_part.ljust(6, '0')[:6]
            return f"{integer_part}.{decimal_part}"
        else:
            return f"{number_str}.000000"
    except:
        return "0.000000"

# Funzione per leggere i poligoni dal file CSV
def read_polygons(file_path):
    df = pd.read_csv(file_path, header=None)
    polygons = []
    for _, row in df.iterrows():
        wkt_string = ' '.join(row.dropna().astype(str))
        try:
            polygon = load_wkt(wkt_string)
            polygons.append(polygon)
        except:
            continue
    return polygons

# Funzione per leggere i ristoranti dal file CSV
def read_restaurants(file_path):
    restaurants = []
    df = pd.read_csv(file_path)
    for _, row in df.iterrows():
        try:
            latitude = float(clean_and_format_coordinate(str(row['Latitude']).replace(',', '.')))
            longitude = float(clean_and_format_coordinate(str(row['Longitude']).replace(',', '.')))
            restaurants.append({
                "Name": row.get('Name', row.get('Name', 'Unknown')),
                "Point": Point(longitude, latitude)
            })
        except:
            continue
    return restaurants

# Funzione per salvare i risultati in un file CSV
def save_results(results, output_path):
    with open(output_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Name', 'Latitude', 'Longitude', 'Polygon Number'])
        writer.writeheader()
        writer.writerows(results)

# Funzione principale
def main(polygons_file, restaurants_file, output_file):
    polygons = read_polygons(polygons_file)
    restaurants = read_restaurants(restaurants_file)

    results = []
    for restaurant in restaurants:
        found = False
        for idx, polygon in enumerate(polygons, start=1):
            if polygon.contains(restaurant['Point']):
                results.append({
                    'Name': restaurant['Name'],
                    'Latitude': restaurant['Point'].y,
                    'Longitude': restaurant['Point'].x,
                    'Polygon Number': idx,
                })
                found = True
                break

        if not found:
            results.append({
                'Name': restaurant['Name'],
                'Latitude': restaurant['Point'].y,
                'Longitude': restaurant['Point'].x,
                'Polygon Number': 'N/A',            
                })

    save_results(results, output_file)
    print(f"Risultati salvati in {output_file}")

if __name__ == "__main__":
    polygons_file = 'Polygons.csv'
    restaurants_file = 'Restaurants.csv'
    output_file = 'Restaurants_in_zones.csv'

    main(polygons_file, restaurants_file, output_file)
