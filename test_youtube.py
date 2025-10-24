from youtube_info import get_video_info

url = "https://youtube.com/shorts/FrHBPT_p6h8?si=lfSG1POzNSEaIelH"
info = get_video_info(url)

if "error" in info:
    print("Ошибка:", info["error"])
else:
    print("Заголовок:", info["title"])
    print("Описание:", info["description"][:100] + "...")
    print("Автор:", info["uploader"])
    print("Длительность:", info["duration"], "сек")

    if info["subtitles"]:
        print("\nСубтитры:")
        for lang, text in info["subtitles"].items():
            print(f"\n[{lang}]")
            print(text[:200] + "..." if len(text) > 200 else text)
    else:
        print("\nСубтитры не найдены.")
