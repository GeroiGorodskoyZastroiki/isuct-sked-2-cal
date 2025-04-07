def get_uniq_audiences(schedule):
    audiences = list()
    for lesson in schedule:
        for audience in lesson['audiences']:
            if not any(audience['name'] == curr_audience.get("name") and lesson['subject'] == curr_audience.get("subject") for curr_audience in audiences):
                new_audience = {"name": audience['name'], "subject": lesson['subject']}
                audiences.append(new_audience)
    return audiences