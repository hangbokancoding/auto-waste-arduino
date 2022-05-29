#include <LiquidCrystal_I2C.h>
#include <string.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

String cmd;

void setup() {
  Serial.begin(9600);

  lcd.init();
  lcd.backlight();
}

void loop() {
    if(Serial.available()){
      cmd = Serial.readString();
      int nameNum = cmd[0] - 48;
      char nameList[4][8] = {
        {'p','a','p','e','r'},
        {'p','l','a','s','t','i','c'},
        {'c','a','n'},
        {'v','i','n','y','l'}
        };
      char _name[8];
      strcpy(_name, nameList[nameNum]);
      char number[4] = {cmd[1], cmd[2], cmd[3], '%'};
      
      lcd.setCursor(0, 0);
      lcd.print(_name);
      
      lcd.setCursor(0, 1);
      lcd.print(number);

      Serial.println(_name);
      Serial.println(number);
    }
}
