from flask import Blueprint
from ..controllers.server_controller import Server

bp_servers= Blueprint("servers",__name__)
bp_servers.route("/", methods=["GET"])(Server.get)
#bp_servers.route("/<int:user_id>", methods=["GET"])(Server.get_by_id)