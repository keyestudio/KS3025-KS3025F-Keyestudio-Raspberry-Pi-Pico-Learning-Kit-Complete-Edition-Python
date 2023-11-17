# Project 24：Night Lamp

1.**Introduction**

Sensors or components are ubiquitous in our daily life. For example, some public street lights turn on automatically at night and turn off automatically during the day. Why? In fact, this make use of a photosensitive element that senses the intensity of external ambient light. 

When the outdoor brightness decreases at night, the street lights will automatically turn on. In the daytime, the street lights will automatically turn off. The principle of this is very simple. 

In this lesson we will use Raspberry Pi Pico to control LEDs to implement the function of this street light.



2.**Components Required**

| ![img](media/wps24.png) | ![img](media/wps25-168412379177468.jpg) | ![img](media/wps26-168412379651069.jpg) | ![img](media/wps27-168412379804570.jpg) | ![img](media/wps28-168412379930171.jpg) |
| ----------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Raspberry Pi Pico*1     | Raspberry Pi Pico Expansion Board*1     | Photoresistor*1                         | Red LED*1                               | 10KΩResistor*1                          |
| ![img](media/wps29.jpg) | ![img](media/wps30-168412380289172.jpg) | ![img](media/wps31-168412380416573.jpg) | ![img](media/wps32-168412380621474.jpg) |                                         |
| Breadboard*1            | 220ΩResistor*1                          | Jumper Wires                            | USB Cable*1                             |                                         |



3.**Component Knowledge**

![](../media/9e553e75b6f976f33438171eb2f2e775.png)

It is a photosensitive resistor, its principle is that the photoresistor surface receives brightness (light) to reduce the resistance. The resistance value will change with the detected intensity of the ambient light. 

With this property, we can use photoresistors to detect light intensity. Photoresistors and other electronic symbols are as follows:


![](../media/7d575da675a2f6cb511d28b801e2abaa.png)

The following circuit is used to detect changes in resistance values of photoresistors:

![](../media/5a7f7e641eb78007760a94151c1d80a5.png)

In the circuit above, when the resistance of the photoresistor changes due to the change of light intensity, the voltage between the photoresistor and resistance R2 will also change. 

Thus, the intensity of light can be obtained by measuring this voltage.



4.**Read the Analog Value**

We first use a simple code to read the value of the photoresistor, print it in the serial monitor. For wiring, please refer to the following wiring diagram.

![](../media/e3fde13b200927346e04b032373ce638.png)

![](../media/b97ff27ae10e3499c36312c8ee4881f8.png)

5.**Test Code**

```c
/*  
 * Filename    : Read Photosensitive Analog Value
 * Description : Basic usage of ADC
 * Auther      : http//www.keyestudio.com
*/
#define PIN_ANALOG_IN  26  //the pin of the photosensitive sensor

void setup() {
  Serial.begin(115200);
}

//In loop() function, analogRead is called to get the ADC value of ADC0 and assign it to adcVal. 
//Calculate the measured voltage value through the formula, and print these data through the serial port monitor.
void loop() {
  int adcVal = analogRead(PIN_ANALOG_IN);
  double voltage = adcVal / 1023.0 * 3.3;
  Serial.println("ADC Value: " + String(adcVal) + " --- Voltage Value: " + String(voltage) + "V");
  delay(500);
}
```


Before uploading Test Code to Raspberry Pi Pico, please check the configuration of Arduino IDE.

Click "Tools" to confirm that the board type and ports.

![](../media/c2667443dab2177d4c4e4cd6ffe5f3f5.png)

Click ![](../media/b0d41283bf5ae66d2d5ab45db15331ba.png) to upload the test code to the Raspberry Pi Pico board

![](../media/d6d4305c8c00bff5a5dee6e1bbf66025.png)

The code was uploaded successfully.

![](../media/18a8a63b39e1faafa934d0ccb3d0e405.png)

Upload the code to the Pico board, wire up and power up, open the serial monitor and set the baud rate to 115200. 

Then you can read the analog value of photoresistor. When the light intensity around the sensor gets dim, the analog value displayed on the serial monitor will gradually reduce. On the contrary, the analog value will gradually increase.

![](../media/b578ae0004b44405bac340bc62138a80.png)

6.**Circuit Diagram and Wiring Diagram**

Next, we make a light-control lamp.

The Raspberry Pi Pico takes the analog value of the sensor and then adjusts the brightness of the LED.

![](../media/b8e8d95bdc869bf76465fa73645db831.png)

![](../media/71f2886dc6fa97d02e2ecd0d429af71b.png)

You can open the code we provide:


```c
/*  
 * Filename    : Night Lamp
 * Description : Controlling the brightness of LED by photosensitive sensor.
 * Auther      : http//www.keyestudio.com
*/
#define PIN_ADC0    26  // the pin of the photosensitive sensor
#define PIN_LED     16  // the pin of the LED

void setup() {
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_ADC0, INPUT);
}

void loop() {
  int adcVal = analogRead(PIN_ADC0); //read the ADC value of photosensitive sensor
  analogWrite(PIN_LED, map(adcVal, 0, 1023, 0, 255));//map ADC to the duty cycle of PWM to control LED brightness.
  delay(10);
}
```


Before uploading Test Code to Raspberry Pi Pico, please check the configuration of Arduino IDE.

Click "Tools" to confirm that the board type and ports.

![](../media/f692a819a6a2d6bed8270e8aecde4c20.png)

Click ![](../media/b0d41283bf5ae66d2d5ab45db15331ba.png) to upload the test code to the Raspberry Pi Pico board

![](../media/6096a95c4680000fbfe297f52bdc558a.png)

The code was uploaded successfully.

![](../media/8d1f2a698fae68f8de0e1820f5ac288e.png)

7.**Test Results:**

After the project code is uploaded successfully and power up. when the light intensity gets weak, the LED will becomes brighter; otherwise, the LED will become darker.
