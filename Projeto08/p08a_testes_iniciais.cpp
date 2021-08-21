#include <ShiftDisplay.h>
#include <GFButton.h>
#include <RotaryEncoder.h>
#include <EEPROM.h>
#include <Servo.h>

Servo ombro;
Servo base;


int count = 0;
int global_addr = 0;
int potenciometro = A5;
int pinA = 2;
int pinB = 3;
int pinC = 4;
int pinD = 5;
int pinBase = 12;
int pinSholder =11;

int anglebase = 90;
int angleombro= 90;

GFButton btn_A(pinA);
GFButton btn_B(pinB);
GFButton btn_C(pinC);
GFButton btn_D(pinD);

void countTimes(GFButton& button)
{
  count++;
  Serial.println(count);
  EEPROM.put(global_addr, count);
}

void setup() {
  Serial.begin(9600);
  btn_B.setPressHandler(countTimes);

  EEPROM.get(global_addr, count);
  
  base.attach(pinBase, 1000, 2000);
  ombro.attach(pinSholder, 1000, 2000);
  
  base.write(anglebase);
  ombro.write(angleombro);

  pinMode(potenciometro, INPUT);
 // btn_2.setPressHandler();
 // btn_2.setReleaseHandler();
}

void loop() {
  btn_A.process();
  btn_B.process();
  btn_C.process();
  int poten_red = map(analogRead(potenciometro), 0, 1023, 0, 180);
  anglebase=poten_red;
  
  if(btn_A.isPressed())
  {
    if (angleombro > 45)
      angleombro -= 1;
  }
  
  if(btn_C.isPressed()){
    if(angleombro <= 135){
      angleombro+= 1;
    }
  }
  
  delay(15);
  base.write(anglebase);
  ombro.write(angleombro);

  //btn_2.process();
}

