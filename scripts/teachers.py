import os, requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup


def add_teachers_full_names(schedule):
    print("Загружаем список преподавателей вуза и ищем полные ФИО...")
    
    short_names = list(get_uniq_teachers_names(schedule))
    full_names = find_teachers_full_names(fetch_teachers_info())
    names_dict = match_teachers_names(short_names, full_names)

    for lesson in schedule:
        for i, teacher in enumerate(lesson['teachers']):
            lesson['teachers'][i] = {
                'name': teacher['name'],
                'full_name': names_dict[teacher['name']]}
    return schedule


def get_uniq_teachers_names(schedule):
    teachers = set()
    for lesson in schedule:
        for teacher in lesson['teachers']:
            teachers.add(teacher['name'])
    return teachers


def get_uniq_teachers(schedule):
    teachers = list()
    for lesson in schedule:
        for teacher in lesson['teachers']:
            if not any(teacher['name'] == curr_teacher.get("name") for curr_teacher in teachers):
                teachers.append(teacher)
    return teachers


def fetch_teachers_info():
    load_dotenv()
    url = os.getenv('URL_TEACHERS')
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def find_teachers_full_names(teachers_info):
    soup = BeautifulSoup(teachers_info, 'html.parser')
    fio_tags = soup.find_all('td', itemprop='fio')
    return [tag.text for tag in fio_tags]


def match_teachers_names(short_names, full_names):
    teachers = {}
    for teacher in short_names:
        first_name = teacher.split()[0]
        found = False
        for full_name in full_names:
            if first_name == full_name.split()[0]:
                teachers[teacher] = full_name
                found = True
                break
        if not found:
            teachers[teacher] = teacher
    return teachers