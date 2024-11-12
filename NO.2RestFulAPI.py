import requests # type: ignore

def get_pokemon_data(pokemon_id):
    # ดึงข้อมูลสถิติ
    stats_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    response_stats = requests.get(stats_url)
    stats_data = response_stats.json()
    
    # ดึงข้อมูลชื่อและรูปภาพ
    sprites_url = f"https://pokeapi.co/api/v2/pokemon-form/{pokemon_id}"
    response_sprites = requests.get(sprites_url)
    sprites_data = response_sprites.json()

    # จัดรูปแบบข้อมูลตามที่ต้องการ
    pokemon_data = {
        "stats": stats_data.get("stats", []),
        "name": stats_data.get("name"),
        "sprites": sprites_data.get("sprites")
    }
    return pokemon_data

# ทดสอบฟังก์ชัน
pokemon_id = 1  # ตัวอย่างใช้ Bulbasaur
print(get_pokemon_data(pokemon_id))
