int i = -1;

void buttonPressed() {
  digitalWrite(D0, LOW);
  digitalWrite(D1, LOW);
  digitalWrite(D2, LOW);

  i = (i + 1) % 3;
  digitalWrite(i, HIGH);
  delay(50);
}

void setup() {
  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  attachInterrupt(D3, buttonPressed, RISING);
}

void loop() {}