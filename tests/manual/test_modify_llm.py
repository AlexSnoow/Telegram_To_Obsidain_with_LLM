# python tests/manual/test_modify_llm.py
import sys
import os
from pathlib import Path

# Добавляем корень в PYTHONPATH (или лучше: pip install -e .)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from src.modify_llm import process_text_with_llm
from src.local_llm import LocalLLMClient


def main():
    # 1. Читаем файл из .TEMP/in
    input_dir = Path(".TEMP/in")
    output_dir = Path(".TEMP/out")
    output_dir.mkdir(exist_ok=True)

    test_file = input_dir / "test1.md"
    if not test_file.exists():
        print(f"❌ Файл {test_file} не найден. Создай его для теста.")
        return

    with open(test_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 2. Подключаемся к LLM
    llm = LocalLLMClient(base_url="http://localhost:8080")

    # 3. Обрабатываем
    print("Отправляем текст в LLM...")
    result = process_text_with_llm(content, llm)

    if not result:
        print("❌ Не удалось получить ответ от LLM.")
        return

    # 4. Сохраняем в .TEMP/out
    output_file = output_dir / f"processed_{test_file.name}"
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(result)

    print(f"✅ Результат сохранён: {output_file}")
    print("\nПервые 200 символов результата:")
    print(result[:200] + "...")


if __name__ == "__main__":
    main()
