#include "pico.h"
#include "hardware/timer.h"

struct repeating_timer timer;
int i = -1;

bool timer_callback(struct repeating_timer *t) {
  digitalWrite(D0, LOW);
  digitalWrite(D1, LOW);
  digitalWrite(D2, LOW);

  i = (i + 1) % 3;
  digitalWrite(i, HIGH);
  return true;
}

void setup() {
  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  add_repeating_timer_ms(3000, timer_callback, NULL, &timer);
}

void loop() {}