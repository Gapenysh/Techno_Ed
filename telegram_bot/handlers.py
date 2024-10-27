from aiogram import Router, types, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import State, StatesGroup  # Новый импорт для состояний
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command

from sber_gigachat import generate_theme_user
from . import keyboards
from . import text
from bl_models.themes_bl import ThemaBL
from bl_models.user_bl import UserBL

class QuestionStates(StatesGroup):
    waiting_for_answer = State()
    current_question = State()

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
async def pick_theme(callback: CallbackQuery, state: FSMContext):
    telegram_id = callback.from_user.id

    await callback.message.answer("Пожалуйста, выберите направление")
    questions = ThemaBL.get_questions()
    user_info = UserBL.get_user_info(telegram_id)

    # Сохраняем telegram_id в состоянии
    await state.update_data(telegram_id=telegram_id, questions=questions, user_info=user_info, current_question_index=0)

    await ask_next_question(callback.message, state, telegram_id)


async def ask_next_question(message: types.Message, state: FSMContext, telegram_id: int):
    data = await state.get_data()
    questions = data['questions']
    current_question_index = data['current_question_index']

    if current_question_index < len(questions):
        question_text = questions[current_question_index][1]
        await message.answer(question_text)

        await state.set_state(QuestionStates.waiting_for_answer)
        await state.update_data(current_question_id=questions[current_question_index][0])
    else:
        await message.answer("Спасибо большое за ваши ответы, мы их записали.")
        await finish_questions(message, state, telegram_id)


@router.message(QuestionStates.waiting_for_answer)
async def handle_answer(message: types.Message, state: FSMContext):
    user_answer = message.text
    data = await state.get_data()
    current_question_id = data['current_question_id']
    user_info = data['user_info']

    telegram_id = data.get('telegram_id')

    data_1 = ThemaBL.create_answer(current_question_id, user_info[0], user_answer)
    if data_1: print('удачно')
    data['current_question_index'] += 1
    await state.update_data(current_question_index=data['current_question_index'])

    await ask_next_question(message, state, telegram_id)


async def finish_questions(message: types.Message, state: FSMContext, telegram_id: int):
    await state.clear()

    user_info = UserBL.get_user_info(telegram_id)
    level_id = user_info[3]
    user_theme_id = user_info[2]

    quest_and_answer = ThemaBL.get_quest_and_answer(user_info[0])

    result = generate_theme_user(quest_and_answer)

    await message.answer(result)

    courses = ThemaBL.get_courses_by_theme_and_level(user_theme_id, level_id)
    message_text = f"Направление: {user_theme_id}\n\n"
    for course in courses:
        message_text += f"- {course[1]}\n"

    await message.answer(message_text)


@router.callback_query(F.data == "teacher_communication")
async def get_themes(msg: Message):
    await msg.answer(f"Здесь можно будет общаться с преподом!")

@router.callback_query(F.data == "get_newsletter")
async def get_themes(msg: Message):
    await msg.answer(f"Здесь можно будет отправлять рассылки и еще кое-что!")

@router.callback_query(F.data == "get_vacancies_and_internships")
async def get_themes(msg: Message):
    await msg.answer(f"Здесь будут выводиться все стажи и вакансии")