from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo! -- Nuevo Cambio --"

@app.route("/user/<string:username>")
def user(username):
    return "Hola %s!" % username

@app.route("/numero/<int:n>")
def numero(n):
    return "El numero es %d" % n

@app.route("/suma/<int:id>/<string:username>")
def username(id, username):
    return "<h1> El id es %d y el nombre es %s </h1>" % (id, username)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma es %f" % (n1 + n2)

@app.route("/default")
@app.route("/default/<string:n>")
def default(n = "datos"):
    return "El valor por defecto es %s" % n

if __name__ == "__main__":
    app.run(debug = True, port = 3000)