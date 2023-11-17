# Project 29：Temperature Instrument

1.**Introduction**

LM35 is a commonly used and easy-to-use temperature sensor. It does not require other hardware, only needs an analog port. The difficulty lies in compiling the code and converting the analog values to Celsius temperature. 

In this project, we use a temperature sensor and 3 LEDs to make a temperature tester. When the temperature sensor touches objects with different temperature, the LED will show different colors.



2.**Components Required**

| ![img](media/wps36-168412922685432.png) | ![img](media/wps37-168412922822933.jpg) | ![img](media/wps38-168412923019734.jpg) |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Raspberry Pi Pico*1                     | Raspberry Pi Pico Expansion Board*1     | Photoresistor*1                         |
| ![img](media/wps39-168412923190235.jpg) | ![img](media/wps40-168412923404036.jpg) | ![img](media/wps41.jpg)                 |
| 10CMM-F Dupont Wires                    | Breadboard*1                            | LCD 128X32 DOT*1                        |
| ![img](media/wps44-168412924907737.jpg) | ![img](media/wps42-168412925202838.jpg) | ![img](media/wps43-168412925387839.jpg) |
| 10KΩ Resistor*1                         | Jumper Wires                            | USB Cable*1                             |



3.**Component Knowledge**

**Thermistor**: 

A thermistor is a temperature sensitive resistor. When it senses a change in temperature, the thermistor's resistance changes. We can use this feature to detect temperature intensity with thermistor. 

Thermistors and its electronic symbols are shown below:

![](../media/809b8634747fb295021f12e3b92b7894.png)

The relation between thermistor resistance and temperature is:

![img](media/wps45.png)

**In the formula:**

**Rt** is the resistance of the thermistor at T2 temperature.

**R** is the nominal resistance value of the thermistor at T1 room temperature.

**EXP\[n\]** is the nth power of e.

**B** is the temperature index

**T1** and **T2** refer to K degrees, that is, Kelvin temperature. Kelvin temperature =273.15 + Celsius temperature. For thermistor parameters, we use : B=3950, R=10KΩ，T1=25℃.

The circuit connection method of thermistor is similar to that the photoresistor, as shown below :

![](../media/ac0d68aac58bffa5c99e1d0ed3a8bc37.jpeg)

We can use the value measured by the ADC converter to get the resistance value of the thermistor, and then use the formula to get the temperature value. 

Therefore, the temperature formula can be deduced as:

![img](media/wps46-168412931966840.png)

4.**Read the Values**

First we will learn the thermistor to read the current ADC value, voltage value and temperature value and print them out . Please connect the wires according to the following wiring diagram.

![](../media/c143dc239ceaa5e65a63f47d6512630c.png)

![](../media/c0ad763fa1dda5ce55d03fe9b3d61bcd.png)

You can open the code we provide:


```c
/*  
 * Filename    : Read the thermistor analog value
 * Description : Making a thermometer by thermistor.
 * Auther      : http//www.keyestudio.com
*/
#define PIN_ADC1   27
void setup() {
  Serial.begin(115200);
}

void loop() {
  int adcValue = analogRead(PIN_ADC1);                            //read ADC pin
  double voltage = (float)adcValue / 1023.0 * 3.3;                // calculate voltage
  double Rt = 10 * voltage / (3.3 - voltage);                     //calculate resistance value of thermistor
  double tempK = 1 / (1 / (273.15 + 25) + log(Rt / 10) / 3950.0); //calculate temperature (Kelvin)
  double tempC = tempK - 273.15;                                  //calculate temperature (Celsius)
  Serial.println("Voltage: " + String(voltage) + "V,\t\t" + "Kelvins: " + String(tempK) + "K,\t" + "Temperature: " + String(tempC) + "C");
  delay(1000);
}
```


Before uploading Test Code to Raspberry Pi Pico, please check the configuration of Arduino IDE.

Click "Tools" to confirm that the board type and ports.

![](../media/c114be082fdeb240c12a32813fb911ba.png)

Click ![](../media/b0d41283bf5ae66d2d5ab45db15331ba.png) to upload the test code to the Raspberry Pi Pico board

![](../media/20f6bde6def6ce1f8163659dd18cf53b.png)

The code was uploaded successfully.

![](../media/9a0aba6cf84febc6e7a4a5f6040ec989.png)

Upload the code to the Raspberry Pi Pico successfully, power up with a USB cable, open the serial monitor and set the baud rate to 115200.

The serial monitor will display the current ADC value, voltage value and temperature value of the thermistor. Press the photoresistor, the temperature value will rise.

![](../media/8dbae0c204a8a98d74c7e58bef84d0d2.png)

Circuit diagram and wiring diagram:

<span style="color: rgb(255, 76, 65);">Note:</span> You must use a 10CM M-F DuPont wire to connect LCD\_128X32\_DOT,then LCD\_128X32\_DOT will display normally;

A 20CM long male-to-female DuPont cable is not required because the LCD\_128X32\_DOT display abnormally.

![](../media/281774a4fbf4f7f2ca0fd1e60c89516c.png)

![](../media/91445212232765942d482b84da03f598.png)

5.**Adding the lcd128\_32\_io library：**

If you added the **lcd128\_32\_io** library, just skip this step.

**Add the library as follows:**

Open Arduino IDE，click “Sketch”→“Include Library”→“Add .zip Library...”. Go to the folder...\\ Libraries\\LCD\_128X32.Zip，click LCD\_128X32.Zip then“Open”

![](../media/e384aaf34a3d9c5c14e76a76a973a236.png)

![](../media/7e9f9bb78e814f063632bd09762c85da.png)

6.**Test Code：**

You can open the code we provide:


```c
/*  
 * Filename    : Temperature Instrument
 * Description : LCD displays the temperature of thermistor.
 * Auther      : http//www.keyestudio.com
*/
#include "lcd128_32_io.h"

#define PIN_ADC1  27

lcd lcd(20, 21); //Create lCD128 *32 pin，sda->20， scl->21

void setup()  {
  lcd.Init(); //initialize
  lcd.Clear();  //clear
}
char string[10];

void loop() {
  int adcValue = analogRead(PIN_ADC1);                            //read ADC pin
  double voltage = (float)adcValue / 1023.0 * 3.3;                // calculate voltage
  double Rt = 10 * voltage / (3.3 - voltage);                     //calculate resistance value of thermistor
  double tempK = 1 / (1 / (273.15 + 25) + log(Rt / 10) / 3950.0); //calculate temperature (Kelvin)
  double tempC = tempK - 273.15;                                  //calculate temperature (Celsius)
  lcd.Cursor(0,0); //Set display position
  lcd.Display("Voltage:"); //Setting the display
  lcd.Cursor(0,8);
  lcd.DisplayNum(voltage);
  lcd.Cursor(0,11);
  lcd.Display("V");
  lcd.Cursor(2,0); 
  lcd.Display("tempC:");
  lcd.Cursor(2,8);
  lcd.DisplayNum(tempC);
  lcd.Cursor(2,11);
  lcd.Display("C");
  delay(200);
}
```


Before uploading Test Code to Raspberry Pi Pico, please check the configuration of Arduino IDE.

Click "Tools" to confirm that the board type and ports.

![](../media/42e0d9dc955098071cec9108e4021c55.png)

Click ![](../media/b0d41283bf5ae66d2d5ab45db15331ba.png) to upload the test code to the Raspberry Pi Pico board

![](../media/9ccafa73c3adeae97a88e5755583f276.png)

The code was uploaded successfully.

![](../media/c38fb4d16283a964daa459d79f6aed2a.png)

7.**Test Result：**

Upload the code and power up with a USB cable. The LCD 128X32 DOT will show the voltage value and temperature value.
