from flask import Flask
from User import Users
from Contacts import Contacts

class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.register_blueprints()

        @self.app.route("/")
        def home():
            return "Welcome to the API"

    def register_blueprints(self):
        self.app.register_blueprint(Users().get_blueprint())
        self.app.register_blueprint(Contacts().get_blueprint())

    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    application = App()
    application.run()
