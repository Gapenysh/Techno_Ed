from dal_models.themes_dal import ThemaDal
from dal_models.user_dal import UserDal


class UserBL(object):
    @staticmethod
    def get_user_info(telegram_id):
        user_info = UserDal.get_user_info(telegram_id)

        return user_info

    @staticmethods
    def edit_user_theme(name):
