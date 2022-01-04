"""
This file have the class
for have a model of the house
in the database.
"""

from utils.db import db

class Houses(db.Model):
  """
  Model for the houses
  """
  # columns
  id = db.Column(db.Integer, primary_key = True)
  location = db.Column(db.String(60))
  price = db.Column(db.Integer)
  disable = db.Column(db.Boolean)

  def __init__(self, location:str, price:int):
    # values for the database

    self.location = location
    self.price = price
    self.disable = False