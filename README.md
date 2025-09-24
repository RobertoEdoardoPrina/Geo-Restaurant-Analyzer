# Restaurant Polygon Checker

This project allows you to check whether specific restaurants (points) fall inside predefined geographical areas (polygons).  
The program analyzes restaurant coordinates and verifies if they are located inside or outside the given zones, producing a CSV file with the results.

## 📂 Project Structure

- **`polygon_check.py`** – Main Python script that performs the analysis.  
- **`Polygons.csv`** – File containing polygons in WKT (Well-Known Text) format.  
- **`Restaurants.csv`** – File containing the list of restaurants with their coordinates (latitude, longitude).  
- **`Restaurants_in_zones.csv`** – Output file generated with the results.  

## ⚙️ How It Works

1. The script loads polygons from `Polygons.csv`.  
2. It reads the list of restaurants from `Restaurants.csv`.  
3. For each restaurant, it checks whether the coordinates are inside one of the polygons.  
4. It saves the results into `Restaurants_in_zones.csv` with the following columns:
   - **Name** – Restaurant name  
   - **Latitude** – Latitude coordinate  
   - **Longitude** – Longitude coordinate  
   - **Polygon Number** – Polygon index containing the restaurant, or `N/A` if not inside any zone  

## 🚀 Usage

### 1. Requirements

Make sure you have Python 3 installed and the following libraries:

```bash
pip install pandas shapely
```

### 2. Run the Script

From the terminal, run:

```bash
python polygon_check.py
```

By default, the script will use:  
- `Polygons.csv`  
- `Restaurants.csv`  
and generate the file `Restaurants_in_zones.csv` in the same directory.

### 3. Input Files

- **Polygons.csv**: contains polygons in WKT format.  
- **Restaurants.csv**: must include at least the columns `Name`, `Latitude`, and `Longitude`.  

Example `Restaurants.csv`:

```csv
Name,Latitude,Longitude
Pizzeria Roma,41.9027835,12.4963655
Trattoria Milano,45.464211,9.191383
```

## 📤 Output

The `Restaurants_in_zones.csv` file will include the restaurants enriched with polygon information.  

Example:

```csv
Name,Latitude,Longitude,Polygon Number
Pizzeria Roma,41.902783,12.496366,1
Trattoria Milano,45.464211,9.191383,N/A
```

## 🛠 Customization

You can modify the input files (`Polygons.csv`, `Restaurants.csv`) to analyze different areas or points of interest.  
If you want to change the default input/output file names, edit the Python script in the following section:

```python
if __name__ == "__main__":
    polygons_file = 'Polygons.csv'
    restaurants_file = 'Restaurants.csv'
    output_file = 'Restaurants_in_zones.csv'
```
