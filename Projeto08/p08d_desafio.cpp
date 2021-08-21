#include <ShiftDisplay.h>
#include <GFButton.h>
#include <RotaryEncoder.h>
#include <EEPROM.h>
#include <Servo.h>
#include <meArm.h>
#include <LinkedList.h>

//#define pi 3.14

enum MovementState
{
  Absolute,
  Relative
};

struct State 
{
  float X;
  float Y;
  float Z;
  bool clawState;
};

LinkedList<State> states;

int potenciometro = A5;
int pinX = A0;
int pinY = A1;
int pinA = 2;
int pinB = 3;
int pinC = 4;
int pinD = 5;
int pinE = 6;
int pinBase = 12;
int pinSholder = 11;
int pinElbow = 10;
int pinClaw = 9; 

int qtd_save = 0;

bool stateClaw = false;

MovementState stateMovement = Absolute;

float matrixState[4][4];

int global_addr = 0;
int qtd_addr = global_addr;
int save_state_addr = qtd_addr + sizeof(int);

int X=0;
int Y=130;
int Z=0;

meArm braco(
 180, 0, -pi/2, pi/2, // ângulos da base
 135, 45, pi/4, 3*pi/4, // ângulos do ombro
 180, 90, 0, -pi/2, // ângulos do cotovelo
 30, 0, pi/2, 0 // ângulos da garra
); 

GFButton btn_A(pinA);
GFButton btn_B(pinB);
GFButton btn_C(pinC);
GFButton btn_D(pinD);
GFButton btn_E(pinE);

void toggleClaw(GFButton& button){
  if(stateClaw){
    braco.openGripper();
    stateClaw = false;
  }
  else{
    braco.closeGripper();
    stateClaw = true;
  }
}

void toggleMode(GFButton& button){
  if(stateMovement==Absolute){
    stateMovement = Relative;
  }
  else{
    stateMovement = Absolute;
  }
  Serial.println(stateMovement);
}


void saveState(GFButton& button)
{
  State position;
  position.X = braco.getX();
  position.Y = braco.getY();
  position.Z = braco.getZ();
  position.clawState = stateClaw;
  states.add(position);

  EEPROM.put(save_state_addr + qtd_save*sizeof(State), position);
  qtd_save++;

  EEPROM.put(qtd_addr, qtd_save);
}

void move(GFButton& button){
  for(int i =0 ; i<qtd_save; i++)
  {
    braco.gotoPoint(
      states.get(i).X,
      states.get(i).Y,
      states.get(i).Z);
    if(states.get(i).clawState){
      braco.closeGripper();
    }
    else{
      braco.openGripper();
    }
    delay(500);
  }
}

void reset(GFButton& button)
{
  qtd_save=0;
  states.clear();
  EEPROM.put(qtd_addr, qtd_save);
}

void setup() {
  Serial.begin(9600);
  btn_A.setPressHandler(toggleClaw);
  btn_B.setPressHandler(toggleMode);
  btn_C.setPressHandler(saveState);
  btn_D.setPressHandler(move);
  btn_E.setPressHandler(reset);
  
  braco.begin(pinBase, pinSholder, pinElbow, pinClaw);
  braco.gotoPoint(X,Y,Z);

  EEPROM.get(qtd_addr, qtd_save);
  for (int i = 0; i< qtd_save; i++)
  {
    State t;
    EEPROM.get(save_state_addr + i*sizeof(State), t);
    states.add(t);
  }
}

void loop() {
  btn_A.process();  
  btn_B.process(); 
  btn_C.process();
  btn_D.process();
  btn_E.process();
  
  if(stateMovement==Absolute)
  {
    X = map(analogRead(pinX), 0, 1023, -150, 150);
    Y = map(analogRead(pinY), 0, 1023, 100, 200);
    Z = map(analogRead(potenciometro), 0, 1023, -30, 100);
    braco.gotoPoint(X,Y,Z);
  }
  else if(stateMovement == Relative)
  {
    int xSpeed = map(analogRead(pinX), 0, 1023, -10, 10)+1;
    int ySpeed = map(analogRead(pinY), 0, 1023, -10, 10)+1;
    
    if(X < -150)
      X = -150;
    else if(X > 150)
      X=150;
    else
      X = X + xSpeed;
    
    if (Y<100)
      Y=100;
    else if(Y > 200)
      Y=200;
    else
      Y = Y + ySpeed;
    
    Z = map(analogRead(potenciometro), 0, 1023, -30, 100);
    braco.goDirectlyTo(X,Y,Z);
    delay(50);
  }
}

