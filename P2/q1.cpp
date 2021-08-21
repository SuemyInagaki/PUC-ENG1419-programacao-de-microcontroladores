// COLOQUE O SEU NOME AQUI: SUEMY INAGAKI PINHEIRO FAGUNDES
// COLOQUE A SUA MATRICULA AQUI: 1811208
#include <GFButton.h>
#include <ShiftDisplay.h>
GFButton botao1(A1);
GFButton botao2(A2);
GFButton botao3(A3);

//declaracao componentes
ShiftDisplay display(9, 10, 13, COMMON_ANODE, 4, true); 
int leds[] = {22, 23, 24, 25};
int potenciometro = A10;
int anglebase = 90;
int angleombro= 90;

//Campainha passiva
int terra = A5;
int campainha = 5;

//Variaveis globais
int indiceLEDaceso = 0;
int indiceLEDanterior = 0;
int duracaoCampainha = 0;

//Funcoes
void botao1Pressionado(GFButton& botaoDoEvento){
 	digitalWrite(leds[0], LOW);
}

void botao1Solto(GFButton& botaoDoEvento){
 	digitalWrite(leds[0], HIGH);
}

void botao2Pressionado(GFButton& botaoDoEvento){
 	//apaga o led aceso anteriormente
 	digitalWrite(leds[indiceLEDanterior], HIGH);
 	
 	//atualiza o anterior
 	indiceLEDanterior = indiceLEDaceso;
 	//acende o led
 	digitalWrite(leds[indiceLEDaceso], LOW);
 	indiceLEDaceso++;
 	if(indiceLEDaceso == 4){
 		indiceLEDaceso = 0;
 	}
}
void botao3Pressionado(GFButton& botaoDoEvento){
 	duracaoCampainha = map(analogRead(potenciometro), 100, 1000, 0, 180);
 	tone(campainha, 293.0, duracaoCampainha);
 	//O enunciado nao pediu para tratar caso de toques seguidos no 
 	//Botao 3, entao nao coloquei o delay(duracaoCampainha)
 	unsigned long instanteAtual = millis(); //em ms
	double instanteEmFloat = instanteAtual/1000.0;
	display.set(instanteEmFloat, 1);
}

void setup(){
	Serial.begin(9600);
	pinMode(leds[0], OUTPUT);
	pinMode(leds[1], OUTPUT);
	pinMode(leds[2], OUTPUT);
	pinMode(leds[3], OUTPUT);
	digitalWrite(leds[0], HIGH);
	digitalWrite(leds[1], HIGH);
	digitalWrite(leds[2], HIGH);
	digitalWrite(leds[3], HIGH);
	
	pinMode(potenciometro, INPUT);

	pinMode(terra, OUTPUT);
	digitalWrite(terra, LOW);
	pinMode(campainha, OUTPUT);

	botao1.setPressHandler(botao1Pressionado);
	botao1.setReleaseHandler(botao1Solto); 
	botao2.setPressHandler(botao2Pressionado);
	botao3.setPressHandler(botao3Pressionado);
}

void loop(){
	botao1.process();
	botao2.process();
	botao3.process();
	display.update();
	
}