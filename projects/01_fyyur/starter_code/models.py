
from flask_sqlalchemy import SQLAlchemy

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#
db = SQLAlchemy()

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

    #Les champs manquants nommés suivant leurs noms sur les pages de détail ou d'ajout de l'application web

    genres = db.Column(db.ARRAY(db.String()))
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(255))

    # Champs qui me permettra de parcourir la liste des shows pour les afficher dans la page de détail d'un 'venue'

    #l'attribut cascade a été défini pour que les shows soient supprimés lorsque leur 'venue' est supprimé pour éviter une erreur de clé étrangère
    #Ajouté dans le cadre du challenge BONUS pour l'ajout d'un bouton de suppression d'un 'venue'

    venue_shows = db.relationship('Show', back_populates='venue', cascade="all, delete", lazy=True)


class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.ARRAY(db.String()))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

    #Les champs manquants nommés suivant leurs noms sur les pages de détail ou d'ajout de l'application web
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(255))

    # Champs qui me permettra de parcourir la liste des shows pour les afficher dans la page de détail d'un artiste donné

    artist_shows = db.relationship('Show', back_populates='artist', lazy=True)


# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = 'Show'

    #Les champs manquants nommés suivant leurs noms sur les pages de détail ou d'ajout de l'application web

    id = db.Column(db.Integer, primary_key=True)
    start_date = db.Column(db.DateTime, nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('Artist.id'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)  
    artist = db.relationship('Artist', back_populates='artist_shows', lazy=True)
    venue = db.relationship('Venue', back_populates='venue_shows', lazy=True)

