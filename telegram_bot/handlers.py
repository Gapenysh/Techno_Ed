from aiogram import Router, types, F
from aiogram.types import Message
from aiogram.filters import Command

from . import keyboards
from . import text

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.start_message.format(name=msg.from_user.full_name), reply_markup=keyboards.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
async def message_handler(msg: Message):
    await msg.answer(f"Вы вышли в меню!")