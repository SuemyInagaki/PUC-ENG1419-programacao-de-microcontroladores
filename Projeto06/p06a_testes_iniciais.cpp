
#include <ShiftDisplay.h>
#include <GFButton.h>
#define USE_TIMER_1 true
#include <TimerInterrupt.h>

int led = 13;
int led2 = 12;
bool vled2 = false;
int conta_bt3 = 0;
GFButton botao2(A2);
GFButton botao3(A3);
ShiftDisplay display(4, 7, 8, COMMON_ANODE, 4, true); 

void setup () {
 Serial.begin(9600); 
 pinMode(led, OUTPUT);
 pinMode(led2, OUTPUT);
 digitalWrite(led, HIGH);
 digitalWrite(led2, HIGH);
 display.set(-4.12, 2);
 display.show(2000); 
 botao2.setPressHandler(botao2Pressionado);
 botao3.setPressHandler(botao3Pressionado);
 //botao2.setReleaseHandler(botaoSolto);
 ITimer1.init();
 ITimer1.attachInterruptInterval(2000, loopTimer);
}
void loop () {
 digitalWrite(led, LOW);
 botao2.process();
 botao3.process();
 display.set(conta_bt3);
 display.update();
}

void botao2Pressionado (GFButton& botaoDoEvento) {
 Serial.println("Botão 2 foi pressionado!");
 if(!vled2){
   digitalWrite(led2, LOW);
   vled2 = true;
 }
 else{
   digitalWrite(led2, HIGH);
   vled2 = false;
 }
 
}
void botaoSolto (GFButton& botaoDoEvento) {
 Serial.println("Botão foi solto!");
}
void botao3Pressionado(GFButton& botaoDoEvento){
 conta_bt3 = conta_bt3 + 1;
}
void loopTimer(){
  Serial.println(conta_bt3); 
}