#!/usr/bin/python3
"""This module defines a class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """This class defines a place by various attributes"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = ""
    longitude = ""
    amenity_ids = []
