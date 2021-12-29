"""
This is the people module and supports all the REST actions for the
people data
"""

from flask import make_response, abort
from sqlalchemy import desc, func, text, asc
from config import db
from models import Directors, DirectorsSchema, Movies


def read_all():
    """
    This function responds to a request for /api/directors
    with the complete lists of directors
    :return:        json string of list of directors
    """
    # Create the list of directors from our data
    directors = Directors.query.order_by(Directors.id).limit(50)
    # .all()

    # Serialize the data for the response
    directors_schema = DirectorsSchema(many=True)
    data = directors_schema.dump(directors)
    return data


def read_one(id):
    """
    This function responds to a request for /api/directors/{id}
    with one matching directors from directors
    :param id:   ID of directors to find
    :return:            directors matching id
    """
    # Build the initial query
    directors = (
        Directors.query.filter(Directors.id == id)
        .outerjoin(Movies)
        .one_or_none()
    )

    # Did we find a directors?
    if directors is not None:

        # Serialize the data for the response
        directors_schema = DirectorsSchema()
        data = directors_schema.dump(directors)
        return data

    # Otherwise, nope, didn't find that directors
    else:
        abort(404, f"Directors not found for ID: {id}")


def create(directors):
    """
    This function creates a new directors in the people structure
    based on the passed in directors data
    :param directors:  directors to create in people structure
    :return:        201 on success, 406 on directors exists
    """
    id = directors.get("id")

    existing_directors = (
        Directors.query.filter(Directors.id == id)
        .one_or_none()
    )

    # Can we insert this directors?
    if existing_directors is None:

        # Create a directors instance using the schema and the passed in directors
        schema = DirectorsSchema()
        new_directors = schema.load(directors, session=db.session)

        # Add the directors to the database
        db.session.add(new_directors)
        db.session.commit()

        # Serialize and return the newly created directors in the response
        data = schema.dump(new_directors)

        return data, 201

    # Otherwise, nope, directors already exists
    else:
        abort(409, f"Directors with ID {id} already exists")


def update(id, directors):
    """
    This function updates an existing directors in the people structure
    :param id       : ID of the directors to update in the people structure
    :param directors: directors to update
    :return         : updated directors structure
    """
    # Get the directors requested from the db into session
    update_directors = Directors.query.filter(
        Directors.id == id
    ).one_or_none()

    # Did we find an existing directors?
    if update_directors is not None:

        # turn the passed in directors into a db object
        schema = DirectorsSchema()
        update = schema.load(directors, session=db.session)

        # Set the id to the directors we want to update
        update.id = update_directors.id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated directors in the response
        data = schema.dump(update_directors)

        return data, 200

    # Otherwise, nope, didn't find that directors
    else:
        abort(404, f"Directors not found for ID: {id}")


def delete(id):
    """
    This function deletes a directors from the people structure
    :param id:   ID of the directors to delete
    :return:            200 on successful delete, 404 if not found
    """
    # Get the directors requested
    directors = Directors.query.filter(Directors.id == id).one_or_none()

    # Did we find a directors?
    if directors is not None:
        db.session.delete(directors)
        db.session.commit()
        return make_response(f"Directors with ID {id} has been deleted", 200)

    # Otherwise, nope, didn't find that directors
    else:
        abort(404, f"Directors not found for ID: {id}")

def read_by_name(director_name):
    """
    This function responds to a request for /api/directors/{director_name}
    with one matching directors from directors
    :param id:   ID of directors to find
    :return:            directors matching id
    """
    # Build the initial query
    search = "%{}%".format(director_name)
    directors = (
        Directors.query.filter(Directors.name.like(search)).all()
    )

    # Did we find a directors?
    if directors is not None:

        # Serialize the data for the response
        directors_schema = DirectorsSchema(many=True)
        data = directors_schema.dump(directors)
        return data

    # Otherwise, nope, didn't find that directors
    else:
        abort(404, f"Directors not found for name that has {director_name}")

def read_most_movies():
    """
    This function responds to a request for /api/directors/{director_name}
    with one matching directors from directors
    :param id:   ID of directors to find
    :return:            directors matching id
    """
    # Build the initial query
    func_count = func.count(Movies.id)
    directors = (
        Directors.query.select_from(Directors)
        .join(Movies, Directors.id == Movies.director_id)
        .group_by(Directors.id)
        .having(func.count(Movies.id))
        .order_by(desc(func_count), asc(Directors.name))
        .limit(10)
    )

    # Serialize the data for the response
    directors_schema = DirectorsSchema(many=True)
    data = directors_schema.dump(directors)
    return data