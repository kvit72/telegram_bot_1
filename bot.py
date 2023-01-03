"""Телеграм бот для напоминаний."""

import time
import logging

from aiogram import Bot, Dispatcher, executor, types


TOKEN = ""
# Секретный ключ для доступа к боту.

MSG = "Ходил ли ты сегодня в тренажерный зал, {}?"
# Сообщение, которое будет напоминаться ботом.

bot = Bot(token=TOKEN)
dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    """Ассинхронная функция для управления работой бота."""
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    user_full_name = message.from_user.full_name
    logging.info(f"{user_id=} {user_full_name=} {time.asctime()}")
    await message.reply(f"Привет, {user_full_name}!")
    notification_time = 2

    for i in range(5):
        time.sleep(notification_time)
        notification_time += 10

        await bot.send_message(user_id, MSG.format(user_name))


if __name__ == '__main__':
    executor.start_polling(dp)