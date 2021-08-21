from cv2 import *

stream = VideoCapture(0)

while True:
    _, imagem = stream.read()
    imshow("Minha Janela", imagem)


    imagem_hsv = cvtColor(imagem, COLOR_BGR2HSV)
    #suemy
    claro = (0, 100, 0)   # valores no espaço HSV
    escuro = (137, 181, 255) # valores no espaço HSV
    
    #rafael
    escuro = (52,255,255)
    claro = (5,66,0)
    
    mascara = inRange(imagem_hsv, claro, escuro)

    imagem2 = bitwise_and(imagem, imagem, mask=mascara)

    imshow("Janela com Minha Cor", imagem2)

    mascara2 = bitwise_not(mascara)
    imagem_com_mascara_invertida = bitwise_and(imagem, imagem, mask=mascara2)
    imagem_cinza = cvtColor(imagem_com_mascara_invertida, COLOR_BGR2GRAY)
    imagem_cinza = cvtColor(imagem_cinza, COLOR_GRAY2BGR)


    imshow("Janela com Imagem em Tons de Cinza Menos Minha Cor", imagem_cinza)

    imagem_final =  imagem2 + imagem_cinza

    putText(imagem_final, "Naruto", (100,50), color=(0,102,255), thickness=2, fontFace=FONT_HERSHEY_SIMPLEX, fontScale=1)
    
    imshow("Janela com Imagem Final", imagem_final)

    


    if waitKey(1) & 0xFF == ord("q"):
        break

stream.release()
destroyAllWindows()
