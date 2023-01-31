from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/operasbas", methods=["GET"])
def index():
    return render_template("operasbas.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    num1 = request.form["txtNum1"]
    num2 = request.form["txtNum2"]

    suma = int(num1) + int(num2)
    resta = int(num1) - int(num2)
    mult = int(num1) * int(num2)
    div = int(num1) / int(num2)

    return render_template("resultado.html", suma = suma, resta = resta, mult = mult, div = div)


if __name__ == "__main__":
    app.run(debug = True, port = 3000)