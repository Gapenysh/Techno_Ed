from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from bl_models.themes_bl import ThemaBL
from bl_models.vacancy_bl import VacancyBL


menu=[[InlineKeyboardButton(text="Направления", callback_data='get_themes')],
       [InlineKeyboardButton(text="Связь с преподавателем", callback_data='teacher_communication')],
       [InlineKeyboardButton(text="Вакансии и стажировки", callback_data='get_vacancies_and_internships')],
       [InlineKeyboardButton(text="Рассылка", callback_data='get_newsletter')]]


def generate_buttons(themes) -> list:
    buttons = []
    for theme in themes:
        button = InlineKeyboardButton(
            text=theme[1],
            callback_data=f"theme_info_{theme[0]}"
        )
        buttons.append([button])

    # Добавляем кнопку "Назад"
    pick_theme = InlineKeyboardButton(
        text="Подобрать направление",
        callback_data="pick_theme"
    )




    back_menu = InlineKeyboardButton(
        text="Вернуться в меню",
        callback_data="back_menu"
    )
    buttons.append([pick_theme])
    buttons.append([back_menu])

    return buttons


data_vacancies = VacancyBL.get_vacancies()
data_themes = ThemaBL.get_themes()

themes = InlineKeyboardMarkup(inline_keyboard=generate_buttons(data_themes))
menu = InlineKeyboardMarkup(inline_keyboard=menu)
