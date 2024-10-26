from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

menu=[[InlineKeyboardButton(text="Направления", callback_data='get_themes'),
       InlineKeyboardButton(text="Связь с преподавателем", callback_data='teacher_communication')],
      [InlineKeyboardButton(text="Вакансии и стажировки", callback_data='get_vacancies_and_internships'),
       InlineKeyboardButton(text="Рассылка", callback_data='get_newsletter')]]


menu = InlineKeyboardMarkup(inline_keyboard=menu)
