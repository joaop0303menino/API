from flask import Flask

app = Flask(__name__)

@app.route("/task", methods=["GET"])
def GET_all_task():
    return "GET: Task"

@app.route("/task/<int:id>", methods=["GET"])
def GET_task(id):
    return "GET: Task"

@app.route("/task", methods=["POST"])
def POST_task():
    return "POST: Task"

@app.route("/task/<int:id>", methods=["PUT"])
def PUT_task(id):
    return "PUT: Task"

@app.route("/task/<int:id>", methods=["DELETE"])
def DELETE_task(id):
    return "DELETE: Task"

if __name__ == "__main__":
    app.run(debug=True)