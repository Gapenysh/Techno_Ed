import requests
from bs4 import BeautifulSoup
import json


def get_course_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Извлекаем весь текст из страницы
    page_text = soup.get_text(separator=' ', strip=True)

    return page_text

url = 'https://academy.itpark.tech/courses/?type=adult'
courses = get_course_data(url)


def save_courses_to_file(courses, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(courses, file, ensure_ascii=False, indent=4)

file_path = 'courses.json'
save_courses_to_file(courses, file_path)