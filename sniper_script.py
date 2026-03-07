import requests
import json

def get_simo_links():
    # روابط جديدة تعمل في المغرب (مصادر دولية مفتوحة)
    data = {
        "en_sport": [
            {
                "name": "Paramount+ HD",
                "url": "https://dwstream.mobi/stream/paramount.m3u8", # رابط بديل ومباشر
                "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Paramount_Plus.svg"
            },
            {
                "name": "EuroSport 1",
                "url": "https://stmv.it.itv.com.br/eurosport1/index.m3u8", # رابط برازيلي قوي يعمل في المغرب
                "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Eurosport_logo.svg"
            }
        ],
        "en_news": [
            {
                "name": "BBC News",
                "url": "https://vs-hls-push-ww-live.akamaized.net/x=4/i=urn:bbc:pips:service:bbc_news_channel_hd/t=3840/v=pv14/b=5070016/main.m3u8",
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
        print("✅ Done! Simo Sniper updated the live links.")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    update_links_json()
