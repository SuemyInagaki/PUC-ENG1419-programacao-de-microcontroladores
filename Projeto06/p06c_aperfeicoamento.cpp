#include <ShiftDisplay.h>
#define USE_TIMER_1 true
#include <TimerInterrupt.h>
#include <GFButton.h>

int tempo[] = {0, 0, 0, 0};
bool vtempo[] = {false, false, false, false};
int indiceDaContagemAtual = 0;
int campainha = 3; 
GFButton botao1(A1);
GFButton botao2(A2);
GFButton botao3(A3);
int leds[] = {13, 12, 11, 10};
ShiftDisplay display(4, 7, 8, COMMON_ANODE, 4, true); 
void setup() {
  // put your setup code here, to run once:
  pinMode(campainha, OUTPUT);
  digitalWrite(campainha, HIGH);
  botao1.setPressHandler(botao1Pressionado);
  botao2.setPressHandler(botao2Pressionado);
  botao3.setPressHandler(botao3Pressionado);
  pinMode(leds[0], OUTPUT);
  pinMode(leds[1], OUTPUT);
  pinMode(leds[2], OUTPUT);
  pinMode(leds[3], OUTPUT);
  digitalWrite(leds[0], LOW);
  digitalWrite(leds[1], HIGH);
  digitalWrite(leds[2], HIGH);
  digitalWrite(leds[3], HIGH);
  ITimer1.init();
  ITimer1.attachInterruptInterval(1000, loopTimer);
}

void loop() {
  // put your main code here, to run repeatedly:
 botao1.process();
 botao2.process();
 botao3.process();

 display.set(((tempo[indiceDaContagemAtual]/60)*100)+(tempo[indiceDaContagemAtual]%60),0 ,2);
 display.changeDot(1, true);
 display.update();
}

void botao1Pressionado(GFButton& botaoDoEvento){
 tempo[indiceDaContagemAtual]+=15;
}
void botao2Pressionado(GFButton& botaoDoEvento){
 tempo[indiceDaContagemAtual]-=15;
 if (tempo[indiceDaContagemAtual] < 0){
   tempo[indiceDaContagemAtual] = 0;
 }
}
void botao3Pressionado(GFButton& botaoDoEvento){
  if(vtempo[indiceDaContagemAtual] || tempo[indiceDaContagemAtual] == 0){
    digitalWrite(leds[indiceDaContagemAtual], HIGH);
    indiceDaContagemAtual++;
    if (indiceDaContagemAtual == 4){
      indiceDaContagemAtual = 0;
    }
    digitalWrite(leds[indiceDaContagemAtual], LOW);
  }
  else{
    vtempo[indiceDaContagemAtual] = true;
  }
}
void loopTimer(){
  digitalWrite(campainha, HIGH);
  for(int i=0; i < 4; i++){
    if(vtempo[i]){
    tempo[i] = tempo[i] - 1;
    if (tempo[i] <= 0){
      tempo[i] = 0;
      vtempo[i] = false;
      digitalWrite(campainha, LOW);
    }  
   }
  }
  
}
