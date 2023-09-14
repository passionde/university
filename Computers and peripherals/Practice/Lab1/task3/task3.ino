// Задание: светофор. Написать программу, которая по нажатии кнопки на пине D3 будет переключать лампочки (D0, D1, D2)
void setup() {
  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, INPUT);
}

PinStatus lastVal = HIGH;
int i = 0;

void loop() {
  PinStatus curVal = digitalRead(D3);

  if (curVal != lastVal) {
    lastVal = curVal;

    i = (i + !curVal) % 3;

    digitalWrite(D0, LOW);
    digitalWrite(D1, LOW);
    digitalWrite(D2, LOW);
  }
  
  digitalWrite(i, HIGH);
  delay(50);
}
