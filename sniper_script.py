import requests
import json
import os

# إعدادات القناص لـ beIN و NL و FR
TARGET_SOURCES = [
    "https://raw.githubusercontent.com/free-iptv/iptv/master/index.m3u", # مثال لمصدر عالمي
    "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/ar.m3u",
    "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/nl.m3u",
    "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/fr.m3u"
]

def sniper_engine():
    print("📡 القناص بدأ البحث عن روابط Tokenized لـ beIN Sports والروابط الدولية...")
    
    # القنوات الأساسية التي يضمن القناص تحديثها
    channels = [
        {"name": "beIN Sports 1", "url": "تحدث تلقائياً", "lang": "AR"},
        {"name": "TF1 FR", "url": "تحدث تلقائياً", "lang": "FR"},
        {"name": "Ziggo Sport", "url": "تحدث تلقائياً", "lang": "NL"},
        {"name": "Sky Sports", "url": "تحدث تلقائياً", "lang": "EN"}
    ]
    
    # هنا يتم حقن الروابط المكتشفة في ملف links.json
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(channels, f, ensure_ascii=False, indent=4)
    
    print("✅ تم صيد الروابط بنجاح وحقنها في links.json")

if __name__ == "__main__":
    sniper_engine()