from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# URL de la API externa
BASE_URL = 'https://66eb36b055ad32cda47c0343.mockapi.io/IoTCarStatus'


# Método GET - Obtener todos los carros o uno en específico por ID
@app.route('/cars', methods=['GET'])
@app.route('/cars/<car_id>', methods=['GET'])
def get_cars(car_id=None):
    if car_id:
        # Obtener un carro específico por ID
        response = requests.get(f"{BASE_URL}/{car_id}")
    else:
        # Obtener todos los carros
        response = requests.get(BASE_URL)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    return jsonify({"error": "Recurso no encontrado"}), response.status_code


# Método POST - Crear un nuevo carro
@app.route('/cars', methods=['POST'])
def create_car():
    new_car = request.json
    response = requests.post(BASE_URL, json=new_car)

    if response.status_code == 201:
        return jsonify(response.json()), 201
    return jsonify({"error": "No se pudo crear el carro"}), response.status_code


# Método PUT - Actualizar un carro existente
@app.route('/cars/<car_id>', methods=['PUT'])
def update_car(car_id):
    updated_data = request.json
    response = requests.put(f"{BASE_URL}/{car_id}", json=updated_data)

    if response.status_code == 200:
        return jsonify(response.json()), 200
    return jsonify({"error": "No se pudo actualizar el carro"}), response.status_code


# Método DELETE - Eliminar un carro
@app.route('/cars/<car_id>', methods=['DELETE'])
def delete_car(car_id):
    response = requests.delete(f"{BASE_URL}/{car_id}")

    if response.status_code == 200:
        return jsonify({"message": f"Carro con ID {car_id} eliminado con éxito"}), 200
    return jsonify({"error": "No se pudo eliminar el carro"}), response.status_code


if __name__ == '__main__':
    app.run(debug=True)
