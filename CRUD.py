from flask import Flask, request, jsonify
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config["MYSQL_PASSWORD"] = "Vidhu@123"
app.config["MYSQL_DB"]="user"
mysql=MySQL(app)

import json

class Object:
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4)
cur=None
# endpoint to create new user
@app.route("/user", methods=["POST"])
def add_user():
    request.get_json(force=True)
    global cur
    username = request.json['username']
    email = request.json['email']
    cur=mysql.connection.cursor()
    query="insert into user_de values (null,%s,%s)"
    data=[username,email]
    cur.execute(query,data)
    cur.connection.commit()
    cur.close()

    me = Object()
    me.name = username
    me.email=email
    return jsonify(me.toJSON())


# endpoint to show all users
@app.route("/user", methods=["GET"])
def get_user():
    cur = mysql.connection.cursor()
    cur.execute("select * from user_de")
    me = Object()
    me.name = cur.fetchall()
    return jsonify(me.toJSON())

# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    cur = mysql.connection.cursor()
    cur.execute("select * from user_de where id=\""+id+"\"")
    me = Object()
    me.name = cur.fetchall()

    return jsonify(me.toJSON())


#
#
# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    request.get_json(force=True)
    global cur

    cur = mysql.connection.cursor()
#    cur.execute("select * from user_detail where id=\"" + id + "\"")
    username = request.json['username']
    email = request.json['email']
    cur.execute("update user_de set username=\""+username+"\" , email=\""+email+"\" where id=\"" + id + "\"")
    cur.connection.commit()

    me = Object()
    me.name = username
    me.email = email
    cur.close()

    return jsonify(me.toJSON())


#
# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    cur = mysql.connection.cursor()
    cur.execute("delete from user_de where id=\""+id+"\"")
    cur.connection.commit()
    me = Object()
    return jsonify(me.toJSON())
#

if __name__ == '__main__':
    app.run(debug=True)
