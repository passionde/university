// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin D0 as an output.
  pinMode(D0, OUTPUT);
  pinMode(D1, INPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(D0, !digitalRead(D1));
}
