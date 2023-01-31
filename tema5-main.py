from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    titulo = "Home RC"
    lista = ["Cristian", "Adrian"]
    return render_template("index.html", titulo = titulo, lista = lista)

@app.route("/Alumnos")
def alumnos():
    return render_template("Alumnos.html")

@app.route("/Usuarios")
def usuarios():
    return render_template("Usuarios.html")

if __name__ == "__main__":
    app.run(debug = True, port = 3000)