#include <stdio.h> 
#include <stdlib.h>

#include <wiringPi.h>

int IN1_PIN = 13; // GPIO 11 (23)
int IN2_PIN = 14; // GPIO 9 (21)

int main(int argc, char *argv[])
{
  if (wiringPiSetup() == -1) {
    printf("Error: setup failed.\n");
    return -1;
  }

  pinMode(IN1_PIN, OUTPUT);
  pinMode(IN2_PIN, OUTPUT);

  digitalWrite(IN1_PIN, 1);
  digitalWrite(IN2_PIN, 0);

  delay(3000); // 3 sec
  
  digitalWrite(IN1_PIN, 0);
  digitalWrite(IN2_PIN, 0);

  
  return 0;
}

