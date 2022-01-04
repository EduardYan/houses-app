"""
This file have the router
for visit in the server.
"""

from flask import Blueprint, render_template, redirect, url_for, request, flash
from utils.db import db
from models.house import Houses

houses = Blueprint('houses', __name__)

@houses.route('/')
def home():
  """
  This is the principal route
  for the server.

  """

  return render_template('index.html')

@houses.route('/about')
def about():
  """
  Show the about page.
  """

  return render_template('about.html')

@houses.route('/more')
def more():
  """
  Render the page for more.
  """

  # getting the info for show
  houses = Houses.query.all()
  quantity = len(houses)

  # in case not houses yet, raise IndexError
  try:
    last = houses[len(houses) - 1].location

    return render_template('more.html', quantity = quantity, last = last)

  except IndexError:
    return render_template('more.html')

@houses.route('/view')
def view():
  """
  This route show the houses
  in the database, consulting
  to database.
  """

  # gettings houses for show
  houses = Houses.query.all()

  return render_template('view.html', houses = houses)

@houses.route('/add-house', methods = ['POST'])
def add():
  """
  This route is for add a new
  house in the database.
  """

  # getting values and adding
  location = request.form['location']
  price = int(request.form['price'])

  house =Houses(location, price)

  db.session.add(house)
  db.session.commit()

  flash('House Added Succesfully')

  return redirect(url_for('houses.view'))

@houses.route('/delete-house/<id>')
def delete(id):
  """
  This route delete the house
  in the database, according to id
  passed for parameter.
  """

  house = Houses.query.get(id)
  db.session.delete(house)
  db.session.commit()

  flash('House Deleted Succesfully')

  return redirect(url_for('houses.view'))

@houses.route('/update-house/<id>', methods = ['GET', 'POST'])
def update(id):
  """
  Update the house in the database
  according to id passed for parameter.

  This route runnning with get and post, method
  if the method is get return the page.
  if not update the house. With the new data in post.
  """

  # getting the house for update
  house = Houses.query.get(id)

  # method
  if request.method == 'POST':
    # new values
    new_location = request.form['location']
    new_price = int(request.form['price'])

    house.location = new_location # chaning values
    house.price = new_price

    db.session.add(house)
    db.session.commit()

    flash(f'House with location {house.location} Updated Succesfully')


    return redirect(url_for('houses.view'))
  
  return render_template('update.html', house = house)

@houses.route('/disable/<id>')
def disable(id):
  """
  Disable the house changing the value in the
  database, according
  to id.
  """

  # getting and changing the value
  house = Houses.query.get(id)
  old_value = house.disable
  house.disable = not(house.disable)

  db.session.add(house)
  db.session.commit()

  if old_value == 1: # validating for show the message
    flash('House Available')

  else:
    flash('Home Disable')

  return redirect(url_for('houses.view'))
