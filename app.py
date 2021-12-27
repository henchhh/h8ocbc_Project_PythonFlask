"""
Main module of the server file
"""

# 3rd party moudles
from flask import render_template

# local modules
import config


# Get the application instance
connex_app = config.connex_app

# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml")
app = connex_app.app



# create a URL route in our application for "/"
@connex_app.route("/")
def home():
    """
    This function just responds to the browser URL
    localhost:5000/
    :return:        the rendered template "home.html"
    """
    return render_template("home.html")


if __name__ == "__main__":
    connex_app.run(debug=True)



# SQLLITE VIEW ALL DATA
# import sqlite3

# conn = sqlite3.connect('people.db')
# cur = conn.cursor()
# cur.execute('SELECT * FROM person ORDER BY lname')
# people = cur.fetchall()
# for person in people:
#     print(f'{person[2]} {person[1]}')    