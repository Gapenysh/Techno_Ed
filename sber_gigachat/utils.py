from langchain_community.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage
from config import gigachat_api

import json

chat = GigaChat(credentials=gigachat_api,
                verify_ssl_certs=False)

with open('courses.json', "r",encoding='utf-8') as file:
    data = json.load(file)

courses = data
print(courses)

query = input("Query: ")
def get_bot_response(query, courses):
    messages = [
        SystemMessage(content=f"Тебе задают организационный вопрос: {query} по поводу всяких курсов и преподавания. "
                              f"Дай обоснованный, подробный ответ, который удовлетворит спрашивающего, основываясь только на данные {courses}")
    ]
    messages.append(HumanMessage(content=query))

    res = chat.invoke(messages)
    messages.append(res)

    return res.content



print(get_bot_response(query, courses))