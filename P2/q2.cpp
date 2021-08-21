// COLOQUE O SEU NOME AQUI: SUEMY INAGAKI PINHEIRO FAGUNDES
// COLOQUE A SUA MATRICULA AQUI: 1811208
#include <GFButton.h>
#include <ShiftDisplay.h>
#include <RotaryEncoder.h>
#include <Servo.h>
#include <EEPROM.h>
#define USE_TIMER_1 true


//declaracao dos componentes

GFButton botao1(A1);
GFButton botao2(A2);
GFButton botao3(A3);
ShiftDisplay display(9, 10, 13, COMMON_ANODE, 4, true);
RotaryEncoder encoder(20, 21);
Servo servo;
int pinServo = 2;



//variaveis globais
int angulo;
int posicaoAnterior = 0;
int vetor[] = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
int qtd = 0;
int indice = 1;
unsigned long instanteAnterior = 0;


int qtd_addr = 0;
int vetor_addr = qtd_addr + sizeof(int);

void tickDoEncoder(){
  encoder.tick();
}

void mostraAngulo(){
	int posicao = encoder.getPosition();
	if (posicao != posicaoAnterior) { //se movemos o encoder
		if(posicao > 180){
			encoder.setPosition(180);
		}
		if(posicao < 0){
			encoder.setPosition(0);
		}
		angulo = posicao;
		posicaoAnterior = posicao;
		char buffer [50];
		int n=sprintf(buffer, "%d%c",angulo, 'o');
		display.set(buffer);
	}	
}

void botao1Pressionado(GFButton& botaoDoEvento){
 	//por algum motivo, ele nao atualiza o vetor[qtd]
 	vetor[qtd] = angulo;
 	qtd++;
 	for(int i = 0; i < qtd; i++){
 		Serial.println(vetor[i]);
 	}
 	Serial.println("----");
 	if(qtd==10){
 		qtd = 0;
 	}
 	EEPROM.put(vetor_addr, vetor); //salvei o vetor
  	EEPROM.put(qtd_addr, qtd); //salvei a quantidade

}

void ajudtaAngulo(){
	unsigned long instanteAtual = millis();
	if(instanteAtual > instanteAnterior + 1500){
		if(indice <= qtd){
			servo.write(vetor[indice]);
			indice++;
			if(indice == qtd){
				indice = 0;
			}
		}
		instanteAnterior = instanteAtual;
		
	}
}
void setup() {
	Serial.begin(9600);
	EEPROM.get(vetor_addr, vetor); 
	EEPROM.get(qtd_addr, qtd); 

	servo.attach(pinServo, 1000, 2000);
	botao1.setPressHandler(botao1Pressionado);
	int origem1 = digitalPinToInterrupt(20);
	attachInterrupt(origem1, tickDoEncoder, CHANGE);
	int origem2 = digitalPinToInterrupt(21);
	attachInterrupt(origem2, tickDoEncoder, CHANGE);


}


void loop() {

	mostraAngulo();
	botao1.process();
	display.update();
	ajudtaAngulo();

}