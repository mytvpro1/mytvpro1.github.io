import json
import requests

def sniper_engine():
    print("🚀 جاري القنص من المصادر العالمية المباشرة...")
    
    # هذه روابط مباشرة لملفات m3u يتم تحديثها باستمرار على GitHub
    sources = [
        "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/ar.m3u",
        "https://raw.githubusercontent.com/Stay-Live/Iptv-Arabic/main/Arabic.m3u"
    ]
    
    channels_data = {"ar_sport": [], "ar_news": [], "fr_sport": [], "nl_sport": []}

    # نحن نبحث عن beIN Sports تحديداً
    target_names = ["beIN SPORTS 1", "beIN SPORTS 2", "beIN SPORTS 3", "beIN SPORTS 4"]

    for url in sources:
        try:
            r = requests.get(url, timeout=15)
            if r.status_code == 200:
                lines = r.text.splitlines()
                for i, line in enumerate(lines):
                    for target in target_names:
                        if target in line and i+1 < len(lines):
                            stream_url = lines[i+1].strip()
                            if stream_url.startswith("http") and not any(c['name'] == target for c in channels_data["ar_sport"]):
                                channels_data["ar_sport"].append({
                                    "name": target,
                                    "url": stream_url,
                                    "logo": f"https://raw.githubusercontent.com/SimoGlobal/Logos/main/{target.replace(' ', '-')}.png"
                                })
        except:
            continue

    # إضافة قناة إخبارية حقيقية (الجزيرة)
    channels_data["ar_news"].append({
        "name": "الجزيرة مباشر",
        "url": "https://live-hls-web-aje.akamaized.net/hls/live/2036303/aje/index.m3u8",
        "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Aljazeera_eng.svg/1200px-Aljazeera_eng.svg.png"
    })

    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(channels_data, f, ensure_ascii=False, indent=4)
    
    print(f"✅ تم العثور على {len(channels_data['ar_sport'])} قنوات رياضية.")

if __name__ == "__main__":
    sniper_engine()