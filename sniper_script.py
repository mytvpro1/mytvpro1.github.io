import requests
import json
import os

def get_simo_links():
    # إعادة القنوات الدولية (فرنسا، ألمانيا، هولندا، وأمريكا)
    data = {
        "fr_channels": [
            {"name": "TF1 HD", "url": "https://p-fr-011.p-cdn.pro/TF1/index.m3u8", "logo": "https://upload.wikimedia.org/wikipedia/commons/2/23/TF1_logo_2013.svg"},
            {"name": "France 2", "url": "https://p-fr-011.p-cdn.pro/France2/index.m3u8", "logo": "https://upload.wikimedia.org/wikipedia/commons/e/e0/France_2_logo_2018.svg"},
            {"name": "M6 HD", "url": "https://p-fr-011.p-cdn.pro/M6/index.m3u8", "logo": "https://upload.wikimedia.org/wikipedia/commons/a/af/M6_logo_2009.svg"}
        ],
        "de_channels": [
            {"name": "ZDF HD", "url": "https://zdf-hls-15.akamaized.net/hls/live/2016498/de/veryhigh/master.m3u8", "logo": "https://upload.wikimedia.org/wikipedia/commons/4/41/ZDF_logo.svg"},
            {"name": "Das Erste", "url": "https://daserste-live.akamaized.net/hls/live/2021438/de/veryhigh/master.m3u8", "logo": "https://upload.wikimedia.org/wikipedia/commons/d/da/Das_Erste_logo_2014.svg"}
        ],
        "nl_channels": [
            {"name": "NPO 1", "url": "http://62.210.139.141:8000/live/npo1/playlist.m3u8", "logo": "https://upload.wikimedia.org/wikipedia/commons/1/1d/NPO_1_logo_2014.svg"},
            {"name": "NPO 2", "url": "http://62.210.139.141:8000/live/npo2/playlist.m3u8", "logo": "https://upload.wikimedia.org/wikipedia/commons/0/0e/NPO_2_logo_2014.svg"}
        ],
        "en_sport": [
            {"name": "Paramount+ HD", "url": "http://158.69.123.134:80/live/SimoGlobal/12345/10231.m3u8", "logo": "https://upload.wikimedia.org/wikipedia/commons/a/a5/Paramount_Plus.svg"},
            {"name": "EuroSport 1", "url": "http://62.210.139.141:8000/live/eurosport1/playlist.m3u8", "logo": "https://upload.wikimedia.org/wikipedia/commons/b/b3/Eurosport_logo.svg"}
        ]
    }
    return data

def update_links_json():
    try:
        channels = get_simo_links()
        with open('links.json', 'w', encoding='utf-8') as f:
            json.dump(channels, f, ensure_ascii=False, indent=4)
        print("✅ Simo Sniper: All International Channels Restored!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    update_links_json()
