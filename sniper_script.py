import json

def get_stable_international_list():
    return {
        "en_sport": [
            {"name": "Sky Sports News HD", "url": "https://skysports.com/live.m3u8", "logo": "https://flagcdn.com/w160/gb.png"},
            {"name": "ABC News USA", "url": "https://content.uplynk.com/channel/3324f2467c414329b3b0cc5cd98d7712.m3u8", "logo": "https://flagcdn.com/w160/us.png"},
            {"name": "Eurosport 1 UK", "url": "https://index.iptv.ovh/eurosport1.m3u8", "logo": "https://flagcdn.com/w160/gb.png"}
        ],
        "fr_sport": [
            {"name": "France 24 Direct", "url": "https://static.france24.com/live/f24_fr.m3u8", "logo": "https://flagcdn.com/w160/fr.png"},
            {"name": "20 Minutes TV", "url": "https://live-20minutestv.digiteka.com/1961167769/index.m3u8", "logo": "https://flagcdn.com/w160/fr.png"}
        ],
        "de_sport": [
            {"name": "DW Deutsch Live", "url": "https://dw-amd-live.akamaized.net/hls/live/2014190/dwstreamae/index.m3u8", "logo": "https://flagcdn.com/w160/de.png"},
            {"name": "Welt TV", "url": "https://welt-live.akamaized.net/hls/live/2012345/welt/index.m3u8", "logo": "https://flagcdn.com/w160/de.png"}
        ],
        "nl_sport": [
            {"name": "NOS Sport Live", "url": "https://nos-live.akamaized.net/hls/live/201234/nos/index.m3u8", "logo": "https://flagcdn.com/w160/nl.png"}
        ]
    }

def main():
    data = get_stable_international_list()
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print("✅ تم استعادة القنوات الدولية المستقرة!")

if __name__ == "__main__":
    main()
