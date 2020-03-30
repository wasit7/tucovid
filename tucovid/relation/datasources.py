def map_relation(relation, current_user):
    return {
        'id': relation.pk,
        'other_person': relation.persons.exclude(pk=current_user.pk).first().profile.full_name,
        'level': relation.get_level_display()
    }
