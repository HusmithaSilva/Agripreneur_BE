from extensions import mongo, db, check_for_token
from Main import app
# from flask import Blueprint

from flask import Response, request, session

# import pymongo
import json
from bson.objectid import ObjectId
import jwt

# ====Routes====
# ====Get users====
@app.route("/auth")
@check_for_token
def authorized():
        return Response(
            response= json.dumps({"message": "Can access by authorized users"}),
            status=200,

        )

# public route
@app.route("/public")
def public():
        return Response(
            response= json.dumps({"message": "Can access by any users"}),
            status=200,

        )

#login routes 
@app.route("/login", methods=["POST"])
def login():

        if request.form['email'] and request.form["password"] == 'password':
            session['user'] = request.form['email']
            token = jwt.encode({
                'user': request.form['email']
            }, 'app.SECRET_KEY')
            return Response(
                response=json.dumps({"token": token} )
            )
            
        return Response(
            response= json.dumps({"message": "login failed"}),
            status=400,

        )