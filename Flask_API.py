from flask import Flask , request
from flask.json import jsonify

app = Flask(__name__)


#get POST put # delete
#host status
@app.route("/")
def host_status():
    return{"host":"on"}


#get
user_list = [
    {"username":"TOM",
    "password":"324"},
    {"username":"AA",
    "password":"efc"}
    ]

@app.route("/users",methods = ["GET"])
def get_user_list():
    return jsonify(user_list)


#post 
# @app.route("/users", methods = ["POST"])
# def create_user():
#     user = request.get_json()
#     if user["username"] not in [item["username"] for item in user_list]:
#         user_list.append(user)
#         return jsonify({"message":"user create Success"})
#     return jsonify({"message":"user exists!"})
#     # print(user)

@app.route("/users", methods = ["POST"])
def create_user():
    user = request.get_json()
    for item in user_list:
        if item["username"] == user["username"]:
            return jsonify({"message":"user exists!"})
    user_list.append(user)           
    return jsonify({"message":"user create Success"})
    # print(user)


#delete
# @app.route("/users/<username>", methods = ["DELETE"])
# def delete_user(username):
#     for item in user_list:
#         if item["username"] == username:
#             user_list.remove(item)
#             return jsonify({"message":"user delete"})
#     return jsonify({"message":"user not found!!"})

#put
# @app.route("/users/<username>", methods = ["PUT"])
# def put_user_paswword(username):
#     user = request.get_json()
#     for item in user_list:s
#         if item["username"] == username:
#             item["password"] = user["password"]
#             return jsonify({"message":"user password update"})
#     return jsonify({"message":"user not found!!"})


# put delete
@app.route("/users/<username>", methods = ["PUT","DELETE"])
def delete_put_user_paswword(username):
    user = request.get_json()
    for item in user_list:
        if item["username"] == username:
            if request.method == "PUT":
                item["password"] = user["password"]
                return jsonify({"message":"user password update"})
            elif request.method == "DELETE":
                user_list.remove(item)
                return jsonify({"message":"user delete"})
    return jsonify({"message":"user not found!!"})



        




if __name__ == "__main__":
    app.run()