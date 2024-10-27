from dal_models.themes_dal import ThemaDal
from dal_models.user_dal import UserDal


class UserBL(object):
    @staticmethod
    def get_user_info(telegram_id):
        user_info = UserDal.get_user_info(telegram_id)

        return user_info

    @staticmethod
    def edit_user_theme(name):
        success = UserDal.edit_user_theme(name)

        if not success:
            return False
        return success
    @staticmethod
    def add_pdf_resume(pdf_file):
        success = UserDal.add_resume(pdf_file)

        if not success:
            return False
        return success
