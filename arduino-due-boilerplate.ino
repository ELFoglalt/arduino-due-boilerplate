#include <Arduino.h>

#include <Wire.h>
#include <FDC2214.h>

int main() {
  init();
  pinMode(LED_BUILTIN, OUTPUT);

  while(true) {
    digitalWrite(LED_BUILTIN, HIGH);
    delay(500);
    digitalWrite(LED_BUILTIN, LOW);
    delay(500);
  }
}