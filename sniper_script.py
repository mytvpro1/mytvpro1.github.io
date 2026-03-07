import requests
import json

def get_best_links():
    # سيمو: هنا نضع الروابط الدولية التي تعمل في المغرب 100%
    # Paramount+ و Eurosport هما الأولوية الآن
    channels = {
        "en_sport": [
            {
                "name": "Paramount+ HD",
                "url": "https://raw.githubusercontent.com/Simo-Global/Stream/main/paramount.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Paramount_Plus.svg"
            },
            {
                "name": "EuroSport 1",
                "url": "https://index.iptv.ovh/eurosport1.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Eurosport_logo.svg"
            }
        ],
        "en_news": [
            {
                "name": "BBC News HD",
                "url": "https://vs-hls-push-ww-live.akamaized.net/x=4/i=urn:bbc:pips:service:bbc_news_channel_hd/t=3840/v=pv14/b=5070016/main.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/commons/6/62/BBC_News_2022.svg"
            }
        ]
    }
    return channels

def save_to_json():
    try:
        data = get_best_links()
        with open('links.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("✅ Success: Simo Sniper updated links.json")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    save_to_json()
