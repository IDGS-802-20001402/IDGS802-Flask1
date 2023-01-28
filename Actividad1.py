from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/operasBasicas", methods=["GET", "POST"])
def operasBasicas():

    if request.method == "POST":
        num1 = request.form.get("num1")
        num2 = request.form.get("num2")
        operacion = request.form.get("operacion")
        
        if operacion == "suma":
            return "<h2> La suma es {} </h2>".format(str(int(num1) + int(num2)))
        elif operacion == "resta":
            return "<h2> La resta es {} </h2>".format(str(int(num1) - int(num2)))
        elif operacion == "multiplicacion":
            return "<h2> La multiplicacion es {} </h2>".format(str(int(num1) * int(num2)))
        else:
            return "<h2> La division es {} </h2>".format(str(int(num1) / int(num2)))
            
    else:
        return """
        <form action="" method="post">
            <input type="text" name="num1" placeholder="Numero 1">
            <br>
            <input type="text" name="num2" placeholder="Numero 2">
            <br>
            <br>
            <input type="radio" name="operacion" value="suma"> Suma
            <input type="radio" name="operacion" value="resta"> Resta
            <input type="radio" name="operacion" value="multiplicacion"> Multiplicacion
            <input type="radio" name="operacion" value="division"> Division
            <br>
            <br>
            <input type="submit" value="Enviar">
        </form>
        
        <style>

            form{
                width: 400px;
                margin: 0 auto;
                padding: 20px;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            input{
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
            }

            input[type="radio"]{
                width: 20px;
                padding: 10px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 5px;
            }


            input[type="submit"]{
                background: #333;
                color: #fff;
                border: none;
                cursor: pointer;
            }
            
        </style>
        
        """

if __name__ == "__main__":
    app.run(debug=True, port=3000)