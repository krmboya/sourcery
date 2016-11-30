# -*- coding: utf-8 -*-
import entities

def list_local_activity(location_id, **kwargs):

    location_repo = kwargs.get('location_repo')
    activity_repo = kwargs.get('activity_repo')

    location = location_repo.get_by_id(location_id)
    local_activities = activity_repo.filter_by(location)
    return local_activities

