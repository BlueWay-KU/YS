//analog input
int gasPin = A0 ;
int flamePin = A1;

//sensor vaue
int gas_val;
int flame_val;

void setup() {
  Serial.begin(9600);
}

void loop() {
  gas_val = analogRead(gasPin);
  flame_val = analogRead(flamePin);

  //Serial.print("smoke sensor: ");
  //Serial.println(gas_val);

  //Serial.print("flame sensor: ");
  //Serial.println(flame_val);

  if(gas_val>300 | flame_val<800){
    Serial.println("1");
  }
  else{
    Serial.println("0");
  }
  delay(1000);
}
