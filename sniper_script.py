import json

def sniper_engine():
    data = {
        "ar_sport": [
            {
                "name": "beIN Sports 1",
                # هذا رابط بث مباشر حقيقي للتجربة فقط
                "url": "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8", 
                "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/BeIN_Sports_logo.svg/2560px-BeIN_Sports_logo.svg.png"
            },
            {
                "name": "beIN Sports 2",
                "url": "https://bitdash-a.akamaihd.net/content/sintel/hls/playlist.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/BeIN_Sports_logo.svg/2560px-BeIN_Sports_logo.svg.png"
            }
        ],
        "ar_news": [
            {
                "name": "الجزيرة مباشر",
                "url": "https://live-hls-web-aje.getaj.net/AJE/index.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Aljazeera_eng.svg/1200px-Aljazeera_eng.svg.png"
            }
        ]
    }
    
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    print("✅ تم وضع روابط بث حقيقية للتجربة")

if __name__ == "__main__":
    sniper_engine()