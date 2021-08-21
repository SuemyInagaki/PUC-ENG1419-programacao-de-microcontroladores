from extra.tello import Tello
from time import sleep
from cv2 import *
from traceback import format_exc

    
drone = Tello("TELLO-C7AC08", test_mode=True)
#drone = Tello("TELLO-D023AE", test_mode=True)
drone.inicia_cmds()
print("[INFO] - Drone pronto")



while True:
    
  # A linha abaixo já faz o papel do VideoCapture e do stream.read
  imagem1 = drone.current_image
  imagem2 = drone.current_image
  
  
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
    x, y, comprimento, altura = boundingRect(contorno)
    
    rectangle(imagem1, pt1=(x,y), pt2=(x+comprimento,y+altura), color=(0,255,0), thickness=3)
    
    area = comprimento*altura
    if(area>maior_area and area >2000):
      maior_area=area
      maior_contorno = contorno

  if (maior_contorno is not None):
    x,y,comprimento,altura = boundingRect(maior_contorno)
    rectangle(imagem2, pt1=(x,y), pt2=(x+comprimento,y+altura), color=(0,255,0), thickness=3)
 
  imshow("Todos os contornos", imagem1)
  imshow("O maior contorno", imagem2)
  
  if waitKey(1) & 0xFF == ord("q"):
    break

destroyAllWindows()