from flask import request, jsonify
from APP.models.mensajes_model import Mensajes  # Importa el modelo Mensajes

class MensajesController:
    
    @staticmethod
    def get_by_id(canal_id):
        #mensajes=Mensajes(canal_id=canal_id)
        result = Mensajes.get_by_id(canal_id)

        # Construye la lista de mensajes en formato JSON
        mensajes_json=[]
        for row in result:
            mensaje_json = {
                "id_mensaje": row[0],
                "contenido_mensaje": row[1],
                "usuario_mensaje": row[2],
                "mensaje_canal": row[3],
                "fechahora_mensaje": row[4]
            }
            mensajes_json.append(mensaje_json)

        return jsonify(mensajes_json), 200

    @staticmethod
    def create():
        mensajescontenido = request.json['mensajescontenido']
        mensajesusuario = request.json['mensajesusuario']
        mensajescanal = request.json['mensajescanal']
        mensajefechahora = request.json['mensajefechahora']

        # Crear una instancia del modelo Mensajes
        nuevo_mensaje = Mensajes(None, mensajescontenido, mensajesusuario, mensajescanal, mensajefechahora)

        # Llamada a la API para invocar el método create del controlador
        try:
            # Suponiendo que tienes un método en DatabaseConnection para crear un canal
            nuevo_mensaje_id = ""
            return f'Mensaje creado con ID: {nuevo_mensaje_id}', 201
        except Exception as e:
            return f'Error al crear el Mensaje: {str(e)}', 500
