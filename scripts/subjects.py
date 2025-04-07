def get_uniq_subjects(schedule):
    subjects = set()
    for lesson in schedule:
        subjects.add(lesson['subject'])
    return subjects