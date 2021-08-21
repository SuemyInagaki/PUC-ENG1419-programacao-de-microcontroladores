// COLOQUE O SEU NOME AQUI: SUEMY INAGAKI PINHEIRO FAGUNDES
// COLOQUE A SUA MATRICULA AQUI: 1811208
#include <GFButton.h>
#include <Adafruit_GFX.h>
#include <Adafruit_ILI9341.h>

GFButton botao1(A1);
GFButton botao2(A2);
GFButton botao3(A3);
int pinX = A8;
int pinY = A9;
unsigned long instanteAnterior = 0;
Adafruit_ILI9341 tela = Adafruit_ILI9341(8, 10, 9);

int xa = 120, ya = 160;
int X, Y;
int c = 0; //para saber se é a primeira vez do botao 1
int x_, y_;

void desenhaQuadrado(int x, int y){
	tela.fillRect(x-5, y-5, 10, 10, ILI9341_BLUE);
}

void botao1Pressionado(GFButton& botaoDoEvento){
	if(c != 0){
		tela.drawLine(x_, y_, X, Y, ILI9341_BLUE);
		x_ = X;
		y_ = Y;
	}
	else{
		x_ = X;
		y_ = Y;
		c++;
	}
}

void botao2Pressionado(GFButton& botaoDoEvento){
	tela.fillRect(11, 11, 218, 298, ILI9341_BLACK);
	tela.fillRect(115, 155, 10, 10, ILI9341_BLUE);
}
void setup() {
Serial.begin(9600);
  tela.begin();
  tela.fillScreen(ILI9341_BLACK);
  tela.drawRect(10, 10, 220, 300, ILI9341_WHITE);
  tela.fillRect(115, 155, 10, 10, ILI9341_BLUE);
  botao1.setPressHandler(botao1Pressionado);
  botao2.setPressHandler(botao2Pressionado);
  pinMode(pinX, INPUT);
  pinMode(pinY, INPUT); 


}

void loop() {
	botao1.process();
	botao2.process();
	unsigned long instanteAtual = millis();
	//Deixei esse tempo grande pq meu pc estava muito lento
	if(instanteAtual > instanteAnterior + 1000){
		tela.fillRect(xa-5, ya-5, 10, 10, ILI9341_BLACK);
		xa = X; ya = Y; //salva as posicoes anteriores
		X = map(analogRead(pinX), 0, 1023, -8, 8); //é o movimento do joystick
	    Y = map(analogRead(pinY), 0, 1023, -8, 8);
	    //multiplico por -1 pq quando o joystick esta para cima, ele vai pra baixo
	    //por causa do sentido positivo da tela
	    Y*=(-1);
	    if(xa + X <= 16){ //inclui o 11 por causa da borda
	    	X = 16; //11 + 5 pra contar a posicao do centro
	    }
	    if(xa + X >= 224){
	    	X = 224; //240 -11 - 5 para contar a posicao do centro e a largura da borda
	    }
	    if(ya + Y <= 16){
	    	Y = 16;
	    }
	    if(ya + Y >= 304){//240 - 11 - 5
	    	Y = 304;
	    }
	    X = X + xa; //é a posicao na tela
	    Y = Y + ya;
	    desenhaQuadrado(X, Y);
	    instanteAnterior = instanteAtual;
	}
	delay(200);

}