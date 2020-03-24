from django.db import models
from django.contrib.auth.models import User

class Relationship(models.Model):
    FAMILY_RELATION = 'FR'
    CLOSE_FRIEND_RELATION = 'CR'

    RELATION_LEVELS = [
        (FAMILY_RELATION, 'Family'),
        (CLOSE_FRIEND_RELATION, 'Close friend'),
    ]

    # required exactly 2 persons.
    persons = models.ManyToManyField(User, related_name='relationship')
    level = models.CharField(max_length=2, choices=RELATION_LEVELS)
    created_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='relation_reporter')

    def __str__(self):
        return 'Relationships of {} and {} is {}'.format(
            self.persons.first(), self.persons.last(), self.get_level_display()
        )