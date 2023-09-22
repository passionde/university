int sensorValue = 0;
int outputValue = 0;

void setup() {
  analogWriteFreq(120);
}

void loop() {
  sensorValue = analogRead(A0);
  outputValue = map(sensorValue, 0, 4095, 0, 255);
  analogWrite(D0, outputValue);
}
