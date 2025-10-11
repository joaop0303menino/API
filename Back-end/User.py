from flask import Blueprint, request, jsonify
from Connect import Connect

class Users:
    def __init__(self):
        self.connect = Connect()
        self.blueprint = Blueprint("users", __name__, url_prefix="/api/users")
        self.register_routes()

    def register_routes(self):
        @self.blueprint.route("/", methods=["GET"])
        def get_all_users():
            conn = self.connect.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Usuario")
            rows = cursor.fetchall()
            conn.close()

            users = [{"id": r[0], "name": r[1], "year": r[2], "city": r[3]} for r in rows]
            return jsonify(users)

        @self.blueprint.route("/<int:id>", methods=["GET"])
        def get_user(id):
            conn = self.connect.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Usuario WHERE id=?", (id,))
            row = cursor.fetchone()
            conn.close()

            if row:
                return jsonify({"id": row[0], "name": row[1], "year": row[2], "city": row[3]})
            else:
                return jsonify({"error": "User not found"}), 404

        @self.blueprint.route("/", methods=["POST"])
        def add_user():
            data = request.get_json()
            name = data.get("name")
            year = data.get("year")
            city = data.get("city")

            conn = self.connect.get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Usuario (name, year, city) VALUES (?, ?, ?)", (name, year, city))
            conn.commit()
            conn.close()

            return jsonify({"message": "User added"}), 201

        @self.blueprint.route("/<int:id>", methods=["PUT"])
        def update_user(id):
            data = request.get_json()
            name = data.get("name")
            year = data.get("year")
            city = data.get("city")

            conn = self.connect.get_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE Usuario SET name=?, year=?, city=? WHERE id=?", (name, year, city, id))
            updated = cursor.rowcount
            conn.commit()
            conn.close()

            if updated:
                return jsonify({"message": "User updated"})
            else:
                return jsonify({"error": "User not found"}), 404

        @self.blueprint.route("/<int:id>", methods=["DELETE"])
        def delete_user(id):
            conn = self.connect.get_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Usuario WHERE id=?", (id,))
            deleted = cursor.rowcount
            conn.commit()
            conn.close()

            if deleted:
                return jsonify({"message": "User deleted"})
            else:
                return jsonify({"error": "User not found"}), 404

    def get_blueprint(self):
        return self.blueprint
