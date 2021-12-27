import os
from datetime import datetime
from config import db
from models import Directors, Movies

# # Data to initialize database with
FINAL_PROJ = []
# PEOPLE = [
#     {
#         "fname": "Raka",
#         "lname": "Ardhi",
#         "notes": [
#             ("Cool, a Hacktiv8 mini-blogging application!", "2019-01-06 22:17:54"),
#             ("This could be useful", "2019-01-08 22:17:54"),
#             ("Well, sort of useful", "2019-03-06 22:17:54"),
#         ],
#     },
#     {
#         "fname": "Rinintha",
#         "lname": "Anggie",
#         "notes": [
#             (
#                 "I'm going to make really profound observations",
#                 "2019-01-07 22:17:54",
#             ),
#             (
#                 "Maybe they'll be more obvious than I thought",
#                 "2019-02-06 22:17:54",
#             ),
#         ],
#     },
#     {
#         "fname": "Safran",
#         "lname": "Wijaya",
#         "notes": [
#             ("Has anyone seen my eggs?", "2019-01-07 22:47:54"),
#             ("I'm really late delivering these!", "2019-04-06 22:17:54"),
#         ],
#     },
# ]

# Delete database file if it exists currently
if os.path.exists('final_proj.db'):
    os.remove('final_proj.db')

# Create the database
db.create_all()

# Iterate over the PEOPLE structure and populate the database
for person in FINAL_PROJ:
    p = Person(lname=person.get("lname"), fname=person.get("fname"))

    # # Add the notes for the person
    # for note in person.get("notes"):
    #     content, timestamp = note
    #     p.notes.append(
    #         Note(
    #             content=content,
    #             timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
    #         )
    #     )
    db.session.add(p)

db.session.commit()