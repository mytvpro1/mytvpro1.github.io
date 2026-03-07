import json

def generate_links():
    # هذه هي قاعدة البيانات التي يحتاجها موقعك الجديد (en_sport و en_news)
    data = {
        "en_sport": [
            {
                "name": "beIN Sports 1 HD",
                "url": "https://example.com/live/bein1.m3u8", # القناص سيحدث هذا الرابط
                "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/BeIN_Sports_1_logo.svg/1024px-BeIN_Sports_1_logo.svg.png"
            },
            {
                "name": "beIN Sports 2 HD",
                "url": "https://example.com/live/bein2.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/BeIN_Sports_2_logo.svg/1024px-BeIN_Sports_2_logo.svg.png"
            },
            {
                "name": "EuroSport 1 HD",
                "url": "https://index.iptv.ovh/eurosport1.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Eurosport_logo.svg/1024px-Eurosport_logo.svg.png"
            }
        ],
        "en_news": [
            {
                "name": "Al Jazeera English",
                "url": "https://live-hls-web-aje.getaj.net/AJE/index.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Aljazeera_eng.svg/1024px-Aljazeera_eng.svg.png"
            },
            {
                "name": "BBC News",
                "url": "https://bbc-news.com/live.m3u8",
                "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/62/BBC_News_2019.svg/1024px-BBC_News_2019.svg.png"
            }
        ]
    }
    return data

def main():
    # إنشاء ملف الروابط النهائي
    final_data = generate_links()
    
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(final_data, f, ensure_ascii=False, indent=4)
    
    print("✅ Done! links.json synchronized with MYTVPRO Global Design.")

if __name__ == "__main__":
    main()
