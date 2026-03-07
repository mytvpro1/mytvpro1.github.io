import json

def main():
    # هذه هي قاعدة البيانات التي سيقرأها الـ index.html
    simo_final_data = {
        "beIN_Sports": [
            {"name": "beIN Sports 1 HD", "url": "رابط_القناة_هنا", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/BeIN_Sports_1_logo.svg/1024px-BeIN_Sports_1_logo.svg.png"},
            {"name": "beIN Sports 2 HD", "url": "رابط_القناة_هنا", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/BeIN_Sports_2_logo.svg/1024px-BeIN_Sports_2_logo.svg.png"}
        ],
        "fr_sport": [
            {"name": "Eurosport 1", "url": "https://index.iptv.ovh/eurosport1.m3u8", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c2/Eurosport_logo.svg/1024px-Eurosport_logo.svg.png"},
            {"name": "Paramount+ HD", "url": "https://demo.unified-streaming.com/k8s/features/stable/video/tears-of-steel/tears-of-steel.ism/.m3u8", "logo": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Paramount_Plus_logo.svg/1024px-Paramount_Plus_logo.svg.png"}
        ],
        "Sports": []
    }

    # كتابة الملف بصيغة JSON
    with open('links.json', 'w', encoding='utf-8') as f:
        json.dump(simo_final_data, f, ensure_ascii=False, indent=4)
    print("✅ links.json updated with beIN and International channels!")

if __name__ == "__main__":
    main()
