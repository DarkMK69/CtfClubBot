import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
token = os.environ.get('BOT_TOKEN')
from handlers import common_router


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=token)
# Диспетчер
dp = Dispatcher()

dp.include_routers(common_router,)


# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())