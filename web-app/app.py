from flask import Flask, render_template, request
from tinydb import TinyDB, Query
from serial.tools import list_ports
from pydobot import Dobot
from datetime import datetime

app = Flask(__name__)
log_db = TinyDB('./web-app/log_database.json')

@app.route('/', methods=['GET', 'POST'])
def mainPage():

    connectedComPorts = list_ports.comports()

    if len(connectedComPorts) > 0:
        return render_template("main_page.html")
    
    return render_template("log_page.html", log_db=log_db)

@app.route('/conexao')
def conexao():
    connectedComPorts = list_ports.comports()

    if len(connectedComPorts) > 0:
        return '<p>O robô está conectado corretamente</p>'
    
    return '<p>O robô não está conectado corretamente</p>'

@app.route('/logs')
def logPage():
    return render_template("log_page.html", log_db=log_db)

@app.route('/mover_braco', methods=['POST'])
def mover_braco():

    x = float(request.form.get("X"))
    y = float(request.form.get("Y"))
    z = float(request.form.get("Z"))

    robot.move_to(x=x, y=y, z=z, r=50, wait=True)

    log_db.insert({'horario': str(datetime.now()), 'X': x, 'Y': y, 'Z': z})

    return f"<p>Coordenadas atuais: X: {x} Y: {y} Z: {z}"

if __name__ == "__main__":

    connectedComPorts = list_ports.comports()

    if len(connectedComPorts) > 0:
        robot = Dobot(port=connectedComPorts[0].device)
    else:
        print("Erro de conexão com o robô")

    app.run(port=8000, host='0.0.0.0')