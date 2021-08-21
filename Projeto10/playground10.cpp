#include <Adafruit_GFX.h>
#include <MCUFRIEND_kbv.h> //Biblioteca para exibir na tela
#include <TouchScreen.h> //biblioteca para o touch

MCUFRIEND_kbv tela; //Declara a tela
TouchScreen touch(6, A1, A2, 7, 300); //Declara o touch
const int TS_LEFT = 145, TS_RIGHT = 887, TS_TOP = 934, TS_BOT = 158; //constntes de calibração

/*

A Origem do plano cartesiano começa no canto superior esquerdo 
E cresce para a direita e pra baixo: 

(0,0) ----->
|          |
|          |        
|          |
|          |
|          |
|          v
v---------->(240,320)


*/


void setup(){
    tela.begin(tela.readID()); //inicializo a tela
    tela.fillScreen(TFT_BLACK); //preencho ela toda de preto
    
    //Exemplo para desenhar uma linha verde:
    tela.drawLine(10, 10, 60, 60, TFT_GREEN);
    
    //Exemplo para desenhar um circulo
    tela.fillCircle(150, 70, 50, TFT_YELLOW);
    
    //Desenhar borda do circulo
    tela.drawCircle(150, 70, 50, TFT_PINK);
    
    //OBS: é bom desenhar o preenchimento primeiro
    // Senão ele tampa o contorno. 
    
    //Desenhar um retangulo
    // Primeiro preenche
    // Depois contorna
    tela.fillRect(20, 150, 100, 120, TFT_RED);
    tela.drawRect(20, 150, 100, 120, TFT_WHITE);
    
    //Desenhar um triangulo
    tela.fillTriangle(50, 160, 70, 200, 90, 160, TFT_BLUE);
    
    //Desenhar textos:
    tela.setCursor(20, 100);
    tela.setTextColor(TFT_YELLOW);
    tela.setTextSize(4);
    tela.print("Jan K. S.");
    
    //Se eu quiser escrever outro texto, tem que começar a receita do zero

}

/*
    Eu posso colocar os comandos de desenho na loop tambem
    Mas eles sao muito demorados, entao o melhor é desenhar
    no mínimo de frequencia possivel

*/
void loop{

}



// Desenhar linha:
//tela.drawLine(x1, y1, x2, y2, cor);

// (x,y) do centro
//tela.fillCircle(x, y, raio, cor);
//tela.drawCircle(x, y, raio, cor);

// (x, y) do canto esquerdo superior
//tela.fillRect(x, y, comprimento, altura, cor);
//tela.drawRect(x, y, comprimento, altura, cor);

// Coordenada dos tres vertices do triangulo
//tela.fillTriangle(x1, y1, x2, y2, x3, y3, cor);
//tela.drawTriangle(x1, y1, x2, y2, x3, y3, cor);

//Desenhar textos na tela:
/*
1) SetCursor pra definir o local de inicio
2) SetTextColor
3) SetTextSize
4) Chama a print passando o texto a ser impresso


tela.setCursor(20, 100);
tela.setTextColor(TFT_YELLOW);
tela.setTextSize(4);
tela.print("Jan K. S.");
Se eu quiser escrever outro texto, tem que começar a receita do zero
*/

/*
    TOUCH SCREEN
    
    No setup, inicializo a serial:
    Serial.begin(9600);
    
    No loop:
    TSPoint ponto = touch.getPoint(); //isso desregula a tela para desenho
    pinMode(A1, OUTPUT); digitalWrite(A1, HIGH); //reconfigura pinos
    pinMode(A2, OUTPUT); digitalWrite(A2, HIGH); //para desenho
    
    int forca = ponto.z; //forca aplicada na tela
    if (forca > 200 && forca < 1000){
        if(millis() - instanteAnterior > 300){
            int x = map(ponto.x, TS_LEFT, TS_RT, 0, 240);
            int y = map(ponto.y, TS_TOP, TS_BOT, 0, 320);
            Serial.println(x + String(",") + y);
        }
        instanteAnterior = millis();
    }
    
    Mesmo quando entra no if, ele fica mostrando o forca = 0 por causa de bounce. 
    
    Para resolver, declarar o instante anterior como unsigned long  e usar a millis
    
    unsigned long instanteAnterior;
    
*/

/*
Para criar botoes na tela:

#include<JKSButton.h>

JKSButton botao;

botao.init(
    &tela, &touch, 
    xDoCentro, yDoCentro, comprimento, altura,
    corDaBorda, corDoFundo, corDoTexto,
    texto, tamanhoDoTexto
);

botao.setPressHandler(funcao1);
botao.setReleaseHandler(funcao2);


na loop:
    botao.process();
*/

