import pandas as pd
import json
import os

def json_to_csv(json_file, csv_file):
    # Read the JSON file
    data = pd.read_json(json_file)
    # Convert to CSV and save
    data.to_csv(csv_file, index=False)

# Define the paths for the JSON files and their corresponding CSV files
json_files = [
    'data/processed/games.json',
    'data/processed/game_stores.json',
    'data/processed/game_platforms.json'
]

csv_files = [
    'data/processed/games.csv',
    'data/processed/game_stores.csv',
    'data/processed/game_platforms.csv'
]

# Transform each JSON file to CSV
for json_file, csv_file in zip(json_files, csv_files):
    json_to_csv(json_file, csv_file)


