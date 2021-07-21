# mongoDB

import pymongo
from flask import Response, request
import json
from functools import wraps
from bson.objectid import ObjectId
import jwt

try:
    mongo = pymongo.MongoClient(host="localhost", port=27017)
    db = mongo.company
except:
    print("cannot connect to db")


# JWT config
def check_for_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
            token = request.args.get('Token')
            print(token)
            if not token:
                return Response(
                response= json.dumps({"message": "Missing token"}),
                status=200,
            )
            try:
                data=jwt.decode(token, 'app.SECRET_KEY', ['HS256'])
                return Response(
                response= json.dumps({"message": data}),
                status=200,
                )
            except:
                return Response(
                response= json.dumps({"message": "invalid token"}),
                status=200,
                )              
            return func(*args, **kwargs)
    return wrapped

    
        
