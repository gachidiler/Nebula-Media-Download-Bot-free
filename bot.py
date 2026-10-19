
import os
import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("NEBULA")

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✦ NEBULA MUSIC\n\n"
        "Привет! Добро пожаловать в NEBULA.\n\n"
        "🎧 Отправь ссылку на YouTube или SoundCloud.\n"
        "🌌 Музыка — без платы за использование бота.\n\n"
        "Сервис пока находится в разработке."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✦ Как пользоваться NEBULA\n\n"
        "1. Отправь ссылку на трек.\n"
        "2. Дождись обработки.\n\n"
        "Скачивание станет доступно после подключения "
        "модуля обработки аудио."
    )


async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if "youtube.com/" in text or "youtu.be/" in text:
        service = "YouTube"
    elif "soundcloud.com/" in text:
        service = "SoundCloud"
    else:
        await update.message.reply_text(
            "Пожалуйста, отправь ссылку на YouTube или SoundCloud."
        )
        return

    await update.message.reply_text(
        f"✦ NEBULA\n\n"
        f"Источник: {service}\n"
        "Ссылка принята!\n\n"
        "Модуль скачивания пока подключается. "
        "Следующий этап — настройка аудиообработки."
    )


def main():
    if not TOKEN:
        raise RuntimeError("Не задан BOT_TOKEN.")

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link)
    )

    logger.info("NEBULA запускается")
    app.run_polling()


if __name__ == "__main__":
    main()

