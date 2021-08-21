from serial import Serial
from threading import Thread, Timer
from extra.tello import Tello
from time import sleep
from cv2 import *
from traceback import format_exc
import numpy as np

global x
global y
global altura
global comprimento

global image_width
global image_height

x=0
y=0
altura=0
comprimento=0

def serial():
  while True:
    if meu_serial != None:
      texto_recebido = meu_serial.readline().decode().strip()
      if texto_recebido != "":
        if (texto_recebido == "Decolar"):
          drone.takeoff();

        elif (texto_recebido == "Pousar"):
          drone.land();

        elif (texto_recebido == "esquerda"):
          drone.rc(0,0,0,-40)

        elif (texto_recebido == "direita"):
          drone.rc(0,0,0,40)

        elif (texto_recebido == "frente"):
          drone.rc(0,40,0,0)

        elif (texto_recebido == "Parar"):
          drone.rc(0,0,0,0)

        # ESCREVA AQUI O SEU CÓDIGO DA SERIAL!

def enviaMsg():
  global x, y, altura, comprimento
  print(x,y,altura,comprimento)
  x = int(202*x/image_width)
  y = int(152*y/image_height)
  altura = int(152*altura/image_height)
  comprimento = int(202*comprimento/image_width)
  
  string = f"retangulo {x:03d} {y:03d} {altura:03d} {comprimento:03d}"
  print(string)
  meu_serial.write(string.encode("UTF-8"))
  Timer(3,enviaMsg).start()

  
# CASO A SERIAL NÃO FUNCIONE, COMENTE A LINHA ABAIXO E DESCOMENTE A SEGUINTE

meu_serial = Serial("COM9", baudrate=9600, timeout=0.1)
#meu_serial = None

print("[INFO] Serial: ok")

thread = Thread(target=serial)
thread.daemon = True
thread.start()  

drone = Tello("TELLO-C7AC08", test_mode=True)
#drone = Tello("TELLO-D023AE", test_mode=True)
drone.inicia_cmds()
print("[INFO] Drone pronto")

try:
  Timer(3,enviaMsg).start()

  while True:
    
    # COLOQUE AQUI O CÓDIGO DO WHILE DA IMPLEMENTACAO
    imagem1 = drone.current_image 
    
    # COLOQUE AQUI O CÓDIGO DO OPENCV
    
    imagem_hsv = cvtColor(imagem1, COLOR_BGR2HSV)
  
    #Drone:
    claro = (0, 60, 60)
    escuro = (20, 255, 255)
    
    mascara = inRange(imagem_hsv, claro, escuro)

    contornos,_ = findContours(mascara, RETR_TREE, CHAIN_APPROX_SIMPLE)
  
    maior_area=0
    maior_contorno = None
    pontos = None

    for contorno in contornos:
      x_1, y_1, comprimento_1, altura_1 = boundingRect(contorno)
            
      area = comprimento_1*altura_1
      if(area>maior_area and area >2000):
        maior_area=area
        maior_contorno = contorno

    if (maior_contorno is not None):
      x,y,comprimento,altura = boundingRect(maior_contorno)


    if waitKey(1) & 0xFF == ord("q"):
      break
    
    image_height, image_width, _ = imagem1.shape
    rectangle(imagem1, pt1=(x,y), pt2=(x+comprimento,y+altura), color=(0,255,0), thickness=3)
    imshow("Todos os contornos", imagem1)
        

except:
  if meu_serial != None:
    meu_serial.close()
  
  print("FIM!")
  print(format_exc())
  drone.land()
   