import requests
from typing import List, Dict, Optional


class LocalLLMClient:
    def __init__(self, base_url: str = "http://localhost:8080"):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def chat_complete(
        self,
        messages: List[Dict[str, str]],
        max_tokens: int = 512,
        temperature: float = 0.7,
        stream: bool = False,
    ) -> Optional[str]:
        """
        Отправляет запрос к локальной LLM через llamafile API.

        Args:
            messages: список сообщений в формате [{"role": "user", "content": "..."}, ...]
            max_tokens: максимальное количество генерируемых токенов
            temperature: креативность (0.0–1.0)
            stream: пока не поддерживается в простом режиме

        Returns:
            str: ответ модели или None при ошибке
        """
        url = f"{self.base_url}/v1/chat/completions"
        payload = {
            "model": "gemma-3-1b-it",  # имя не критично, но лучше указать
            "messages": messages,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "stream": stream,
        }

        try:
            response = self.session.post(url, json=payload, timeout=120)
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"Ошибка при обращении к LLM: {e}")
            return None
