from extra.prova import rodar

@rodar
def programa():
    
    # importação das bibliotecas
    from time import sleep
    from gpiozero import LED, Button, DistanceSensor, Buzzer, LightSensor, MotionSensor
    from datetime import datetime
    from pymongo import MongoClient, ASCENDING, DESCENDING
    #from extra.redefinir_banco import redefinir_banco
    from requests import post
    from flask import Flask, render_template, redirect
    from threading import Timer
    from Adafruit_CharLCD import Adafruit_CharLCD
    from mplayer import Player
    
    
    
    # inicialização dos componentes
    
    lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)
    botao1 = Button(11)
    botao2 = Button(12)
    botao3 = Button(13)
    botao4 = Button(14)
    sensor_de_movimento = MotionSensor(27)
    sensor_de_luz = LightSensor(8)
    sensor_de_luz.threshold = 0.7
    sensor_de_distancia = DistanceSensor(trigger=17, echo=18)
    
    
    # inicialização do banco de dados
    
    cliente = MongoClient("localhost", 27017)
    banco = cliente["questao2"] 
    colecao = banco["sensores"]

    
    
    # inicialização do servidor
    
    app = Flask(__name__)
    
    
    # páginas do servidor
    
    @app.route("/")
    def home():
        texto = sensor_de_distancia.distance*100
        texto = round(texto, 3)
        texto = "Distancia atual: "+str(texto) + " cm"
        return texto
    
    @app.route("/tracinhos/<string:palavra>")
    def tracinhos(palavra):
        nova = ""
        for i in range(len(palavra)):
            if i != len(palavra) -1:
                nova+= palavra[i]
                nova+= "-"
            else:
                nova+= palavra[i]
        return nova
            
    @app.route("/documento")
    def documento():
        sensor_de_luz.threshold = 0.7
        agora = datetime.now()
        if sensor_de_movimento.motion_detected:
            movimento = "movimentando"
        else:
            movimento = "parado"
        if sensor_de_distancia.distance*100 >= 8:
            distancia = "longe"
        else:
            distancia = "perto"
        if sensor_de_luz.light_detected:
            luz = "claro"
        else:
            luz = "escuro"
        dados = {"data/hora": agora, "movimento": movimento, "distancia": distancia, "luz": luz} 
        colecao.insert(dados)
        return "Dados dos sensores adicionado ao banco de dados"
    
    @app.route("/busca")
    def busca():
        b = {"movimento": "movimentando"}
        documentos = list(colecao.find(b))
        qm1 = len(documentos)
        b = {"movimento": "parado"}
        documentos = list(colecao.find(b))
        qm2 = len(documentos)
        b = {"distancia": "perto"}
        documentos = list(colecao.find(b))
        qd1 = len(documentos)
        b = {"distancia": "longe"}
        documentos = list(colecao.find(b))
        qd2 = len(documentos)
        b = {"luz": "claro"}
        documentos = list(colecao.find(b))
        ql1 = len(documentos)
        b = {"luz": "escuro"}
        documentos = list(colecao.find(b))
        ql2 = len(documentos)
        texto = "<ul> <li>Movimentando: " +str(qm1)+" / Parado: "+str(qm2) + "</li>"
        texto+= "<li>Perto: "+str(qd1)+" / Longe: " + str(qd2) + "</li>"
        texto+="<li>Claro: "+str(ql1) + " / Escuro: "+str(ql2) + "</li></ul>"
        return texto

    
    # roda o servidor
    
    app.run(port=5000)
    
    
    # loop infinito (pode remover depois que fizer o servidor)
    while True:
        sleep(0.2)