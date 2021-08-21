#include <Adafruit_GFX.h>
#include <Adafruit_ILI9341.h>
#include <JKSButton.h>
#include <TouchScreen.h> 

JKSButton botaoDecolar;
JKSButton botaoPousar;
JKSButton botaoFrente;
JKSButton botaoDireita;
JKSButton botaoEsquerda;

Adafruit_ILI9341 tela = Adafruit_ILI9341(8, 10, 9);
TouchScreen touch(6, A1, A2, 7, 300);

void botaoDecolarPressed(JKSButton& botao){
  Serial.println("Decolar");
}

void botaoPousarPressed(JKSButton& botao){
  Serial.println("Pousar");
}

void botaoEsquerdaPressed(JKSButton& botao){
  Serial.println("esquerda");
}

void botaoDireitaPressed(JKSButton& botao){
  Serial.println("direita");
}

void botaoFrentePressed(JKSButton& botao){
  Serial.println("frente");
}

void release(JKSButton& botao){
  Serial.println("Parar");
}


void setup() {
  Serial.begin(9600);
  tela.begin();
  tela.fillScreen(ILI9341_BLACK);

  botaoDecolar.init(&tela, &touch, 60, 50, 100, 50, ILI9341_WHITE, ILI9341_GREEN, ILI9341_BLACK, "Decolar", 2); 
  botaoPousar.init(&tela, &touch, 180, 50, 100, 50, ILI9341_WHITE, ILI9341_RED, ILI9341_WHITE, "Pousar", 2); 
  botaoEsquerda.init(&tela, &touch, 35 , 120, 50, 50, ILI9341_WHITE, ILI9341_LIGHTGREY, ILI9341_BLACK, "<", 2);
  botaoFrente.init(&tela, &touch, 110 , 120, 50, 50, ILI9341_WHITE, ILI9341_LIGHTGREY, ILI9341_BLACK, "^", 2);
  botaoDireita.init(&tela, &touch, 190 , 120, 50, 50, ILI9341_WHITE, ILI9341_LIGHTGREY, ILI9341_BLACK, ">", 2);



  botaoDecolar.setPressHandler(botaoDecolarPressed);
  botaoPousar.setPressHandler(botaoPousarPressed); 
  botaoEsquerda.setPressHandler(botaoEsquerdaPressed);
  botaoDireita.setPressHandler(botaoDireitaPressed);
  botaoFrente.setPressHandler(botaoFrentePressed);
  botaoEsquerda.setReleaseHandler(release);
  botaoDireita.setReleaseHandler(release);
  botaoFrente.setReleaseHandler(release);
}

void loop() {
    botaoDecolar.process();
    botaoPousar.process();
    botaoFrente.process();
    botaoDireita.process();
    botaoEsquerda.process();
}

