# Neste playground 10 B, vamos trabalhar com o vídeo da câmera web.
# Veja os códigos de exemplo e programe o que está sendo soliticado em LETRAS MAIÚSCULAS.


# Mas primeiro temos alguns lembretes importantes!
    
# 1. Caso você não tenha uma câmera web, existem apps que conectam a câmera do seu celular com o computador.
    # Nesse caso, experimente apps como o Camo ou o Iriun.
# 2. Se você estiver usando o Thonny no macOS, rode o código com Run > Run current script in terminal.


# Começamos importando todas as funções do OpenCV.
from cv2 import *


# Aí podemos iniciar a conexão com a câmera web.
stream = VideoCapture(0)


# Dentro do while True, a gente fica repetindo aquele ciclo de captura -> processamento -> exibição da imagem.
while True:
    
    # Captura um quadro de imagem pela câmera.
    _, imagem_original = stream.read()
    
    
    # Vamos começar só exibindo essa imagem direto na janela.
    imshow("Janela com Imagem Original", imagem_original)
    
    
    # RODE O CÓDIGO PARA TESTAR O STREAM BÁSICO.
    # APERTE "Q" NO TECLADO PARA SAIR.
    
    
    # Agora vamos testar vários tipos de modificação nessa imagem original antes de exibi-la.
    # Vou começar com o blur, para desfocar a imagem.
    # Ela recebe a imagem original e a intensidade do borrão na horizontal e na vertical.
    imagem_desfocada = blur(imagem_original, (30, 30))
    
    
    # Agora é só chamar a imshow para essa nova imagem.
    # Se houver mais de um imshow com títulos diferentes, o Python vai abrir janelas separadas.
    # Por isso, você pode ir comentando de novo essas chamadas, se quiser.
    
    
    # DESCOMENTE A LINHA A SEGUIR E RODE O CÓDIGO PARA VER O RESULTADO.
    # EM SEGUIDA, EXPERIMENTE VARIAR O PARÂMETRO DO BLUR, INCLUSIVE COM VALORES NÃO REPETIDOS.
    
    imshow("Janela com Imagem Desfocada", imagem_desfocada)
    
    
    
    # Existem vários efeitos rápidos como o blur.
    # Eu não cheguei a comentar na teoria, mas vamos testar a convertScaleAbs.
    # Ela é útil para mexer no brilho e no contraste da imagem.
    # Para cada ponto da imagem, ela multiplica o valor por alpha e adiciona beta.
    # Aumentando esses valores, a gente deixa a imagem mais clara.
    imagem_mais_clara = convertScaleAbs(imagem_original, alpha=1.5, beta=30)
    
    
    # DESCOMENTE A LINHA A SEGUIR E RODE O CÓDIGO PARA VER O RESULTADO.
    # EM SEGUIDA, EXPERIMENTE VARIAR O ALPHA (ENTRE 0 E 1) E O BETA (ENTRE -255 E 255)
    
    #imshow("Janela com Mais Contraste e Brilho", imagem_mais_clara)
    
    #Com alpha entre 0 e 1, a imagem fica mais escura
    #Com beta = 255 a imagem fica toda branca
    #Com beta = 100 a imagem parece que fica meio branca. Como se tivesse um papel manteiga na frente
    imagem_suemy = convertScaleAbs(imagem_original, alpha=1, beta=100)
    
    #imshow("Janela suemy", imagem_suemy)    
    # Outro efeito simples é deixar tudo em tons de cinza.
    # Como a gente comentou na teoria, é só mudar o espaço de cores para CINZA.
    # Mas como eu posso querer combinar isso com coisas coloridas, voltamos em seguida para o espaço BGR.
    # Nesse retorno, os tons de cinza permanecem, só que usando as 3 componentes de cor.
    imagem_cinza = cvtColor(imagem_original, COLOR_BGR2GRAY)
    imagem_cinza = cvtColor(imagem_cinza, COLOR_GRAY2BGR)
    
    
    # DESCOMENTE A LINHA A SEGUIR PARA VER O RESULTADO, DEPOIS COMENTE NOVAMENTE.
    
    #imshow("Janela com Imagem em Tons de Cinza", imagem_cinza)
    
    
    
    # COMBINE OS EFEITOS NA IMAGEM ORIGINAL PARA ESCURECER E DEIXAR EM TONS DE CINZA.
    # DEPOIS EXIBA O RESULTADO NUMA NOVA JANELA.
    
    #Por algum motivo, essas duas proximas linhas nao funcionam bem
    #imagem_com_efeitos = cvtColor(imagem_original, COLOR_GRAY2BGR)
    #imagem_com_efeitos = cvtColor(imagem_com_efeitos, COLOR_GRAY2BGR)
    imagem_com_efeitos = convertScaleAbs(imagem_cinza, alpha=0.1, beta=0)
    imagem_cinza = cvtColor(imagem_com_efeitos, COLOR_BGR2GRAY) #transforma em escala de cinza
    imagem_cinza = cvtColor(imagem_cinza, COLOR_GRAY2BGR) #volta para a escala original. Mas perde informacoes de cores
    
    #imshow("Janela com Imagem com efeitos", imagem_cinza)
    
    
    # A mudança no espaço de cor é útil também para criar máscaras.
    # O espaço HSV ajuda na seleção de tons diferentes de uma determinada cor.
    # No exemplo abaixo, vou criar uma máscara que selecione tons de azul.
    imagem_hsv = cvtColor(imagem_original, COLOR_BGR2HSV)
    azul_claro = (110, 0, 0)   # valores no espaço HSV
    azul_escuro = (170, 255, 255) # valores no espaço HSV
    mascara = inRange(imagem_hsv, azul_claro, azul_escuro)
    
    #Para inverter a mascara (mostrar tuo que nao for azul)
    #mascara2 = bitwise_not(mascara)
    #imagem_com_azuis = bitwise_and(imagem_original, imagem_original, mask=mascara2)
    
    # Nessa máscara, os tons de azul aparecerão como regiões brancas, e o resto fica tudo preto.
    
    
    # DESCOMENTE A LINHA A SEGUIR PARA VER O RESULTADO, DEPOIS COMENTE NOVAMENTE.
    
    #imshow("Janela com Mascara para Tons de Azul", mascara)
    
    
    
    # Agora eu posso aplicar a máscara na imagem original, para mostrar só os tons.
    imagem_com_azuis = bitwise_and(imagem_original, imagem_original, mask=mascara)
    
    
    # DESCOMENTE A LINHA A SEGUIR PARA VER O RESULTADO, DEPOIS COMENTE NOVAMENTE.
    
    #imshow("Janela com Apenas Tons de Azul", imagem_com_azuis)
    
    
    
    # MEXA NOS VALORES DO H (PRIMEIRA COORDENADA) DO AZUL CLARO E DO AZUL ESCURO.
    # VEJA A DIFERENÇA NA CORES QUE APARECEM.
    # DEPOIS VOLTE ESSES VALORES PARA 110 E 170.
    
    # Quando eu coloco o azul claro no zero, fica tudo branco (Provavelmente começa a entender como se
    # tudo fosse azul claro
    # Já quando eu coloco o azul claro como 255, fica tudo preto. 
    #
    # Quando coloco o azul escuro como 0, fica tudo escuro 
    # Se eu coloco o azul escuro como 255, aumenta a area branca (Acho que aumenta o range do azul)
    #
    imagem_hsv = cvtColor(imagem_original, COLOR_BGR2HSV)
    azul_claro = (110, 0, 0)   # valores no espaço HSV
    azul_escuro = (255, 255, 255) # valores no espaço HSV
    mascara = inRange(imagem_hsv, azul_claro, azul_escuro)
    
    
    #imshow("Janela com Mascara2 para Tons de Azul", mascara)
    
    # Por fim, a gente pode usar a máscara para detectar regiões com uma certa cor 
    contornos,_ = findContours(mascara, RETR_TREE, CHAIN_APPROX_SIMPLE)
    
    # Agora podemos percorrer essas regiões
    for contorno in contornos:
        x, y, comprimento, altura = boundingRect(contorno)
        
        # Posso usar as coordenadas para desenhar retângulos.
        # Você vai perceber que haverá muitos retângulos pequenos.
        rectangle(imagem_com_azuis, pt1=(x,y), pt2=(x+comprimento,y+altura), color=(0,255,0), thickness=3)
        
        #Para desenhar o retangulo, passa o ponto esquerdo superior e o ponto direito inferior.
        
        #Par desenhar circulos
        #circle(imagem, (x,y), raio, color=(r,gb), thickness=espessura)
        
        #Para desenhar texto: O ponto x,y é o canto inferior esquerdo
        #putText(imagem, "texto" (x,y),color=(r,g,b), thickness=espessura, fontFace=FONT_HERSHEY_SIMPLEX, fontScale=tamanho)
    # Depois que o for terminar, exibimos a imagem com o resultado final.
    # Se você colocasse o imshow lá dentro, o programa ficaria bem lento!
        
    # DESCOMENTE A LINHA A SEGUIR PARA VER O RESULTADO, DEPOIS COMENTE NOVAMENTE.
    
    #imshow("Janela com Retangulos na Cor Escolhida", imagem_com_azuis)
        
    
    
    # FAÇA O FOR DOS CONTORNOS NOVAMENTE AQUI EMBAIXO, MAS COM ALGUMAS MODIFICAÇÕES
        # CONSIDERE APENAS RETÂNGULOS COM ÁREA MAIOR QUE 10000 (DEZ MIL)
        # DESENHE ESSES RETÂNGULOS NA IMAGEM ORIGINAL 
    # FORA DESSE FOR, MOSTRE A IMAGEM ORIGINAL MODIFICADA NUMA NOVA JANELA.
    azul_claro = (0, 0, 0)   # valores no espaço HSV
    azul_escuro = (255, 255, 255) # valores no espaço HSV
    mascara = inRange(imagem_original, azul_claro, azul_escuro)
    
    contornos,_ = findContours(mascara, RETR_TREE, CHAIN_APPROX_SIMPLE)
    
    for contorno in contornos:
        x, y, comprimento, altura = boundingRect(contorno)
        
        # Posso usar as coordenadas para desenhar retângulos.
        # Você vai perceber que haverá muitos retângulos pequenos.
        if altura*comprimento > 10000:
            print("oi")
            rectangle(imagem_original, pt1=(x,y), pt2=(x+comprimento,y+altura), color=(0,255,0), thickness=3)
    
    imshow("Janela com Retangulos imagem Original", imagem_original)
    # Essa é a etapa final padrão no while do OpenCV.
    # Ela mostra as imagens durante 1 milissegundo e interrompe loop quando a tecla q for pressionada.
    if waitKey(1) & 0xFF == ord("q"):
        break
    

# Quando o usuário interrompe o while, a gente libera a câmera e fecha as janelas.
stream.release()
destroyAllWindows()