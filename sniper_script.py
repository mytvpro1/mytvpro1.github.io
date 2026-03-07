import requests
import json

def get_simo_links():
    # روابط m3u8 مباشرة بدون تعقيدات
    data = {
        "en_sport": [
            {
                "name": "Paramount+ HD",
                "url": "https://pplus-ch-us.akamaized.net/hls/live/2097312/primary/index.m3u8", 
                "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Paramount_Plus.svg"
            },
            {
                "name": "EuroSport 1",
                "url": "http://62.210.139.141:8000/live/eurosport1/playlist.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Eurosport_logo.svg"
            }
        ],
        "en_news": [
            {
                "name": "BBC News",
                "url": "http://103.199.161.254/Content/bbcworld/Live/Channel(BBCWorld)/index.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/commons/6/62/BBC_News_2022.svg"
            }
        ]
    }
    return data

def update_links_json():
    try:
        channels = get_simo_links()
        with open('links.json', 'w', encoding='utf-8') as f:
            json.dump(channels, f, ensure_ascii=False, indent=4)
        print("✅ Links Updated!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    update_links_json()
