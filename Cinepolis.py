from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/cinepolis", methods=["GET"])
def index():
    return render_template("cinepolis.html")

@app.route("/procesar", methods=["POST"])
def resultado():

    data = {}
    
    costo_boleto = 12
    costo_final = 0
    nombre = request.form["nombre"]
    cantidad_compradores = int(request.form["cantidad_compradores"])
    tarjeta_cineco = int(request.form["tarjeta_cineco"])
    cantidad_boletos = int(request.form["cantidad_boletos"])

    cantidad_boletos_permitidos = 7 * cantidad_compradores

    descuento = 0

    if(cantidad_boletos > cantidad_boletos_permitidos):
        data["costo_final"] = "No se puede comprar mas de 7 boletos"
        return data

    if(cantidad_boletos * cantidad_compradores > cantidad_compradores * 5 and cantidad_boletos <= cantidad_boletos_permitidos):
        descuento = 0.15

    if(cantidad_boletos * cantidad_compradores > cantidad_compradores * 2 and cantidad_boletos <= cantidad_compradores * 5):	
        descuento = 0.10

    if(cantidad_boletos <= cantidad_compradores * 2):
        descuento = 0

    costo_final = (costo_boleto * cantidad_boletos) - (costo_boleto * cantidad_boletos * descuento)

    if(tarjeta_cineco == 1):
        costo_final = costo_final - (costo_final * 0.10)
    
    data["costo_final"] = costo_final

    return data


if __name__ == "__main__":
    app.run(debug = True, port = 3000)