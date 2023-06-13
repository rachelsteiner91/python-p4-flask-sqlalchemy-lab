from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

##The ZOOKEEPER model should contain a name, a birthday, and a list of animals that they take care of.
class Zookeeper(db.Model):
    __tablename__ = 'zookeepers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    birthday = db.Column(db.String)
##list of animals that they take care of
    animals = db.relationship('Animal', back_populates='zookeeper')

##The ENCLOSURE model should contain:
# environment (grass, sand, or water)
# an open_to_visitors boolean
#  and a list of animals.
class Enclosure(db.Model):
    __tablename__ = 'enclosures'

    id = db.Column(db.Integer, primary_key=True)
    environment = db.Column(db.String)
    open_to_visitors = db.Column(db.Boolean)

##list of animals relationship
    animals = db.relationship('Animal', back_populates='enclosure')

##The ANIMAL model should contain a name, a species, a zookeeper, and an enclosure.
class Animal(db.Model):
    __tablename__ = 'animals'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    species = db.Column(db.String)

    #FOREIGN KEY 
    #variable name make a column ()
    zookeeper_id = db.Column(db.Integer, db.ForeignKey('zookeepers.id'))
    enclosure_id = db.Column(db.Integer, db.ForeignKey('enclosures.id'))
    #RELATIONSHIP
    # the naimaal  zookeeper is accessed trhrough the Zookeeper class  and
    zookeeper = db.relationship('Zookeeper', back_populates='animals')
    enclosure = db.relationship('Enclosure', back_populates='animals')

# foreign key similar to which we can compare
#  zip  us together and l ook aat the whole piece 

