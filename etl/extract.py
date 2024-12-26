import requests
import json
import os
from dotenv import load_dotenv

# load .env file
load_dotenv()

# getting the api key from the environment variable
api_key = os.getenv('RAWG_API_KEY')

def fetch_rawg_data(api_url="https://api.rawg.io/api/games", page_size=20, total_games=100):
    all_games = []
    page = 1
    date_range = "2024-01-01,2024-12-31"  # games only from 2024 
    while len(all_games) < total_games:
        response = requests.get(api_url, params={"key": api_key, "page_size": page_size, "page": page, "dates": date_range})
        response.raise_for_status()
        data = response.json()
        
        if len(data['results']) == 0:  # iif data is empty 
            break
        
        all_games.extend(data['results'])
        if len(data['results']) < page_size:  
            break
        page += 1
    return all_games[:total_games]  # total game  

# JSON Path
output_dir = 'data/raw'
output_file_path = os.path.join(output_dir, 'games_data.json')


if not os.path.exists(output_file_path):
    os.makedirs(output_dir, exist_ok=True)  # reposity create if not exist 
    games = fetch_rawg_data()  
    with open(output_file_path, 'w') as json_file:
        json.dump(games, json_file, indent=4)
else:
    print(f"Data already exists: '{output_file_path}'")

    