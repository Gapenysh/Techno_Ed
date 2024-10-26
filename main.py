import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

import config
from telegram_bot.handlers import router


async def main():
    # Задаем параметры бота с parse_mode напрямую
    bot = Bot(token=config.BOT_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_router(router)

    # Удаление вебхука и разрешение обновлений
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":  # Исправлено условие на правильное
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())