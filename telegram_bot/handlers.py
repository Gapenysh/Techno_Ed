from aiogram import Router, types, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from . import keyboards
from . import text
from bl_models.themes_bl import ThemaBL
from bl_models.user_bl import UserBL

router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(text.start_message.format(name=msg.from_user.full_name), reply_markup=keyboards.menu)

@router.message(F.text == "Меню")
@router.message(F.text == "Выйти в меню")
async def message_handler(msg: Message):
    await msg.answer(f"Вы вышли в меню!")

@router.callback_query(F.data == "get_themes")
async def get_themes(callback: CallbackQuery):
    await callback.message.answer(text.get_themes_message, reply_markup=keyboards.themes)


@router.callback_query(F.data.startswith("theme_info_"))
async def show_theme_info(callback: CallbackQuery):
    theme_id = callback.data.split("_")[2]
    theme_info = ThemaBL.get_theme_info(theme_id)
    telegram_id = callback.from_user.id
    user_info = UserBL.get_user_info(telegram_id)
    level_id = user_info[3]

    courses = ThemaBL.get_courses_by_theme_and_level(theme_id, level_id)


    message = f"Направление: {theme_info[1]}\n\n"
    message += f"{theme_info[2]}\n"
    message += f"{courses}"

    await callback.message.answer(message)

@router.callback_query(F.data.startswith("pick_theme"))
async def pick_theme(callback: CallbackQuery):
    await callback.message.answer(text.text_pick_message)
    telegram_id = callback.from_user.id
    user_info = UserBL.get_user_info(telegram_id)
    level_id = user_info[3]
    user_theme_id = user_info[2]

    courses = ThemaBL.get_courses_by_theme_and_level(user_theme_id, level_id)

    message = f"Направление: {theme_info[1]}\n\n"
    message += f"{theme_info[2]}\n"

    await callback.message.answer(message)




@router.callback_query(F.data == "teacher_communication")
async def get_themes(msg: Message):
    await msg.answer(f"Здесь можно будет общаться с преподом!")

@router.callback_query(F.data == "get_newsletter")
async def get_themes(msg: Message):
    await msg.answer(f"Здесь можно будет отправлять рассылки и еще кое-что!")

@router.callback_query(F.data == "get_vacancies_and_internships")
async def get_themes(msg: Message):
    await msg.answer(f"Здесь будут выводиться все стажи и вакансии")




