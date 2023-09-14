// Задание: при удержании кнопки D1 должна гореть лампока D0
void setup() {
  pinMode(D0, OUTPUT);
  pinMode(D1, INPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(D0, !digitalRead(D1));
}
