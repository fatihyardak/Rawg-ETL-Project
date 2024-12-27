import json
import os

class DataProcessor:
    def __init__(self, raw_data_path, processed_data_dir):
        self.raw_data_path = raw_data_path
        self.processed_data_dir = processed_data_dir
        self.data = []

    def load_data(self):
        """Veriyi ham JSON dosyasından yükler."""
        with open(self.raw_data_path, "r") as f:
            self.data = json.load(f)

    def normalize_data(self):
        """Veriyi normalize ederek oyun, mağaza ve platform bilgilerini ayrıştırır."""
        games = []
        game_stores = []
        game_platforms = []

        for game in self.data:
            # Temel oyun bilgilerini sakla
            games.append({
                "slug": game.get("slug"),
                "name": game.get("name"),
                "playtime": game.get("playtime"),
                "rating": game.get("rating"),
                "released": game.get("released")
            })

            # Mağaza bilgilerini normalize et
            if game.get("store"):
                for store in game["store"]:
                    game_stores.append({
                        "slug": game["slug"],
                        "store": store["store"]["name"]  # Sadece mağaza adını al
                    })

            # Platform bilgilerini normalize et
            if game.get("platform"):
                for platform in game["platform"]:
                    game_platforms.append({
                        "slug": game["slug"],
                        "platform": platform["platform"]["name"]  # Sadece platform adını al
                    })

        return games, game_stores, game_platforms

    def save_to_json(self, data, filename):
        os.makedirs(self.processed_data_dir, exist_ok=True)
        with open(f"{self.processed_data_dir}/{filename}", "w") as f:
            json.dump(data, f, indent=4)

    def process_and_save(self):
        self.load_data()
        games, game_stores, game_platforms = self.normalize_data()

        self.save_to_json(games, "games.json")
        self.save_to_json(game_stores, "game_stores.json")
        self.save_to_json(game_platforms, "game_platforms.json")

if __name__ == "__main__":
    raw_data_path = "data/raw/games_data.json"
    processed_data_dir = "data/processed"

    processor = DataProcessor(raw_data_path, processed_data_dir)
    processor.process_and_save()
    print("All files saved to 'data/processed/' successfully.")
