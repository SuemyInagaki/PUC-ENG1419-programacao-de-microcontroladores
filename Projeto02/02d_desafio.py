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
  from json import load

  init("aquario", blocking=False)
    
  # criação do servidor
  app = Flask(__name__)
    
  global dicionarios_de_canais 
  dicionarios_de_canais = load(open('canais.json', encoding="UTF-8"))
  print(dicionarios_de_canais)

  # definição de funções das páginas
  @app.route("/")
  def main_page():
    global dicionarios_de_canais
    return render_template("pagina1.html", dicionarios_de_canais=dicionarios_de_canais)

  @app.route("/power")
  def power():
    send_once("aquario", ["KEY_POWER"])
    return redirect("/")

  @app.route("/aumentar")
  def aumentar():
    send_once("aquario", ["KEY_VOLUMEUP"])
    return redirect("/")

  @app.route("/diminuir")
  def diminuir():
    send_once("aquario", ["KEY_VOLUMEDOWN"])
    return redirect("/")
  
  @app.route("/mudo")
  def mudo():
    send_once("aquario", ["KEY_MUTE"])
    return redirect("/")
  
  @app.route("/canal/<string:canal_str>")
  def canal(canal_str):
    btn_list = []
    for num_str in canal_str:
      btn_list.append("KEY_" + num_str)
    send_once("aquario", btn_list)
    return redirect("/")
  
  @app.route("/desliga/<int:t>")
  def desliga(t):
    Timer(t, lambda: send_once("aquario", ["KEY_POWER"])).start()
    return redirect("/")

  # rode o servidor
  app.run(port=5000)