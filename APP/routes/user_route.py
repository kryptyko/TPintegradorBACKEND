from flask import Blueprint
from ..controllers.user_controller import UserController


bp_users= Blueprint("users",__name__)
bp_users.route("/", methods=["GET"])(UserController.get)
bp_users.route("/<int:user_id>", methods=["GET"])(UserController.get_by_id)
bp_users.route("/", methods=["POST"])(UserController.create)
bp_users.route("/<int:user_id>", methods=["PUT"])(UserController.update)
bp_users.route("/<int:user_id>", methods=["DELETE"])(UserController.delete)
bp_users.route("/<int:user_id>/servers", methods=["GET"])(UserController.get_servers)
bp_users.route("/login", methods=["POST"])(UserController.login)



