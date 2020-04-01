from relation.models import Relationship, Event
from django.contrib.auth.models import User
from datetime import datetime
from relation.datasources import map_relation, map_event

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

    return map_event(event)
