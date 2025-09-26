import os
from scripts import schedule, teachers, excel, calendar

def make_schedule_file():
    my_schedule = None
    while True:
        group = input("Введите номер группы: ")
        try:
            my_schedule = schedule.get_schedule(group)
            break 
        except ValueError as e:
            print(e)

    my_schedule = teachers.add_teachers_full_names(my_schedule)
    excel.create_workbook(my_schedule)


def make_calendar():
    input("Откройте документ, прочитайте инструкцию и отредактируйте получившийся документ\n" \
    "P.S. ОБЯЗАТЕЛЬНО внестите ЛЮБОЕ изменение в документ\n" \
    "P.P.S Без этого Excel не кэширует значения вычисляемых ячеек и программа не сможет их считать на следующем шаге\n" \
    "Нажмите Enter (КАК ТОЛЬКО ВЫПОЛНИЛИ ТО, ЧТО ОПИСАНО ВЫШЕ)")
    calendar.create_calendar()


output_dir_existed = os.path.exists('output')
if not output_dir_existed:
    print("Папки output не было - создаём")
    os.mkdir('output')

download = input("Вы ещё НЕ загружали расписание? (Y/n): ").strip().lower()
if download == '' or download == 'y' or not output_dir_existed:
    print("Создаём файл расписания")
    make_schedule_file()
else:
    print("Переходим к созданию календаря")
make_calendar()