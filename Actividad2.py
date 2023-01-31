from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/operasbas", methods=["GET"])
def index():
    return render_template("act_opera_base.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    num1 = request.form["txtNum1"]
    num2 = request.form["txtNum2"]

    mult = int(num1) * int(num2)

    string = ""
    
    for i in range(0, int(num2)):
        string += str(num1) + " + "

    string = string[:-3]
    string += " = " + str(mult)

    return render_template("act_resultado.html", mult = mult, string = string)


if __name__ == "__main__":
    app.run(debug = True, port = 3000)