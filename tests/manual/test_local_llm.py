# tests/manual/test_local_llm.py

import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.local_llm import LocalLLMClient


def main():
    llm = LocalLLMClient(base_url="http://localhost:8080")

    messages = [{"role": "user", "content": "Кратко объясни, что такое Markdown?"}]

    print("Отправляем запрос к LLM...")
    response = llm.chat_complete(messages, max_tokens=10000)

    if response:
        print("✅ Ответ:")
        print(response)
    else:
        print("❌ Не удалось получить ответ. Убедись, что llamafile запущен!")


if __name__ == "__main__":
    main()
