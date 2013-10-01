int sensorTMP36Pin = A0;

void setup(){
  Serial.begin(9600);
}//setup
 
void loop(){
  delay(1000);

  unsigned int valorSensorTMP36 = analogRead(sensorTMP36Pin);  
  float miliVoltios = (valorSensorTMP36 * 5000.0) / 1024.0;
  float grados = (miliVoltios-500.0)/10.0;
  
  Serial.println("------------------------------");
  Serial.print("Valor entrada analógica: ");
  Serial.println( valorSensorTMP36 );
  Serial.print("mV: ");
  Serial.println(miliVoltios);
  Serial.print("Grados ºC: ");
  Serial.println(grados);
}//loop
