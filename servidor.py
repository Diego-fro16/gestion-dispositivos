from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada (en memoria)
dispositivos = [
    {"id": 1, "name": "Router 1", "type": "Router", "status": "active"},
    {"id": 2, "name": "Switch 1", "type": "Switch", "status": "inactive"}
]

# Endpoint para listar dispositivos (GET)
@app.route('/api/devices', methods=['GET'])
def listar_dispositivos():
    return jsonify(dispositivos), 200

# Endpoint para agregar un dispositivo (POST)
@app.route('/api/devices', methods=['POST'])
def agregar_dispositivo():
    data = request.get_json()  # Obtiene los datos del cliente
    nuevo_dispositivo = {
        "id": len(dispositivos) + 1,  # Asigna un nuevo ID
        "name": data["name"],
        "type": data["type"],
        "status": data["status"]
    }
    dispositivos.append(nuevo_dispositivo)  # Agrega el dispositivo a la lista
    return jsonify(nuevo_dispositivo), 201  # Devuelve el nuevo dispositivo con status 201

# Endpoint para actualizar un dispositivo (PUT)
@app.route('/api/devices/<int:id>', methods=['PUT'])
def actualizar_dispositivo(id):
    data = request.get_json()
    for dispositivo in dispositivos:
        if dispositivo["id"] == id:
            dispositivo["name"] = data["name"]
            dispositivo["type"] = data["type"]
            dispositivo["status"] = data["status"]
            return jsonify(dispositivo), 200
    return jsonify({"error": "Dispositivo no encontrado"}), 404  # Si no se encuentra el dispositivo

# Endpoint para eliminar un dispositivo (DELETE)
@app.route('/api/devices/<int:id>', methods=['DELETE'])
def eliminar_dispositivo(id):
    global dispositivos
    dispositivos = [dispositivo for dispositivo in dispositivos if dispositivo["id"] != id]  # Elimina el dispositivo
    return jsonify({"message": "Dispositivo eliminado"}), 204  # 204 No content, porque no devuelve cuerpo

# Iniciar el servidor
if __name__ == '__main__':
    app.run(debug=True)
