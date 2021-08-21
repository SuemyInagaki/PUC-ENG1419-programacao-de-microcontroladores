#include <ShiftDisplay.h>
#define USE_TIMER_1 true
#include <TimerInterrupt.h>
#include <GFButton.h>

int tempo = 0;
bool vtempo = false;
int campainha = 3; 
GFButton botao1(A1);
GFButton botao2(A2);
GFButton botao3(A3);
ShiftDisplay display(4, 7, 8, COMMON_ANODE, 4, true); 
void setup() {
  // put your setup code here, to run once:
  pinMode(campainha, OUTPUT);
  digitalWrite(campainha, HIGH);
  botao1.setPressHandler(botao1Pressionado);
  botao2.setPressHandler(botao2Pressionado);
  botao3.setPressHandler(botao3Pressionado);
  ITimer1.init();
  ITimer1.attachInterruptInterval(1000, loopTimer);
}

void loop() {
  // put your main code here, to run repeatedly:
 botao1.process();
 botao2.process();
 botao3.process();

 display.set(((tempo/60)*100)+(tempo%60),0 ,2);
 display.changeDot(1, true);
 display.update();
}

void botao1Pressionado(GFButton& botaoDoEvento){
 tempo+=15;
}
void botao2Pressionado(GFButton& botaoDoEvento){
 tempo-=15;
 if (tempo < 0){
   tempo = 0;
 }
}
void botao3Pressionado(GFButton& botaoDoEvento){
 vtempo = true;
}
void loopTimer(){
  digitalWrite(campainha, HIGH);
  if(vtempo){
    tempo = tempo - 1;
    if (tempo <= 0){
      tempo = 0;
      vtempo = false;
      digitalWrite(campainha, LOW);
   }  
  }
}
