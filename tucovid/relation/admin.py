from django.contrib import admin
from relation.models import Relationship, Event

@admin.register(Relationship)
class RelationshipAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'first_person',
        'second_person',
        'level',
        'created_date',
        'created_by',
    ]

    def first_person(self, obj):
        return obj.persons.first()
    
    def second_person(self, obj):
        return obj.persons.last()

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'start',
        'finish',
        'localtion',
        'reporter',
        'created_date',
        'created_by',
    ]
