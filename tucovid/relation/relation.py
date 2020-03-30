from relation.models import Relationship, Event
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import datetime
from relation.datasources import map_relation

def get_relation_history(user_id):
    user = User.objects.get(pk=user_id)
    relations = Relationship.objects.filter(persons=user).order_by('-id')[:10]

    return [ map_relation(relation, user) for relation in relations ]

def create_relation_record(user, data):
    reporter_id = data['reporter_id'] if user.is_staff else user
    reporter = User.objects.get(pk=reporter_id)
    friend = User.objects.get(pk=data['friend_id'])

    relation = Relationship()
    relation.level = data['level']
    relation.created_by = user
    relation.save()

    relation.persons.set([reporter, friend])

    return map_relation(relation, reporter)

def get_event_history(user_id):
    user = User.objects.get(pk=user_id)
    events = Event.objects.filter(
        Q(reporter=user) |
        Q(participants=user)
    ).order_by('-id')[:10]

    events = [
        {
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
        } for event in events
    ] 

    return events

def create_event_record(user, data):
    reporter_id = data['reporter_id'] if user.is_staff else user

    reporter = User.objects.get(pk=reporter_id)
    participants = User.objects.filter(pk__in=data['participants'])

    event = Event()
    event.title = data['title']
    event.start = datetime.strptime(data['start'], '%Y-%m-%d %H:%M')
    event.finish = datetime.strptime(data['finish'], '%Y-%m-%d %H:%M')
    event.location = data['location']
    event.reporter = reporter
    event.created_by = user
    event.save()

    event.participants.set(participants)

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
