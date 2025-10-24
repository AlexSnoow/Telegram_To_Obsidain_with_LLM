from typing import Optional
from src.local_llm import LocalLLMClient


def process_text_with_llm(
    text: str,
    llm_client: LocalLLMClient,
    max_tokens: int = 1024,
    temperature: float = 0.3,
) -> Optional[str]:
    """
    Обрабатывает входной текст с помощью LLM.

    Args:
        text (str): Исходный текст (например, содержимое .md файла)
        llm_client (LocalLLMClient): клиент для обращения к LLM
        max_tokens (int): макс. длина ответа
        temperature (float): креативность

    Returns:
        str или None: обработанный текст в формате Obsidian MD или None при ошибке
    """
    system_prompt = (
        "You are an expert assistant for processing Telegram messages into Obsidian notes. "
        "Your task is to:\n"
        "1. Keep the original meaning.\n"
        "2. Format the output as a clean Markdown note with YAML frontmatter.\n"
        "3. Add relevant tags like #Telegram, #LLM, #Obsidian.\n"
        "4. Use the current date for 'created'.\n"
        "5. Preserve key facts, remove noise."
    )

    user_prompt = f"Process this Telegram message into an Obsidian note:\n\n{text}"

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ]

    return llm_client.chat_complete(
        messages=messages, max_tokens=max_tokens, temperature=temperature
    )
