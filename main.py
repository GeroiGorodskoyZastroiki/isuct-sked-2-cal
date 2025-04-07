import os
from scripts import schedule, teachers, excel, calendar

if not os.path.exists('output'):
    os.mkdir('output')

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

input("Откройте документ, прочитайте инструкцию и отредактируйте получившийся документ.\n" \
"P.S. ОБЯЗАТЕЛЬНО внестите ЛЮБОЕ изменение в документ.\n" \
"P.P.S Без этого Excel не кэширует значения вычисляемых ячеек и программа не сможет их считать на следующем шаге\n" \
"Нажмите Enter (КАК ТОЛЬКО ВЫПОЛНИЛИ ТО, ЧТО ОПИСАНО ВЫШЕ)")
calendar.create_calendar()