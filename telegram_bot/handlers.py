from aiogram import Router, types, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import State, StatesGroup  # Новый импорт для состояний
from aiogram.fsm.context import FSMContext
from aiogram import Bot
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import Command


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
    await callback.message.answer(text.text_pick_message)

    questions = ThemaBL.get_questions()
    telegram_id = callback.from_user.id
    user_info = UserBL.get_user_info(telegram_id)

    await state.update_data(questions=questions, user_info=user_info, current_question_index=0)

    await ask_next_question(callback, state)

async def ask_next_question(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    questions = data['questions']
    current_question_index = data['current_question_index']

    if current_question_index < len(questions):
        question = questions[current_question_index]
        await callback.answer(question[1])

        await state.set_state(QuestionStates.waiting_for_answer)

        await state.update_data(current_question_id=question[0])
    else:
        await message.answer("Спасибо большое за ваши ответы, мы их записали.")
        await finish_questions(callback, state)

@router.message(QuestionStates.waiting_for_answer)
async def handle_answer(message: types.Message, state: FSMContext):
    # Получаем ответ пользователя и текущий вопрос
    user_answer = message.text
    data = await state.get_data()
    current_question_id = data['current_question_id']
    user_info = data['user_info']

    ThemaBL.create_answer(current_question_id, user_info[0], user_answer)

    data['current_question_index'] += 1
    await state.update_data(current_question_index=data['current_question_index'])

    await ask_next_question(message, state)

async def finish_questions(callback: CallbackQuery, state: FSMContext):
    await state.finish()

    data = await state.get_data()
    user_info = data['user_info']
    level_id = user_info[3]
    user_theme_id = user_info[2]
    courses = ThemaBL.get_courses_by_theme_and_level(user_theme_id, level_id)

    message = f"Направление: {user_theme_id}\n\n"
    for course in courses:
        message += f"- {course[1]}\n"

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




