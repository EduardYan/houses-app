"""
This file have somes configurations
for the app, like the path to sqlite.
"""

from dotenv import load_dotenv
from os import environ

load_dotenv() # loading


# getting
PATH = environ['SQLITE_PATH']
SQLITE_PATH = f'sqlite:///{PATH}'