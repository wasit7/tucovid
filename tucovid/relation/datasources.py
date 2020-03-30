def map_relation(relation, current_user):
    return {
        'id': relation.pk,
        'other_person': relation.persons.exclude(pk=current_user.pk).first().profile.full_name,
        'level': relation.get_level_display()
    }

def map_event(event):
    return {
        'id': event.pk,
        'title': event.title,
        'reporter': {
            'name': event.reporter.profile.full_name
        },
        'location': event.location,
        'start': event.start.strftime('%-d %b %Y %H:%M'),
        'finish': event.finish.strftime('%-d %b %Y %H:%M'),
        'participants': [
            {
                'name': participant.profile.full_name
            } for participant in event.participants.all()
        ]
    }
