from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    titulo = "Home"
    lista = ["Cristian", "Adrian"]
    return render_template("index.html", titulo = titulo, lista = lista)

if __name__ == "__main__":
    app.run(debug = True, port = 3000)