# RAWG ETL Project

## Overview
This project is an ETL (Extract, Transform, Load) pipeline that interacts with the RAWG API to extract data about video games, processes the data through transformation steps, and loads it into a SQLite database for further analysis and visualization.

---

## Project Objectives
- Extract raw video game data from the RAWG API.
- Transform and normalize the extracted data by cleaning and organizing it into multiple tables based on relevant categories.
- Load the processed data into a SQLite database for easy querying.
- Perform exploratory data analysis (EDA) on the collected data using Jupyter Notebook.

---

## Workflow

### 1. Extract
The data extraction is handled by the `extract.py` script.

#### Steps:
1. Fetches game data from the RAWG API using HTTP requests.
2. Filters games released within a specified date range (e.g., 2024).
3. Saves the raw data to `games_data.json`.

#### Key Features:
- Pagination is used to fetch large datasets.
- API key is loaded from an environment file.
- JSON structure adheres to the format provided by the RAWG API.

#### Files:
- **Script:** `extract.py`
- **Raw Data:** `games_data.json`

---

### 2. Transform
The transformation process is handled by the `transform.py` script.

#### Steps:
1. Unwanted columns are removed from the raw data.
2. Data is normalized into different tables:
   - Games
   - Platforms
   - Stores
3. Ensures consistency and avoids redundancy.

#### Normalized Tables:
- **Games:** Contains basic game details such as `name`, `rating`, and `release date`.
- **Platforms:** Maps games to supported platforms like `PC`, `PlayStation`, and `Xbox`.
- **Stores:** Tracks availability on stores such as `Steam`, `Epic Games`, and `GOG`.

#### Files:
- **Script:** `transform.py`
- **Normalized Data:**
  - `games.json`
  - `game_platforms.json`
  - `game_stores.json`

---

### 3. Load
The data loading process is handled by the `load.py` script.

#### Steps:
1. Reads normalized JSON files.
2. Inserts the data into a SQLite database.
3. Ensures proper table structure and indexing for optimized queries.

#### Files:
- **Script:** `load.py`
- **Database:** `games.db`

---

### 4. Analyze (EDA)
The analysis is performed in a Jupyter Notebook `eda.ipynb`.

#### Steps:
1. Loads data from the SQLite database.
2. Generates visualizations and basic analytics using libraries such as `pandas`, `matplotlib`, and `seaborn`.
3. Provides insights into:
   - Game ratings.
   - Popular platforms and stores.
   - Release trends.

#### Files:
- **Notebook:** `eda.ipynb`

---

## Prerequisites

1. Python 3.9+
2. Required Python Libraries:
   - `requests`
   - `pandas`
   - `matplotlib`
   - `seaborn`
   - `sqlite3`
   - `jupyter`
3. RAWG API key (stored in a `.env` file):
   ```
   RAWG_API_KEY=your_api_key_here
   ```

4. Install dependencies using:
   ```
   pip install -r requirements.txt
   ```

---

## How to Run the Project

1. Clone the repository:
   ```
   git clone https://github.com/fatihyardak/Rawg-ETL-Project.git
   cd Rawg-ETL-Project
   ```

2. Set up the `.env` file with your RAWG API key.

3. Run the extraction script:
   ```
   python extract.py
   ```

4. Run the transformation script:
   ```
   python transform.py
   ```

5. Run the loading script:
   ```
   python load.py
   ```

6. Open the Jupyter Notebook and start analyzing the data:
   ```
   jupyter notebook notebooks/eda.ipynb
   ```

---

## Directory Structure
```
Rawg-ETL-Project/
|-- data/
|   |-- raw/
|   |   |-- games_data.json
|   |-- processed/
|       |-- games.json
|       |-- game_platforms.json
|       |-- game_stores.json
|-- notebooks/
|   |-- eda.ipynb
|-- scripts/
|   |-- extract.py
|   |-- transform.py
|   |-- load.py
|-- games.db
|-- requirements.txt
|-- README.md
```

---

## Resources
- **RAWG API Documentation:** [https://rawg.io/apidocs](https://rawg.io/apidocs)
- **GitHub Repository:** [Rawg-ETL-Project](https://github.com/fatihyardak/Rawg-ETL-Project)
- **LinkedIn:** [Fatih Yardak](https://www.linkedin.com/in/fatih-y-2463b2219/)

---

## License
This project is licensed under the MIT License.

