from relation.models import Relationship, Event
from django.contrib.auth.models import User
from django.db.models import Q

def get_history_relation(user_id):
    user = User.objects.get(pk=user_id)
    relations = Relationship.objects.filter(persons=user).order_by('-id')[:10]

    relations = [
        {
            'id': relation.pk,
            'other_person': relation.persons.exclude(pk=user.pk).first().profile.full_name,
            'level': relation.get_level_display()
        } for relation in relations
    ]

    return relations

def create_relation_record(user, data):
    persons = [ int(data['reporter_id']), int(data['friend_id']) ]
    users = User.objects.filter(pk__in=persons)

    relation = Relationship.objects.create(
        level=data['level'],
        created_by=user
    )
    relation.persons.set(users)

    return {
        'id': relation.pk,
        'person': users.first().profile.full_name,
        'other_person': users.last().profile.full_name,
        'level': relation.get_level_display()
    }


def get_event_history(user_id):
    user = User.objects.get(pk=user_id)
    events = Event.objects.filter(
        Q(reporter=user) |
        Q(participants=user)
    ).order_by('-id')[:10]

    events = [
        {
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
        } for event in events
    ] 

    return events