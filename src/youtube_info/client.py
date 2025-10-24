import yt_dlp
from typing import Optional, Dict, Any


def get_video_info(url: str) -> Optional[Dict[str, Any]]:
    """
    Получает информацию о видео с YouTube по URL.

    Args:
        url (str): Ссылка на видео (включая Shorts)

    Returns:
        dict или None: словарь с ключами:
            - title: str
            - description: str
            - subtitles: dict (язык -> текст) или None
            - url: str (нормализованный URL)
            - error: str (если произошла ошибка)
    """
    ydl_opts = {
        "quiet": True,
        "no_warnings": True,
        "extract_flat": False,
        "skip_download": True,
        "writesubtitles": False,
        "writeautomaticsub": True,  # автоматические субтитры (часто есть у Shorts)
        "subtitleslangs": ["en", "ru", "auto"],  # попробуем английский, русский, авто
        "simulate": True,  # не скачивать видео
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

            if not info:
                return {"error": "Не удалось извлечь информацию"}

            # Извлекаем субтитры
            subtitles = {}
            if info.get("requested_subtitles"):
                for lang, sub_info in info["requested_subtitles"].items():
                    if "data" in sub_info:
                        # Субтитры в формате SRT или VTT → преобразуем в чистый текст
                        raw = sub_info["data"]
                        # Простой парсинг: убираем временные метки
                        lines = [
                            line.strip()
                            for line in raw.splitlines()
                            if line.strip()
                            and not line.strip()
                            .replace(":", "")
                            .replace(",", "")
                            .replace(".", "")
                            .isdigit()
                        ]
                        subtitles[lang] = "\n".join(lines)

            return {
                "title": info.get("title", "Без названия"),
                "description": info.get("description", ""),
                "subtitles": subtitles or None,
                "url": info.get("webpage_url", url),
                "duration": info.get("duration", 0),  # в секундах
                "uploader": info.get("uploader", ""),
            }

    except Exception as e:
        return {"error": str(e)}
