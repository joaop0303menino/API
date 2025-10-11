from flask import Blueprint, request, jsonify
from Connect import Connect

class Contacts:
    def __init__(self):
        self.connect = Connect()
        self.blueprint = Blueprint("contacts", __name__, url_prefix="/api/contacts")
        self.register_routes()

    def register_routes(self):
        @self.blueprint.route("/", methods=["GET"])
        def get_all_contacts():
            conn = self.connect.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Contacts")
            rows = cursor.fetchall()
            conn.close()

            contacts = [{"id": r[0], "type": r[1], "value": r[2], "user_id": r[3]} for r in rows]
            return jsonify(contacts)

        @self.blueprint.route("/<int:id>", methods=["GET"])
        def get_contact(id):
            conn = self.connect.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Contacts WHERE id=?", (id,))
            row = cursor.fetchone()
            conn.close()

            if row:
                return jsonify({"id": row[0], "type": row[1], "value": row[2], "user_id": row[3]})
            else:
                return jsonify({"error": "Contact not found"}), 404

        @self.blueprint.route("/", methods=["POST"])
        def add_contact():
            data = request.get_json()
            type = data.get("type")
            value = data.get("value")
            user_id = data.get("user_id")

            conn = self.connect.get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Contacts (type, value, user_id) VALUES (?, ?, ?)", (type, value, user_id))
            conn.commit()
            conn.close()

            return jsonify({"message": "Contact added"}), 201

        @self.blueprint.route("/<int:id>", methods=["PUT"])
        def update_contact(id):
            data = request.get_json()
            type = data.get("type")
            value = data.get("value")
            user_id = data.get("user_id")

            conn = self.connect.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Contacts SET type=?, value=?, user_id=? WHERE id=?", (type, value, user_id, id))
            updated = cursor.rowcount
            conn.commit()
            conn.close()

            if updated:
                return jsonify({"message": "Contact updated"})
            else:
                return jsonify({"error": "Contact not found"}), 404

        @self.blueprint.route("/<int:id>", methods=["DELETE"])
        def delete_contact(id):
            conn = self.connect.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Contacts WHERE id=?", (id,))
            deleted = cursor.rowcount
            conn.commit()
            conn.close()

            if deleted:
                return jsonify({"message": "Contact deleted"})
            else:
                return jsonify({"error": "Contact not found"}), 404

    def get_blueprint(self):
        return self.blueprint
