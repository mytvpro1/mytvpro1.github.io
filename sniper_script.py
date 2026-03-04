import json

def sniper_engine():
    # هذه القنوات ستكون ثابتة ويقوم الروبوت بتحديث روابطها
    channels = [
        {"name": "beIN Sports 1", "url": "https://example.com/live1.m3u8", "lang": "AR"},
        {"name": "beIN Sports 2", "url": "https://example.com/live2.m3u8", "lang": "AR"},
        {"name": "NOS Sport", "url": "https://example.com/nl1.m3u8", "lang": "NL"},
        {"name": "TF1 France", "url": "https://example.com/fr1.m3u8", "lang": "FR"}
    ]
    
    # هنا يتم حقن الروابط في ملف links.json
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(channels, f, ensure_ascii=False, indent=4)
    
    print("✅ تم تحديث القنوات بنجاح في links.json")

if __name__ == "__main__":
    sniper_engine()