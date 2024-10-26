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

@router.callback_query(F.data == "get_themes")
async def get_themes(msg: Message):
    await msg.answer(f"Здесь будут выводиться все темы и еще кое-что!")

@router.callback_query(F.data == "teacher_communication")
async def get_themes(msg: Message):
    await msg.answer(f"Здесь можно будет общаться с преподом!")

@router.callback_query(F.data == "get_newsletter")
async def get_themes(msg: Message):
    await msg.answer(f"Здесь можно будет отправлять рассылки и еще кое-что!")

@router.callback_query(F.data == "get_vacancies_and_internships")
async def get_themes(msg: Message):
    await msg.answer(f"Здесь будут выводиться все стажи и вакансии")




