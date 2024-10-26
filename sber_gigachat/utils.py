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
query_test = input("Query: ")

messages = [
    SystemMessage(
        content=f"Тебе задают организационный вопрос {query_test} по поводу всяких курсов и преподавания. "
                f"Дай обоснованный, подробный ответ, который удовлетворит спрашивающего, основываясь только на данные {courses}"
                f"не упоминай объект, из которого берешь информацию"
                f"Если затрудняешь ответить на основе {courses}, ответь как-нибудь обобщенно и отметь, что в It академии нет нужной темы"
    )
]


messages.append(HumanMessage(content=query_test))


res = chat.invoke(messages)
messages.append(res)
# print("Messages: ", messages)
print("Bot: ", res.content)