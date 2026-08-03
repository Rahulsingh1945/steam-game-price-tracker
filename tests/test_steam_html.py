import requests
from bs4 import BeautifulSoup


url = "https://store.steampowered.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")


games = soup.find_all("a", class_="store_capsule")


print("Games found:", len(games))


import pandas as pd

data = []

for game in games:
    img = game.find("img")

    app_id = game.get("data-ds-appid")

    name = img.get("alt") if img else None

    price = game.find("div", class_="discount_final_price")
    discount = game.find("div", class_="discount_pct")

    price = price.text.strip() if price else "N/A"
    discount = discount.text.strip() if discount else "No Discount"

    data.append({
        "app_id": app_id,
        "game_name": name,
        "price": price,
        "discount": discount
    })

df = pd.DataFrame(data)

df.to_csv("C:/project list/web scraping/steam-game-price-tracker/data/raw/steam_games.csv", index=False, encoding="utf-8-sig")

print(df)
print("\nsteam_games.csv")