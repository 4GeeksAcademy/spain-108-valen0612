from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        # do not serialize the password, its a secur 
        return { "id": self.id,
                 "email": self.email,
                 "is_active": self.is_active,
                 "post_to": [row.serialize() for row in self.post_to]}


class Posts(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String)
    body = db.Column(db.String)
    date = db.Column(db.Date, nullable=False)
    image_url = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_to = db.relationship('Users', back_populates="posts_to", lazy='select')

    def serialize(self):
        return { "id": self.id,
                 "title": self.title,
                 "description": self.description,
                 "body": self.body,
                 "date": self.date,
                 "image_url": self.image_url,
                 "coments_to": [row.serialize() for row in self.coments_to]}

class Media(db.Model):
    __tablename__ = 'media'
    id = db.Column(db.Integer, primary_key=True)
    media_type = db.Column(db.Enum('image', 'video', 'audio', name='media_type'), nullable=False)
    image_url = db.Column(db.String)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    post_to = db.relationship('Posts', back_populates="media_to", lazy='select')


class Coments(db.Model):
    __tablename__ = 'coments'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    user_to = db.relationship('Users', back_populates="coments_to", lazy='select')
    post_to = db.relationship('Posts', back_populates="coments_to", lazy='select')

    def serialize(self):
        return { "id": self.id,
                 "body": self.body,
                 "user_id": self.user_id,
                 "post_id": self.post_id}
   

class Followers(db.Model):
    __tablename__ = 'followers'
    id = db.Column(db.Integer, primary_key=True)
    following_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    following_to = db.relationship('Users', back_populates="followers_to", lazy='select')
    follower_to = db.relationship('Users', back_populates="followers_to", lazy='select')


class CharactersFavorites(db.Model):
    __tablename__ = 'characters_favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    character_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user_to = db.relationship('Users', back_populates="characters_favorites_to", lazy='select')
    character_to = db.relationship('Characters', back_populates="characters_favorites_to", lazy='select')


class PlanetsFavorites(db.Model):
    __tablename__ = 'planets_favorites'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    user_to = db.relationship('Users', back_populates="planets_favorites_to", lazy='select')
    planet_to = db.relationship('Planets', back_populates="planets_favorites_to", lazy='select')
    

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String , nullable=False , unique=True)
    height= db.Column(db.String , nullable=False)
    mass = db.Column(db.String , nullable=False)
    hair_color = db.Column(db.String , nullable=False)
    skin_color = db.Column(db.String , nullable=False)
    eye_color = db.Column(db.String , nullable=False)
    birth_year = db.Column(db.String , nullable=False)
    gender = db.Column(db.String , nullable=False)

    
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String , nullable=False , unique=True)
    diameter = db.Column(db.String , nullable=False)
    rotation_period = db.Column(db.String , nullable=False)
    orbital_period = db.Column(db.String , nullable=False)
    gravity = db.Column(db.String , nullable=False)
    population = db.Column(db.String , nullable=False)
    climate = db.Column(db.String , nullable=False)
    terrain = db.Column(db.String , nullable=False)

