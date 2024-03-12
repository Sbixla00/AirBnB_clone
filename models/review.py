#!/usr/bin/python3
""" state module """
from models.base_model import BaseModel


class Review(BaseModel):
    """ cls review """

    place_id = ""
    user_id = ""
    text = ""