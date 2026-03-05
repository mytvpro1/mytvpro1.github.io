import json
import requests
import re

def sniper_engine():
    print("🚀 جاري قنص روابط beIN Sports والروابط الدولية...")
    
    # قائمة ببعض المصادر التي تنشر روابط متجددة على GitHub (أمثلة لمصادر تقنص التوكن)
    sources = [
        "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/ar.m3u",
        "https://raw.githubusercontent.com/mohamed-elmesary/Arabic-IPTV/main/Arabic-IPTV.m3u"
    ]
    
    channels_data = {
        "ar_sport": [],
        "ar_news": [],
        "fr_sport": [],
        "nl_sport": []
    }

    # محرك بحث مصغر للبحث عن القنوات المطلوبة داخل المصادر
    for url in sources:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                content = response.text
                # البحث عن قنوات beIN
                for i in range(1, 11):
                    name = f"beIN SPORTS {i}"
                    # بحث بسيط عن الرابط بعد اسم القناة
                    pattern = rf"{name}.*?\n(http.*?\.m3u8)"
                    match = re.search(pattern, content, re.IGNORECASE)
                    if match:
                        link = match.group(1).strip()
                        if not any(c['name'] == name for c in channels_data["ar_sport"]):
                            channels_data["ar_sport"].append({
                                "name": name,
                                "url": link,
                                "logo": f"https://raw.githubusercontent.com/SimoGlobal/Logos/main/bein-{i}.png"
                            })
                
                # إضافة قناة الجزيرة كمثال للأخبار
                if "Al Jazeera" in content:
                    match = re.search(r"Al Jazeera.*?\n(http.*?\.m3u8)", content, re.IGNORECASE)
                    if match:
                        channels_data["ar_news"].append({
                            "name": "الجزيرة مباشر",
                            "url": match.group(1).strip(),
                            "logo": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f2/Aljazeera_eng.svg/1200px-Aljazeera_eng.svg.png"
                        })
        except:
            continue

    # في حال لم يجد القناص شيئاً، نضع روابط احتياطية لكي لا يبقى الموقع فارغاً
    if not channels_data["ar_sport"]:
        channels_data["ar_sport"] = [{"name": "beIN 1 (Server 2)", "url": "https://moctobpltc-i.akamaihd.net/hls/live/502913/mctp/mon01/index.m3u8", "logo": ""}]

    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(channels_data, f, ensure_ascii=False, indent=4)
    
    print("✅ انتهى القنص بنجاح!")

if __name__ == "__main__":
    sniper_engine()