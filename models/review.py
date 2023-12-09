#!/usr/bin/python3
"""Review class inhirit from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inhirit from BaseModel"""
    place_id = ''
    user_id = ''
    text = ''
