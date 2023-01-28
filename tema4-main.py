from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/operasBasicas", methods=["GET", "POST"])
def operasBasicas():

    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        return "<h2> La suma es {} </h2>".format(str(int(num1) + int(num2)))
    else:

        return """
        <form action = "" method = "post">
            <label> Numero 1: </label>
            <input type = "text" name = "num1" />
            <label> Numero 2: </label>
            <input type = "text" name = "num2" />
            <input type = "submit" value = "Sumar" />
        </form>
        """


if __name__ == "__main__":
    app.run(debug=True, port=3000)
