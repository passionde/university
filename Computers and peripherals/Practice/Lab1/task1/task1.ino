// Задание: реализовать мигание лампочки D0
void setup() {
  pinMode(D0, OUTPUT);
}

void loop() {
  digitalWrite(D0, HIGH); 
  delay(50);  
  digitalWrite(D0, LOW);  
  delay(50); 
}
