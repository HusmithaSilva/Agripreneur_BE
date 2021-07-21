from extensions import mongo, db
from Main import app

# from flask import Blueprint


from flask import Response, request

# import pymongo
import json
from bson.objectid import ObjectId

# main = Blueprint('main', __name__)

# ====Routes====
# ====post users====
@app.route("/users", methods=["POST"])
def create_user():
    try:
        user = {"name": request.form["name"], 
                "email": request.form["email"], 
                "password": request.form["password"], 
                "district": request.form["district"]}
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        return Response(
            response= json.dumps({"message": "user created", 
            "id": f"{dbResponse.inserted_id}"}),
            status=200,

        )
    except Exception as Ex:   
        print("**********") 
        print(Ex)
        return Response(
            response= json.dumps({"message": "cannot read user"}),
            status=500,

        )


# ====Routes====
# ====Get users====
@app.route("/getUsers", methods=["GET"])
def get_some_users():
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"] = str(user["_id"])

        return Response(
            response= json.dumps(data),
            status=200,

        )

    except Exception as Ex:   
        print("**********") 
        print(Ex)


# ====Routes====
# ====update user====

@app.route("/updateUsers/<id>", methods=["PUT"])
def update_user(id):
    try:
        dbResponse = db.users.update_one(
            {"_id": ObjectId(id)},
            {"$set": {"name": request.form["name"]}}
        )
        # for attr in dir(dbResponse):
        #     print(f"{attr}")

        print(dbResponse.upserted_id)
        return Response(
            response= json.dumps({"message": "updated user"}),
            status=200,

        )
    except Exception as Ex:   
        print("**********") 
        print(Ex)
        return Response(
            response= json.dumps({"message": "cannot update user"}),
            status=500,

        )



# ====Routes====
# ====delete user====

@app.route("/deleteUsers/<id>", methods=["DELETE"])
def delete_user(id):
    try:
        dbResponse = db.users.delete_one({"_id": ObjectId(id)},)

        return Response(
            response= json.dumps({"message": "user deleted", "id": f"{id}"}),
            status=200,

        )  

    except Exception as Ex:   
        print("**********") 
        print(Ex)
        return Response(
            response= json.dumps({"message": "cannot delete user"}),
            status=500,

        )    
