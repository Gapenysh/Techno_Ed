from langchain_community.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage
from config import gigachat_api

import json

chat = GigaChat(credentials=gigachat_api,
                verify_ssl_certs=False)





def get_bot_response_courses(query, courses):
    with open('courses.json', "r", encoding='utf-8') as file:
        data = json.load(file)
    messages = [
        SystemMessage(content=f"Тебе задают организационный вопрос: {query} по поводу всяких курсов и преподавания. "
                              f"Дай обоснованный, подробный ответ, который удовлетворит спрашивающего, основываясь только на данные {data}")
    ]
    messages.append(HumanMessage(content=query))

    res = chat.invoke(messages)
    messages.append(res)

    return res.content


def generate_theme_user(question_answer):
    questions = [q for q, a in question_answer]
    answers = [a for q, a in question_answer]
    messages = [
        SystemMessage(content=f"Ты профессиональный HR, проанализируй ответы пользователя. Пользователь ответил на серию вопросов: {questions}, которые проверяют его предпочитаемое направление"
                              "передай одно из перечисленных специальностей, смотря от его ответов: Frontend, Backend, UI/UX дизайнер, DevOps,"
                              f"которое подходит человеку по его ответам: {answers} (порядок вопросов и ответов совпадает). Выведи только одно слово - специальность (Frontend, Backend, UI/UX дизайнер, DevOps)")
    ]


    res = chat.invoke(messages)
    messages.append(res)

    return res.content

def generate_level_user(answers, questions):
    messages = [SystemMessage(content="Пользователь ответил на серию вопросов, которые проверяют его предположительный уровень сложности для курсов, который может пройти"
                              "Сделай выбор между значениями: Легкий, Средний, Сложный"
                              f"На основе данных:{questions}, {answers} (Порядок вопросов/ответов совпадает)")]


    res = chat.invoke(messages)
    messages.append(res)

    return res.content

# print(gene(query, courses))