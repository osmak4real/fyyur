from email.policy import default
from re import T
from flask_sqlalchemy import SQLAlchemy
import datetime
# from app import db

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False )
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500), nullable=True)
    facebook_link = db.Column(db.String(120), nullable=True)
    website_link = db.Column(db.String(120), nullable=True)
    seeking_talent = db.Column(db.Boolean, default=False, nullable=True)
    genres = db.Column(db.ARRAY(db.String), nullable=False)
    seeking_description = db.Column(db.String(500), nullable=True)
    shows = db.relationship('Show', backref='venue', lazy=True)
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

    def __repr__(self):
        return '<Venue {}>'.format(self.name)



class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), )
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    website_link = db.Column(db.String(120), nullable=True)
    seeking_venue = db.Column(db.Boolean, default=False, nullable=True)
    seeking_description = db.Column(db.String(500), nullable=True)
    shows = db.relationship('Show', backref='artist', lazy=True)
    # TODO: implement any missing fields, as a database migration using Flask-Migrate

    def __repr__(self):
        return '<Artist {}>'.format(self.name)

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

class Show(db.Model):
    __tablename__ = 'show'
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return '<Show {}{}>'.format(self.artist_id, self.venue_id)