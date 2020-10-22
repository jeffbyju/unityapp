from flask import Flask, jsonify
import pymysql
import json
from flask_cors import *

app = Flask(__name__)
cors = CORS(app)

db = pymysql.connect("us-cdbr-east-02.cleardb.com", "b9f8d376f99bb0",
                     "8e6fda48", "heroku_3e48eb031aa9cd3")

cursor = db.cursor()


@app.route("/")
def index():
    script = 'select * from users;'
    cursor.execute(script)
    users = cursor.fetchall()
    Users = []
    for i in range(len(users)):
        Id, username, password = users[i]
        user = User(username, password)
        Users.append(user.__dict__)
        #json.dumps(user,indent=4,cls=UserEncoder)
    return json.dumps(Users)
    # return jsonify(data=cursor.fetchall())


if __name__ == "__main__":
    app.run(debug=True)