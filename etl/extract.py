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
        
        # Keep only the desired keys
        filtered_games = []
        for game in data['results']:
            filtered_game = {
                'slug': game.get('slug'),
                'name': game.get('name'),
                'playtime': game.get('playtime'),
                'store': game.get('stores'),  # Nested structure
                'rating': game.get('rating'),
                'released': game.get('released'),
                'parent_platforms': game.get('parent_platforms'),  # Nested structure
                'platform': game.get('platforms')  # Nested structure
            }
            filtered_games.append(filtered_game)
        
        all_games.extend(filtered_games)
        if len(data['results']) < page_size:  
            break
        page += 1
    return all_games[:total_games]  # total game  

if __name__ == "__main__":
    # Fetch the data
    games_data = fetch_rawg_data()
    
    # Create the data/raw directory if it doesn't exist
    os.makedirs('data/raw', exist_ok=True)
    
    # Save the data to a JSON file in the data/raw folder
    with open('data/raw/games_data.json', 'w') as f:
        json.dump(games_data, f, indent=4)  # Save the data  