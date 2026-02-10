from icalendar import Calendar, Event
from datetime import datetime
from .excel import load_custom_schedule

def create_calendar():
    print("Экспортируем кастомное расписание в календарь...")
    
    cal = Calendar()

    schedule = load_custom_schedule()
    for lesson in schedule:
        date_start = lesson['date']['start'].split('.')
        notify_date = lesson['date']['end'].split('.')
        time_start = lesson['time']['start'].split(':')
        time_end = lesson['time']['end'].split(':')
        week_day = datetime.strptime(lesson['date']['start'], "%d.%m.%Y").weekday()
        until = datetime(int(notify_date[2]), int(notify_date[1]), int(notify_date[0]), 23, 59, 59)
        
        event = Event()
        event.add('summary', lesson['view'])
        event.add('dtstart', datetime(int(date_start[2]), int(date_start[1]), int(date_start[0]), int(time_start[0]), int(time_start[1])))
        event.add('dtend', datetime(int(date_start[2]), int(date_start[1]), int(date_start[0]), int(time_end[0]), int(time_end[1])))
        event.add('rrule', {'freq': 'weekly', 'byweekdaynum': week_day, 'interval': 2, 'until': until})
        cal.add_component(event)


    notify_date = schedule[0]['date']['end'].split('.')
    if notify_date[1] == "12":
        notify_date[1] = 1
        notify_date[2] = int(notify_date[2]) + 1
    else: 
        notify_date[1] = 9

    notify_event = Event()
    notify_event.add('summary', "Воспользуйтесь isuct-sked-2-cal (см. описание)")
    notify_event.add('description', 'https://github.com/GeroiGorodskoyZastroiki/isuct-sked-2-cal')
    notify_event.add('dtstart', datetime(int(notify_date[2]), int(notify_date[1]), 1))
    notify_event.add('dtend', datetime(int(notify_date[2]), int(notify_date[1])+1, 1))
    cal.add_component(notify_event)

    with open('output/schedule.ics', 'wb') as f:
        f.write(cal.to_ical())

    print("Календарь успешно создан и сохранен в output/schedule.ics")