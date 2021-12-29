"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from sqlalchemy import desc
from config import db
from models import Directors, Movies, MoviesSchema


def read_all():
    """
    This function responds to a request for /api/directors/movies
    with the complete list of movies, sorted by note timestamp
    :return:                json list of all movies for all directors
    """
    # Query the database for all the movies
    movies = Movies.query.order_by(Movies.id).limit(1000)
    # .all()

    # Serialize the list of movies from our data
    movies_schema = MoviesSchema(many=True)
    data = movies_schema.dump(movies)
    return data


def read_one(director_id, id):
    """
    This function responds to a request for
    /api/directors/director_id/movies/id
    with one matching movies for the associated directors
    :param id: Id of directors the movies is related to
    :param id: Id of the movies
    :return:   json string of movies contents
    """
    # Query the database for the movies
    movies = (
        Movies.query.join(Directors, Directors.id == Movies.director_id)
        .filter(Directors.id == director_id)
        .filter(Movies.id == id)
        .one_or_none()
    )

    # Was a movies found?
    if movies is not None:
        movies_schema = MoviesSchema()
        data = movies_schema.dump(movies)
        return data

    # Otherwise, nope, didn't find that movies
    else:
        abort(404, f"Movies not found for Id: {id}")


def create(director_id, movies):
    """
    This function creates a new movies related to the passed in directors id.
    :param id    : Id of the directors the movies is related to
    :param movies: The JSON containing the movies data
    :return      : 201 on success
    """
    # get the parent directors
    directors = Directors.query.filter(Directors.id == director_id).one_or_none()

    # Was a person found?
    if directors is None:
        abort(404, f"Directors not found for Id: {director_id}")

    id = movies.get("id")

    existing_movies = (
        Movies.query.filter(Movies.id == id)
        .one_or_none()
    )

    # Can we insert this movies?
    if existing_movies is None:

        # Create a movies schema instance
        schema = MoviesSchema()
        new_movies = schema.load(movies, session=db.session)

        # Add the movies to the person and database
        directors.movies.append(new_movies)
        db.session.commit()

        # Serialize and return the newly created movies in the response
        data = schema.dump(new_movies)

        return data, 201

    # Otherwise, nope, movies already exists
    else:
        abort(409, f"Movies with ID {id} already exists")


def update(director_id, id, movies):
    """
    This function updates an existing movies related to the passed in
    directors id.
    :param director_id: Id of the directors the movies is related to
    :param id         : Id of the movies to update
    :param content    : The JSON containing the movies data
    :return           : 200 on success
    """
    update_movies = (
        Movies.query.filter(Directors.id == director_id)
        .filter(Movies.id == id)
        .one_or_none()
    )

    # Did we find an existing movies?
    if update_movies is not None:

        # turn the passed in movies into a db object
        schema = MoviesSchema()
        update = schema.load(movies, session=db.session)

        # Set the id's to the movies we want to update
        update.director_id = update_movies.director_id
        update.id = update_movies.id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated movies in the response
        data = schema.dump(update_movies)

        return data, 200

    # Otherwise, nope, didn't find that movies
    else:
        abort(404, f"Movies not found for Id: {id}")


def delete(director_id, id):
    """
    This function deletes a movies from the movies structure
    :param director_id: Id of the person the movies is related to
    :param id         : Id of the movies to delete
    :return           : 200 on successful delete, 404 if not found
    """
    # Get the movies requested
    movies = (
        Movies.query.join(Directors, Directors.id == Movies.director_id)
        .filter(Directors.id == director_id)
        .filter(Movies.id == id)
        .one_or_none()
    )

    # did we find a movies?
    if movies is not None:
        db.session.delete(movies)
        db.session.commit()
        return make_response(
            "Movies with ID {id} deleted".format(id=id), 200
        )

    # Otherwise, nope, didn't find that movies
    else:
        abort(404, f"Movies not found for ID: {id}")

def read_most_popular():
    """
    This function responds to a request for /api/directors/movies
    with the complete list of movies, sorted by note timestamp
    :return:                json list of all movies for all directors
    """
    # Query the database for all the movies
    movies = Movies.query.order_by(desc(Movies.popularity)).limit(10)
    # .all()

    # Serialize the list of movies from our data
    movies_schema = MoviesSchema(many=True)
    data = movies_schema.dump(movies)
    return data

def read_most_budget():
    """
    This function responds to a request for /api/directors/movies
    with the complete list of movies, sorted by note timestamp
    :return:                json list of all movies for all directors
    """
    # Query the database for all the movies
    movies = Movies.query.order_by(desc(Movies.budget)).limit(10)
    # .all()

    # Serialize the list of movies from our data
    movies_schema = MoviesSchema(many=True)
    data = movies_schema.dump(movies)
    return data

def read_most_revenue():
    """
    This function responds to a request for /api/directors/movies
    with the complete list of movies, sorted by note timestamp
    :return:                json list of all movies for all directors
    """
    # Query the database for all the movies
    movies = Movies.query.order_by(desc(Movies.revenue)).limit(10)
    # .all()

    # Serialize the list of movies from our data
    movies_schema = MoviesSchema(many=True)
    data = movies_schema.dump(movies)
    return data

def read_most_vote_average():
    """
    This function responds to a request for /api/directors/movies
    with the complete list of movies, sorted by note timestamp
    :return:                json list of all movies for all directors
    """
    # Query the database for all the movies
    movies = Movies.query.order_by(desc(Movies.vote_average),desc(Movies.vote_count)).limit(10)
    # .all()

    # Serialize the list of movies from our data
    movies_schema = MoviesSchema(many=True)
    data = movies_schema.dump(movies)
    return data


