#API ES LA FORMA EN QUE 2 APPS SE COMUNICAN ENTRE SI
#application programming interface

#formas de conectarse:
#SDK, O LIBRERIA, DIRECTAMENTE EN CODIGO
#REST basado en http, la mas popular// el q vamos a utilizar
#SOAP Y OTROS: se estan dejando de usar



#REST: REPRESENTATIONAL STATE TRANSFER

#CLIENTE SERVIDOR
#SIN ESTADO: no se guardan datos de contexto en el servidor
#CACHEABLE
#SISTEMA EN CAPAS
#CODIGO A DEMANDA:pueden recibir codigo ejecutable
#INTERFAZ UNIFORME

#!flask/bin/python
# -*- coding: UTF-8 -*-

from flask import Flask, request, jsonify, abort

app= Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True



@app.route('/')
def index():
    info={
        "mensaje" : "Bienvenido a la API",
        "acciones" : [
            "GET /curriculum",
            "POST /mensajes" 
        ]
    }
    return jsonify(info)

@app.route('/curriculum', methods=['GET'])
def cv():
    url_imagen = request.host_url + "static/amigosmtb.png"
    cv = {
        "nombre" : "Franco",
        "apellido" : "Di Martino",
        "residencia" : "Argentina",
        "experiencia" : [{
            "posicion" : "< describe tu posición>",
            "empresa" : "< nombre de tu empresa >",
            "desde" : "< cuándo empezaste a trabajar >",
            "hasta" : "< si ya no trabajas más, cuándo >",
            "descripcion" : "< detalles >"
        }],
        "educación" : {
            "nivel" : "< nivel de tus estudios >",
            "titulo" : "< nombre de tu carrera >",
            "institucion" : "< dónde estudiaste >",
            "facultad" : "< más detalles >"
        },
        "intereses" : ["python", "apis", "enseñar"],
        "redes" : {
            "github" : "https://github.com/DiMartinoFranco",
            
            
        },
        "foto" : url_imagen
    }
    return jsonify(cv)




@app.route('/mensajes', methods=['POST'])
def contacto():
    mensaje = request.get_data()

    if not mensaje:
        abort(400, description="Debe enviar su mensaje en el body del POST.")
    print("MENSAJE DE CONTACTO: " + str(mensaje))
    return "Gracias por su mensaje."

if __name__=='__main__':
    app.run()



