// the setup function runs once when you press reset or power the board
void setup() {
  pinMode(D0, OUTPUT);
  pinMode(D1, OUTPUT);
  pinMode(D2, OUTPUT);
  pinMode(D3, INPUT);
}

int i = 0;

void loop() {
  if (!digitalRead(D3)) {
    i = (i + !digitalRead(D3)) % 3;
    digitalWrite(D0, LOW);
    digitalWrite(D1, LOW);
    digitalWrite(D2, LOW);
  }
  
  digitalWrite(i, HIGH);
}
