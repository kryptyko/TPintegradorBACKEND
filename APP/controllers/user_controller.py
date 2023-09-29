from flask import request, session
from ..models.user_model import User
from flask import jsonify
class UserController:
    @classmethod
    def get(cls):
        users =[]
        for user in User.get():
            users.append(user.serialize())
        return users, 200
    @classmethod
    def get_by_id(cls, user_id):
        user=User(user_id=user_id)
        user = User.get(user)
        print(user)
        if user:
            return user.serialize(), 200
    @classmethod
    def create(cls):
        data = request.get_json()
        user = User(
            username=data.get("username"),
            password=data.get("password"),
            email=data.get("email"),
            profile_image=data.get("profile_image"),
        )
        User.create(user)
        return {"message": "Usuario creado Correctamente"}, 201
    @classmethod
    def update(cls, user_id):
        data = request.get_json()
        user = User( 
            user_id=user_id,
            username=data.get("username"),
            password=data.get("password"),
            email=data.get("email"),
            profile_image=data.get("profile_image"),
        )
        User.update(user)
        return {"message": "Usuario Actualizado Correctamente"}, 200
    @classmethod
    def delete(cls, user_id):
        user = User(user_id=user_id)
        User.delete(user)
        return {"message": "Usuario borrado correctamente"},200
    @classmethod
    def get_servers(cls,user_id):
        user = User(user_id=user_id)
        servers=[]
        for server_data in User.get_servers(user):
            #print(server)
            #servers.append(server.serialize())
            server = {
                "id_servidor": server_data[0],
                "nombre_servidor": server_data[1],
                "descripcion_servidor": server_data[2]
            }
            servers.append(server)
        return jsonify(servers),200
    @classmethod
    def login(cls):
        data=request.json
        user = User(
            username=data.get("username"),
            password=data.get("password"),
        )
        print (user.serialize())
        user = User.login(user)
        if user:
            session["user_id"] = user.user_id
            session[ "username"]=user.username
            session["email"]=user.email
            session["profile_image"] = user.profile_image
            return user.serialize(),200
        return {"message":"Invalid credentials"}, 401
    