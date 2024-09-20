from flask import Flask, request, jsonify

app = Flask(__name__)

# Datos simulados para el ejemplo
items = {
    "99": {"name": "Item 99", "description": "This is item 99"}
}

# Método GET
@app.route('/api/item', methods=['GET'])
def get_item():
    item_id = request.args.get('id')
    if item_id in items:
        return jsonify(items[item_id])
    else:
        return jsonify({"error": "Item no encontrado"}), 404

# Método POST - Crear un nuevo item
@app.route('/api/item', methods=['POST'])
def create_item():
    new_item = request.json
    item_id = new_item.get('id')

    if not item_id or item_id in items:
        return jsonify({"error": "ID inválido o ya existe"}), 400

    items[item_id] = {"name": new_item.get("name"), "description": new_item.get("description")}
    return jsonify({"message": "Item creado con éxito", "item": items[item_id]}), 201

# Método PUT - Actualizar un item existente
@app.route('/api/item', methods=['PUT'])
def update_item():
    item_id = request.json.get('id')

    if not item_id or item_id not in items:
        return jsonify({"error": "Item no encontrado"}), 404

    items[item_id]['name'] = request.json.get('name', items[item_id]['name'])
    items[item_id]['description'] = request.json.get('description', items[item_id]['description'])
    return jsonify({"message": "Item actualizado con éxito", "item": items[item_id]}), 200

# Método DELETE - Eliminar un item
@app.route('/api/item', methods=['DELETE'])
def delete_item():
    item_id = request.json.get('id')

    if not item_id or item_id not in items:
        return jsonify({"error": "Item no encontrado"}), 404

    del items[item_id]
    return jsonify({"message": f"Item {item_id} eliminado con éxito"}), 200

if __name__ == '__main__':
    app.run(port=5000)
