from django.db import models
from django.contrib.auth.models import User

VERY_CLOSED = '01'
HAVE_DISTANCE = '02'
CLOSED = '03'
ROOM_MATE = '04'

RELATION_LEVELS = [
    (VERY_CLOSED, 'สามี/ภรรยา'),
    (HAVE_DISTANCE, 'เพื่อนร่วมงาน/เพื่อนร่วมชั้น'),
    (CLOSED, ' เพื่อนสนิท/คนรัก'),
    (ROOM_MATE, 'เพื่อนร่วมห้อง'),
]

class Relationship(models.Model):
    # required exactly 2 persons.
    persons = models.ManyToManyField(User, related_name='relationship')
    level = models.CharField(max_length=2, choices=RELATION_LEVELS)
    created_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='relation_creator')

    def __str__(self):
        return 'Relationships of {} and {} is {}'.format(
            self.persons.first(), self.persons.last(), self.get_level_display()
        )

class Event(models.Model):
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
    finish = models.DateTimeField()
    localtion = models.TextField()
    reporter = models.ForeignKey(User, on_delete=models.PROTECT, related_name='event_reporter')
    participants = models.ManyToManyField(User, related_name='participant')
    created_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='event_creator')

    def __str__(self):
        return self.title
