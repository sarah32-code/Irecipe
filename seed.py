import os

# Drop and recreate database
os.system(f'dropdb technoapp --if-exists')
os.system(f'createdb technoapp')

from model import db, connect_to_db
import server

# Connect app to database
connect_to_db(server.app)

# Updates the database schema
db.create_all()