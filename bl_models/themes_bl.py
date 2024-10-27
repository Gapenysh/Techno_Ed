from dal_models.themes_dal import ThemaDal


class ThemaBL(object):
    @staticmethod
    def get_themes():
        data = ThemaDal.get_themes()

        return data

    @staticmethod
    def get_theme_info(theme_id: int):
        data_themes = ThemaDal.get_theme_info(theme_id)

        return data_themes

    @staticmethod
    def get_courses_by_theme_and_level(theme_id: int, level_id: int):
        courses_data = ThemaDal.get_courses_by_theme_and_level(theme_id, level_id)
        return courses_data

    @staticmethod
    def create_answer(question_id, user_id, answer):
        data = ThemaDal.create_answer(question_id, user_id, answer)

        if data:
            print(data)
            return data

        else:
            return "Напишите, пожалуйста, ответ заново"



    @staticmethod
    def get_questions():
        data = ThemaDal.get_all_questions_theme()

        return (data)

    @staticmethod
    def get_quest_and_answer(user_id: int):
        data = ThemaDal.get_quest_and_answer(user_id)

        return data