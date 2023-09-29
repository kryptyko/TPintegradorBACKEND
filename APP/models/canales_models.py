from APP.database import DatabaseConnection

class Canal:
    def __init__(self, id_canal, nombre_canal, descripcion_canal, canales_servidor):
        self.id_canal = id_canal
        self.nombre_canal = nombre_canal
        self.descripcion_canal = descripcion_canal
        self.canales_servidor = canales_servidor

    def serialize(self):
        return {
            'canalesid': self.canales_id,
            'canalesnombre': self.canales_name,
            'canalesdescripcion': self.canales_description,
            'canalesservidor': self.canales_server,
            'canalescreado_por': self.canales_creator
        }
        
    @classmethod
    def create(cls, canal):
        query = """INSERT INTO disgord.canales (canalesnombre, canalesdescripcion, canalesservidor , canalescreado_por) VALUES (%(canales_name)s, %(canales_description)s, %(canales_server)s, %(canales_creator)s)"""
        params = canal.__dict__
        DatabaseConnection.execute_query(query, params)
    @classmethod
    def get (cls, canal=None):
        if canal is not None and canal.canales_id is not None:
            query = """SELECT canalesid , canalesnombre, canalesdescripcion, canalesservidor , canalescreado_por FROM disgord.canales WHERE  canalservidor= %(canales_server)s"""
            params = canal.__dict__
            result = DatabaseConnection.fetch_one(query, params)
            if result:
                return cls(**dict(zip(cls._keys, result)))
            else:
                return None
        else:
            query = "SELECT canalesid , canalesnombre, canalesdescripcion, canalesservidor , canalescreado_por FROM disgord.canales"
            results = DatabaseConnection.fetch_all(query)
            users = []
            for row in results:
                users.append (cls(**dict(zip(cls._keys, row))))
            return users
        
    @classmethod
    def get_canales(cls,server):
        query = """SELECT canalesid , canalesnombre, canalesdescripcion, canalesservidor , canalescreado_por FROM disgord.canales WHERE  canalservidor= %(canales_server)s"""
        params = server.__dict__
        result = DatabaseConnection.fetch_all(query, params)
        
        if result:
            return result
        else:
            return None
        
    @classmethod
    def get_by_id(cls, canales_id):
        # Realiza la consulta SQL para obtener los canales por ID del servidor
        query = f"SELECT canalesid, canalesnombre, canalesdescripcion, canalesservidor, canalescreado_por FROM disgord.canales WHERE canalesservidor = {canales_id}"
        result = DatabaseConnection.fetch_all(query)

        return result
