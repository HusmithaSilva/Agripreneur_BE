
from extensions import mongo, db
from Main import app
from flask import Response, request
# import pymongo
import json
from bson.objectid import ObjectId



@app.route("/points/<id>", methods=["POST"])
# @check_for_token
def add_points_earns(id):
    try:
        points = 42000
        earns = 25000

        user_earns = db.users.find_one({"_id": ObjectId(id)})
        # for user in user_earns:
        #     user["_id"] = str(user["_id"])
        print(user_earns)

        earnsData = {"earns": earns, 
                "points": points,
                "userID": user_earns}
        dbResponse = db.CropData.insert_one(earnsData)
        return Response(
            response= json.dumps({"message": "user points entered"}),
            status=200,

        )
    except Exception as Ex:   
        print("**********") 
        print(Ex)
        return Response(
            response= json.dumps({"message": "cannot read user"}),
            status=500,

        )



# @app.route("/getUsers", methods=["GET"])
# def get_some_users():
#     try:
#         data = list(db.users.find())
#         for user in data:
#             user["_id"] = str(user["_id"])

#         return Response(
#             response= json.dumps(data),
#             status=200,

#         )

#     except Exception as Ex:   
#         print("**********") 
#         print(Ex)
