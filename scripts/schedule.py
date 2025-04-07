import os, re, requests
from dotenv import load_dotenv


def get_schedule(group):
    print("Загружаем расписание и ищем вашу группу...")
    
    return get_group_schedule(fetch_university_schedule(), group)


def fetch_university_schedule():
    load_dotenv()
    url = os.getenv('URL_SCHEDULE')
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_group_schedule(schedule, group):
    for faculty in schedule['faculties']:
        for grp in faculty['groups']:
            if re.sub("[^0-9]", "", grp['name']) == re.sub("[^0-9]", "", group):
                return grp['lessons']
    raise ValueError(f"Группа {group} не найдена в расписании")
