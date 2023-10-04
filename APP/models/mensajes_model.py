from APP.database import DatabaseConnection

class Mensajes:
    def __init__(self, id_mensaje, contenido_mensaje, usuario_mensaje, mensaje_canal, fechahora_mensaje):
        self.id_mensaje = id_mensaje
        self.contenido_mensaje = contenido_mensaje
        self.usuario_mensaje = usuario_mensaje
        self.mensaje_canal = mensaje_canal
        self.fechahora_mensaje = fechahora_mensaje

    def serialize(self):
        return {
            'mensajesid': self.id_mensaje,
            'mensajescontenido': self.contenido_mensaje,
            'mensajesusuario': self.usuario_mensaje,
            'mensajescanal': self.mensaje_canal,
            'mensajefechahora': self.fechahora_mensaje
        }
        
    @classmethod
    def create(cls, mensajes):
        query = """INSERT INTO disgord.mensajes (mensajescontenido, mensajesusuario , mensajescanal, mensajefechahora) VALUES (%(contenido_mensaje)s, %(usuario_mensaje)s, %(mensaje_canal)s, %(fechahora_mensaje)s)"""
        params = mensajes.__dict__
        DatabaseConnection.execute_query(query, params)

    @classmethod
    def get_by_id(cls, canales_id):
        # Realiza la consulta SQL para obtener los mensajes por Id del canal
        query = f"SELECT mensajesid, mensajescontenido, mensajesusuario , mensajescanal, mensajesfechahora FROM disgord.mensajes WHERE mensajescanal = {canales_id}"
        result = DatabaseConnection.fetch_all(query)

        return result