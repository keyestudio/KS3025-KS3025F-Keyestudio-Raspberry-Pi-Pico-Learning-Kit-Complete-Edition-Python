# Project 07: Flowing Light

1.**Introduction**

In our daily life, we can see many billboards made up of different colors of LED. They constantly change the light to attract the attention of customers. In this project, we will use Plus control board with 5 LEDs to achieve the effect of flowing water.

2.**Components Required**

| ![img](media/wps1-16841103136428.png)  | ![img](media/wps2-16841103153619.jpg)  | ![img](media/wps3-168411031722410.jpg) |                                        |
| -------------------------------------- | -------------------------------------- | -------------------------------------- | -------------------------------------- |
| Raspberry Pi Pico*1                    | Raspberry Pi Pico Expansion Board*1    | Red LED*10                             |                                        |
| ![img](media/wps4-168411031900211.jpg) | ![img](media/wps5-168411032077012.jpg) | ![img](media/wps6-168411032274813.jpg) | ![img](media/wps7-168411032732414.jpg) |
| 220Ω Resistor*10                       | Breadboard*1                           | Jumper Wires                           | USB Cable*1                            |



3.**Circuit Diagram and Wiring Diagram**

![](../media/e6f92039d131685369db2d1ac2c30267.png)

![](../media/fc6e73a6664012c9a33262b50d6e256f.png)

**Note:**

How to connect the LED

![](../media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor

![](../media/55c0199544e9819328f6d5778f10d7d0.png)

4.**Test Code：**

You can open the code we provide:


```c
/* 
 * Filename    : Flowing Water Light
 * Description : Using ten leds to demonstrate flowing lamp.
 * Auther      : http//www.keyestudio.com
*/
byte ledPins[] = {16, 17, 18, 19, 20, 21, 22, 26, 27, 28};
int ledCounts;

void setup() {
  ledCounts = sizeof(ledPins);
  for (int i = 0; i < ledCounts; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
}

void loop() {
  for (int i = 0; i < ledCounts; i++) {
    digitalWrite(ledPins[i], HIGH);
    delay(100);
    digitalWrite(ledPins[i], LOW);
  }
  for (int i = ledCounts - 1; i > -1; i--) {
    digitalWrite(ledPins[i], HIGH);
    delay(100);
    digitalWrite(ledPins[i], LOW);
  }
}
```


Before uploading Test Code to Raspberry Pi Pico, please check the configuration of Arduino IDE.

Click "Tools" to confirm that the board type and ports.

![](../media/23c49983c355f1785cc22e197493f40d.png)

Click ![](../media/b0d41283bf5ae66d2d5ab45db15331ba.png) to upload the test code to the Raspberry Pi Pico board

![](../media/1127ab32e3472f3aa31842f80c15750c.png)

The code was uploaded successfully.

![](../media/66f2ab42322fb7b16c0e5821352e94ca.png)

5.**Test Result：**

After burning the project code, connecting the wires and powering on, the 10 LEDs will gradually light up and then gradually go off.

![image-20230515082649234](media/image-20230515082649234.png)
