# Project 14: Mini Table Lamp

1.**Introduction**

Did you know that Arduino can light up an LED when you press a button?

In this project, we will use the Plus Mainboard, a key switch and an LED to make a small desk lamp.

2.**Components Required**

| ![img](media/wps13.png) | ![img](media/wps14-168412182610224.jpg) | ![img](media/wps15-168412182723625.jpg) | ![img](media/wps16-168412182831326.jpg) | ![img](media/wps17-168412182952627.jpg) |
| ----------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Raspberry Pi Pico*1     | Raspberry Pi Pico Expansion Board*1     | Button*1                                | Red LED*1                               | 10KΩ Resistor*1                         |
| ![img](media/wps18.jpg) | ![img](media/wps19-168412183317528.jpg) | ![img](media/wps20-168412183461429.jpg) | ![img](media/wps21-168412183602230.jpg) | ![img](media/wps22-168412183750231.jpg) |
| Breadboard*1            | 220Ω Resistor*1                         | USB Cable*1                             | Jumper Wires                            | Button Cap*1                            |

3.**Component Knowledge**

![](../media/5b8fea4657b47510d199f740fdcaaa9d.png)

**Button:** The button can control the circuit on and off. The circuit is disconnected when the button is not pressed. But it breaks when you release it. 

Why does it only work when you press it? It starts from the internal structure of the button, which is shown in the figure:

![](../media/d2a204e61c768f18924150db58aee093.png)

Before the button is pressed, 1 and 2 are on, 3 and 4 are also on, but 1, 3 or 1, 4 or 2, 3 or 2, 4 are off (not working). Only when the button is pressed, 1, 3 or 1, 4 or 2, 3 or 2, 4 are on.

The key switch is one of the most commonly used components in circuit design.

4.**Schematic diagram of the button:**

![image-20230424165637145](media/image-20230424165637145.png)


5.**Circuit Diagram and Wiring Diagram**

![](../media/0753a2a452e0292b31f79f9b6dabb0cc.png)

![](../media/a03a6553dc194ab61fb7b4d914740f90.png)

**Note:**

How to connect the LED

![](../media/f70404aa49540fd7aecae944c7c01f83.jpeg)

How to identify the 220Ω 5-band resistor and 10KΩ 5-band resistor

![](../media/55c0199544e9819328f6d5778f10d7d0.png)

![](../media/246cf3885dc837c458a28123885c9f7b.png)

6.**Test Code：**

You can open the code we provide:


```C
/* 
 * Filename    : Mini Table Lamp
 * Description : Make a table lamp.
 * Auther      : http//www.keyestudio.com
*/
#define PIN_LED    19
#define PIN_BUTTON 22
bool ledState = false;

void setup() {
  // initialize digital pin PIN_LED as an output.
  pinMode(PIN_LED, OUTPUT);
  pinMode(PIN_BUTTON, INPUT);
}

// the loop function runs over and over again forever
void loop() {
  if (digitalRead(PIN_BUTTON) == LOW) {
    delay(20);
    if (digitalRead(PIN_BUTTON) == LOW) {
      reverseGPIO(PIN_LED);
    }
    while (digitalRead(PIN_BUTTON) == LOW);
  }
}

void reverseGPIO(int pin) {
  ledState = !ledState;
  digitalWrite(pin, ledState);
}
```


Before uploading Test Code to Raspberry Pi Pico, please check the configuration of Arduino IDE.

Click "Tools" to confirm that the board type and ports.

![](../media/fb3c5d5bb135803dd629cae5e8eabc7c.png)

Click ![](../media/b0d41283bf5ae66d2d5ab45db15331ba.png) to upload the test code to the Raspberry Pi Pico board.

![](../media/c9c421a60ba0866cf2102cbe57d7fe28.png)

The code was uploaded successfully.

![](../media/47dd7f6786120f6f15d429407daa74f3.png)

7.**Result**

Burn the project code, connect the wires and power on first. Then press the button, the LED will turn on. Press the button again, the LED will turn off.
