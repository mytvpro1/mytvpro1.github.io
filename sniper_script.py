import json

def sniper_engine():
    # قائمة القنوات الأساسية لموقع Simo Final
    channels = [
        {"name": "beIN Sports 1", "url": "https://example.com/live1.m3u8", "lang": "AR"},
        {"name": "NOS Sport (NL)", "url": "https://example.com/nl_live.m3u8", "lang": "NL"},
        {"name": "TF1 France (FR)", "url": "https://example.com/fr_live.m3u8", "lang": "FR"}
    ]
    
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(channels, f, ensure_ascii=False, indent=4)
    
    print("✅ القنوات عادت للحياة في links.json")

if __name__ == "__main__":
    sniper_engine()