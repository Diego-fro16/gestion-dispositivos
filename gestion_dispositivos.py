import requests

# URL base de la API
BASE_URL = "http://127.0.0.1:5000/api/devices"

# Función para agregar un dispositivo (POST)
def agregar_dispositivo(data):
    print(f"Enviando solicitud POST a {BASE_URL} con los datos: {data}")
    response = requests.post(BASE_URL, json=data)
    print(f"[POST] Código de estado: {response.status_code}")
    if response.status_code == 201:  # Si la creación es exitosa
        dispositivo = response.json()  # Obtén la respuesta en formato JSON
        print("Dispositivo agregado correctamente.")
        print(f"Dispositivo agregado: {dispositivo}")
        return dispositivo
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Muestra el mensaje de error
        return None

# Función para listar dispositivos (GET)
def listar_dispositivos():
    print("\nListando dispositivos...")
    response = requests.get(BASE_URL)
    print(f"[GET] Código de estado: {response.status_code}")
    if response.status_code == 200:  # Si la solicitud es exitosa
        dispositivos = response.json()  # Obtén la respuesta en formato JSON
        print("Dispositivos listados correctamente.")
        print(f"Datos de dispositivos: {dispositivos}")
        return dispositivos
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Muestra el mensaje de error
        return None

# Función para actualizar un dispositivo (PUT)
def actualizar_dispositivo(id, data):
    print(f"\nActualizando dispositivo ID {id} con los datos: {data}")
    response = requests.put(f"{BASE_URL}/{id}", json=data)
    print(f"[PUT] Código de estado: {response.status_code}")
    if response.status_code == 200:  # Si la actualización es exitosa
        dispositivo = response.json()  # Obtén la respuesta en formato JSON
        print("Dispositivo actualizado correctamente.")
        print(f"Dispositivo actualizado: {dispositivo}")
        return dispositivo
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Muestra el mensaje de error
        return None

# Función para eliminar un dispositivo (DELETE)
def eliminar_dispositivo(id):
    print(f"\nEliminando dispositivo ID {id}...")
    response = requests.delete(f"{BASE_URL}/{id}")
    print(f"[DELETE] Código de estado: {response.status_code}")
    if response.status_code == 204:  # Si la eliminación es exitosa
        print("Dispositivo eliminado correctamente.")
        return True
    else:
        print(f"Error: {response.status_code}")
        print(response.text)  # Muestra el mensaje de error
        return False

# Pruebas de las funciones
if __name__ == "__main__":
    # 1. Agregar un dispositivo
    nuevo_dispositivo = {"name": "Router 2", "type": "Router", "status": "active"}
    agregar_dispositivo(nuevo_dispositivo)

    # 2. Listar dispositivos
    dispositivos = listar_dispositivos()
    print(f"Dispositivos obtenidos: {dispositivos}")

    # 3. Actualizar un dispositivo (ID=1)
    dispositivo_actualizado = {"name": "Router 1 Actualizado", "type": "Router", "status": "inactive"}
    actualizar_dispositivo(1, dispositivo_actualizado)

    # 4. Eliminar un dispositivo (ID=2)
    eliminar_dispositivo(2)

    print("\n¡Proceso completado!")
