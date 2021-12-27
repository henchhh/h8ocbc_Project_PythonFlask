from marshmallow import fields
from datetime import datetime
from config import db, ma

class Directors(db.Model): # directors table
    __tablename__ = 'directors'
    name = db.Column(db.Text)
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.Integer)
    uid = db.Column(db.Integer)
    department = db.Column(db.Text)
    movies = db.relationship(
        'Movies',
        backref='directors',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='asc(Movies.id)'
    )
    def __repr__(self):
        return f"Directors ( name: {self.name})"

class Movies(db.Model): # movies table
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    original_title = db.Column(db.Text)
    budget = db.Column(db.Integer)
    popularity = db.Column(db.Integer)
    release_date = db.Column(db.Text)
    revenue = db.Column(db.Integer)
    title = db.Column(db.Text)
    vote_average = db.Column(db.Float)
    vote_count = db.Column(db.Integer)
    overview = db.Column(db.Text)
    tagline = db.Column(db.Text)
    uid = db.Column(db.Integer)
    director_id = db.Column(db.Integer, db.ForeignKey('directors.id'))
    
    # , 

class DirectorsSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Directors
        # sqla_session = db.session
        load_instance = True

    movies = fields.Nested('DirectorsMoviesSchema', default=[], many=True)

class DirectorsMoviesSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    id = fields.Int()
    original_title = fields.Str()
    budget = fields.Int()
    popularity = fields.Int()
    release_date = fields.Str()
    revenue = fields.Int()
    title = fields.Str()
    vote_average = fields.Float()
    vote_count = fields.Int()
    overview = fields.Str()
    tagline = fields.Str()
    uid = fields.Int()
    director_id = fields.Int()

class MoviesSchema(ma.SQLAlchemyAutoSchema):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    class Meta:
        model = Movies
        # sqla_session = db.session
        load_instance = True
    
    directors = fields.Nested("MoviesDirectorsSchema", default=None)

class MoviesDirectorsSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    name = fields.Str()
    id = fields.Int()
    gender = fields.Int()
    uid = fields.Int()
    department = fields.Str()