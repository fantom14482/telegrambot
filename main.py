from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
import asyncio
import os

from background import keep_alive

BOT_TOKEN = os.getenv("7919378958:AAH4aT87Uq93mril_MI_r39ubxsz010JlKo")
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer("👋 Привет! Напиши название песни, и я поищу её для тебя 🎵")

@dp.message()
async def handle_message(message: Message):
    query = message.text.strip()
    await message.answer(f"🔍 Ищу: {query}")
    # Здесь будет логика поиска

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    keep_alive()
    asyncio.run(main())
