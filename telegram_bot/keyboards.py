from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from bl_models.themes_bl import ThemaBL


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
    return buttons


data_themes = ThemaBL.get_themes()
themes = InlineKeyboardMarkup(inline_keyboard=generate_buttons(data_themes))
menu = InlineKeyboardMarkup(inline_keyboard=menu)

