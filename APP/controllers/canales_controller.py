from flask import request, jsonify
from APP.database import DatabaseConnection
from APP.models.canales_models import Canal  # Importa el modelo Canal

class CanalesController:
    @staticmethod
    def get(cls):
        canal=Canal(server_id=request.args.get("server_id"))
        canales=[]
        if canal.server_id is None:
            for canal in canal.get():
                canales.append(canal.serialize())
            else:
                for canal in Canal.get_canales_by_server(canal):
                    canales.append(canal.serialize())
        return canales, 200

    
    
    @staticmethod
    def get_by_id(canales_id):
        result = Canal.get_by_id(canales_id)

        # Construye la lista de canales en formato JSON
        canales_json = []
        for row in result:
            canal_json = {
                "id_canal": row[0],
                "nombre_canal": row[1],
                "descripcion_canal": row[2],
                "canales_servidor": row[3]
            }
            canales_json.append(canal_json)

        return canales_json, 200

    @staticmethod
    def create():
        canalesnombre = request.json['canalesnombre']
        canalesdescripcion = request.json['canalesdescripcion']
        canalesservidor = request.json['canalesservidor']
        canalescreado_por = request.json['canalescreado_por']

        # Crear una instancia del modelo Canal
        nuevo_canal = Canal(None, canalesnombre, canalesdescripcion, canalesservidor, canalescreado_por)

        # Llamada a la API para invocar el método create del controlador
        try:
            # Suponiendo que tienes un método en DatabaseConnection para crear un canal
            nuevo_canal_id = ""
            return f'Canal creado con ID: {nuevo_canal_id}', 201
        except Exception as e:
            return f'Error al crear el canal: {str(e)}', 500

    @staticmethod
    def update(canalesid):
        updated_data = request.json
        query = "UPDATE canales SET canalesnombre=%s, canalesdescripcion=%s, canalesservidor=%s, canalescreado_por=%s WHERE canalesid=%s"
        params = (updated_data['canalesnombre'], updated_data['canalesdescripcion'], updated_data['canalesservidor'], updated_data['canalescreado_por'], canalesid)
        #DatabaseConnection.execute_query(query, params)

        return 'Canal actualizado', 200

    @staticmethod
    def delete(canalesid):
        query = "DELETE FROM canales WHERE canalesid = %s"
        params = (canalesid,)
        #DatabaseConnection.execute_query(query, params)

        return 'Canal eliminado', 200
    
    @classmethod
    def get_canales(cls,canal_id):
        canal = Canal(canal_idd=canal_id)
        canales=[]
        for canal_data in Canal.get_canales(canal):
            #print(server)
            #servers.append(server.serialize())
            canal = {
                "id_canal": canal_data[0],
                "nombre_canal": canal_data[1],
                "descripcion_canal": canal_data[2]
            }
            canales.append(canal)
        return jsonify(canales),200