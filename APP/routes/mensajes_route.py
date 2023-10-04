from flask import Blueprint
from ..controllers.mensajes_controller import MensajesController
bp_mensajes = Blueprint("mensajes", __name__)

bp_mensajes.route("/<int:canal_id>/mensajes", methods=["GET"])(MensajesController.get_by_id)
bp_mensajes.route("/", methods=["POST"])(MensajesController.create)