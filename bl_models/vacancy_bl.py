from dal_models.vacancy_dal import VacansyDAL

class VacancyBL:
    @staticmethod
    def get_vacancies():
        result = VacansyDAL.get_vacansy()

        if not result:
            return None
        return result
    @staticmethod
    def get_interships():
        result = VacansyDAL.get_intership()
        if not result:
            return None
        return result