from extensions import mongo, db
from Main import app
from flask import Response, request
# import pymongo
import json
from bson.objectid import ObjectId

import redis

redisClient = redis.Redis(host='localhost', port=6379, db=0)
print(redisClient)

# redisClient.set('key', 'hello there')
# value = redisClient.get('key')
# print(value)


@app.route("/getDetails", methods=["POST"])
def get_point_redis():

     players = "Players"

     # Add a player to the Redis sorted set against the score

    #  score1       = 56
    #  playerName1  = "Player1"


    #  score2       = 25
    #  playerName2  = "Player2"


    #  score3       = 37
    #  playerName3  = "Player3"
     
     #through loop zadd data with key value pairs to redis db

     user_earns = db.CropData.find()
     print(user_earns)
     for user in user_earns:
        user["_id"] = str(user["_id"])
        user["_id"] = str(user["userID"])
     print(user["_id"])

    #  for user in user_earns:
    #     user["_id"] = str(user["_id"])
    #     print(user["_id"])

        # redisClient.zadd(players, {playerName1: score1})



     print("Contents of the Redis sorted set with scores:")

    #  print(redisClient.zrange(players, 0, -1, desc=True, withscores=True))

     return Response(
            response= json.dumps({"message": "successfully sorted"}),
            status=200,

        )


# @app.route("/users", methods=["POST"])
# def create_user():
#     try:
#         user = {"name": request.form["name"], 
#                 "email": request.form["email"], 
#                 "password": request.form["password"], 
#                 "district": request.form["district"]}
#         dbResponse = db.users.insert_one(user)
#         print(dbResponse.inserted_id)
#         return Response(
#             response= json.dumps({"message": "user created", 
#             "id": f"{dbResponse.inserted_id}"}),
#             status=200,

#         )
#     except Exception as Ex:   
#         print("**********") 
#         print(Ex)
#         return Response(
#             response= json.dumps({"message": "cannot read user"}),
#             status=500,

#         )        


