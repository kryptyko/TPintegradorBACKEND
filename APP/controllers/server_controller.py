from flask import request, session
from ..models.server_model import Server
#este controller hay q modificar e implementar las mismas funciones que tiene el user controller (get, create, delete)
#lo mismo para user_model
class ServerController:
    @classmethod
    def get(cls):
        servers =[]
        for servers in Server.get():
            servers.append(servers.serialize())
        return servers, 200
    @classmethod
    def get_by_id(cls, user_id):
        user=Server(user_id=user_id)
        user = Server.get(user)
        print(user)
        if user:
            return user.serialize(), 200
    @classmethod
    def create(cls):
        data = request.get_json()
        user = Server(
            username=data.get("username"),
            password=data.get("password"),
            email=data.get("email"),
            profile_image=data.get("profile_image"),
        )
        Server.create(user)
        return {"message": "Usuario creado Correctamente"}, 201
    @classmethod
    def update(cls, user_id):
        data = request.get_json()
        user = Server( 
            user_id=user_id,
            username=data.get("username"),
            password=data.get("password"),
            email=data.get("email"),
            profile_image=data.get("profile_image"),
        )
        Server.update(user)
        return {"message": "Usuario Actualizado Correctamente"}, 200
    @classmethod
    def delete(cls, user_id):
        user = Server(user_id=user_id)
        Server.delete(user)
        return {"message": "Usuario borrado correctamente"},200
    @classmethod
    def get_servers(cls,user_id):
        user = Server(user_id=user_id)
        servers=[]
        for server in Server.get_servers(user):
            print(server)
            servers.append(server.serialize())
        return servers,200
    