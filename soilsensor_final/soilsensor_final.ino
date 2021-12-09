int vwet = 330;
int wet = 400;
int moisture = 0;
byte dpin =6;
void setup() {
Serial.begin(9600);
pinMode(6, OUTPUT);
}
void loop() {
 int value = analogRead(A0);
 if(value < vwet){
  Serial.println("mjög blautt");
  digitalWrite(dpin, LOW);
 }
 else if(value > vwet && value < wet){
  Serial.println("blautt");
 }
 else if(value > wet){
  Serial.println("þurrt");
  digitalWrite(dpin, HIGH);
 }
 delay(5000);
}
