# telegram_reporter.py
import requests
import json
import os


def send_allure_summary_to_telegram(bot_token, chat_id, allure_results_path="allure-report"):
    """
    Отправляет сводку Allure отчета в Telegram
    """
    try:
        # Парсим результаты из allure-report
        summary_path = os.path.join(allure_results_path, 'widgets', 'summary.json')

        with open(summary_path, 'r', encoding='utf-8') as f:
            summary = json.load(f)

        # Извлекаем статистику
        statistic = summary.get('statistic', {})
        time_info = summary.get('time', {})

        total = statistic.get('total', 0)
        passed = statistic.get('passed', 0)
        failed = statistic.get('failed', 0)
        broken = statistic.get('broken', 0)
        skipped = statistic.get('skipped', 0)
        duration = time_info.get('duration', 0)

        # Рассчитываем проценты
        success_rate = round((passed / total) * 100, 2) if total > 0 else 0

        # Форматируем время
        duration_seconds = duration / 1000
        minutes = int(duration_seconds // 60)
        seconds = int(duration_seconds % 60)

        # Формируем сообщение
        message = f"""📊 **РЕЗУЛЬТАТЫ ТЕСТИРОВАНИЯ**

✅ Пройдено: {passed}
❌ Упало: {failed}
⚡ Сломано: {broken}
⏸️ Пропущено: {skipped}
📈 Всего тестов: {total}
⏱️ Время выполнения: {minutes}м {seconds}с

🎯 **Успешность: {success_rate}%**"""

        # Отправляем в Telegram
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'Markdown'
        }

        response = requests.post(url, data=payload)

        if response.status_code == 200:
            print("✅ Отчет успешно отправлен в Telegram")
        else:
            print(f"❌ Ошибка отправки: {response.text}")

    except FileNotFoundError:
        print(f"❌ Файл отчета не найден: {summary_path}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")


if __name__ == "__main__":
    # Получаем credentials из переменных окружения
    BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
    CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Не заданы TELEGRAM_BOT_TOKEN или TELEGRAM_CHAT_ID")
        exit(1)

    send_allure_summary_to_telegram(BOT_TOKEN, CHAT_ID)