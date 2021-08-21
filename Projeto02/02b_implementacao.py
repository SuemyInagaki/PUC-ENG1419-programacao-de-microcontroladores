from extra.aula import rodar

@rodar
def programa():
  # importação de bibliotecas
  from flask import Flask, render_template, redirect
  from gpiozero import LED, Button
  from Adafruit_CharLCD import Adafruit_CharLCD
  from lirc import init
  from py_irsend.irsend import send_once
  from threading import Timer
  
  init("aquario", blocking=False)
    
  # criação do servidor
  app = Flask(__name__)
    
  # definição de funções das páginas
  @app.route("/power")
  def power():
    send_once("aquario", ["KEY_POWER"])
    return "O servidor está funcionando!"

  @app.route("/aumentar")
  def aumentar():
    send_once("aquario", ["KEY_VOLUMEUP"])
    return "Volume aumentado!"

  @app.route("/diminuir")
  def diminuir():
    send_once("aquario", ["KEY_VOLUMEDOWN"])
    return "Volume diminuir"
  
  @app.route("/mudo")
  def mudo():
    send_once("aquario", ["KEY_MUTE"])
    return "mudo"
  
  @app.route("/canal/<string:canal_str>")
  def canal(canal_str):
    btn_list = []
    for num_str in canal_str:
      btn_list.append("KEY_" + num_str)
    send_once("aquario", btn_list)
    return "Mudou canal para " + canal_str
  
  @app.route("/desliga/<int:t>")
  def desliga(t):
    Timer(t, lambda: send_once("aquario", ["KEY_POWER"])).start()
    return "desliga apos " + str(t) + " segundos"
  # rode o servidor
  app.run(port=5000)