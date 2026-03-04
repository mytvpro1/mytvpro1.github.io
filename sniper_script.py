import json

def sniper_engine():
    # قائمة القنوات الدولية والعربية لعام 2026
    channels = [
        {"name": "beIN Sports 1", "url": "https://example.com/bein1.m3u8", "lang": "AR"},
        {"name": "beIN Sports 2", "url": "https://example.com/bein2.m3u8", "lang": "AR"},
        {"name": "NOS Sport (NL)", "url": "https://example.com/nos_nl.m3u8", "lang": "NL"},
        {"name": "TF1 France (FR)", "url": "https://example.com/tf1_fr.m3u8", "lang": "FR"},
        {"name": "Sky Sports (EN)", "url": "https://example.com/sky_en.m3u8", "lang": "EN"}
    ]
    
    # حقن القنوات في ملف links.json
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(channels, f, ensure_ascii=False, indent=4)
    
    print("✅ تم صيد القنوات وتحديث links.json بنجاح")

if __name__ == "__main__":
    sniper_engine()