# Project 03：External LED Flashing 

**1. Description：**

There is an onboard LED in Raspberry Pi Pico,which is a GP25 pin attached to the Raspberry Pi Pico. In this project, we will learn the effect of making the onboard LED blink.

**2. Components**

| ![img](media/wps1.png) | ![img](media/wps2.jpg)              |
| ---------------------- | ----------------------------------- |
| Raspberry Pi Pico*1    | Raspberry Pi Pico Expansion Board*1 |
| ![img](media/wps5.jpg) | ![img](media/wps6.jpg)              |
| Red LED*1              | 220Ω Resistor*1                     |
| ![img](media/wps7.jpg) | ![img](media/wps8.jpg)              |
| Breadboard*1           | Jumper Wire*2                       |
| ![img](media/wps9.jpg) |                                     |
| USB Cable*1            |                                     |



**3. Component Knowledge**

**LED:**

![image-20230424163655660](media/image-20230424163655660.png)

It is a kind of semiconductor called "light-emitting diode", which is an electronic device made of semiconductor materials (silicon, selenium, germanium, etc.). It has an anode and a cathode. The short lead (cathode) is grounded. The long lead (anode)is connected to 5V.

![](../media/f70404aa49540fd7aecae944c7c01f83.jpeg)

**Resistor**

A resistor is an electronic component in a circuit that restricts or regulates the flow current flow. Its unit is(Ω). 1 mΩ= 1000 kΩ，1kΩ=1000Ω.

![image-20230424163728269](media/image-20230424163728269.png)

We can use resistors to protect sensitive components, such as LEDs. The strength of the resistance is marked on the body of the resistor with an electronic color code. Each color code represents a number, and you can refer to it in a resistance card.

\-Color 1 – 1st Digit

\-Color 2 – 2nd Digit

\-Color 3 – 3rd Digit

\-Color 4 – Multiplier

\-Color 5 – Tolerance

![](../media/c3df005312cd9f6d4cdae6abf3cddb83.png)

In this kit, we provide eight 5-band resistors with different resistance values. Take three 5-band resistors as an example.

220Ω resistor\*10

![](../media/55c0199544e9819328f6d5778f10d7d0.png)

10KΩ resistor\*10

![](../media/246cf3885dc837c458a28123885c9f7b.png)

1KΩ resistor\*10

![](../media/19f5dfc51adfd79b04c3b164529767ed.png)

The connection between current, voltage, and resistance can be expressed by the formula: I=U/R. In the figure below, if the voltage is 3V, the current through R1 is: I = U / R = 3 V / 10 KΩ= 0.0003A= 0.3mA.

![](../media/b3eec552e4dfad361833730698621776.png)

**Breadboard**

A breadboard is used to build and test circuits quickly before finalizing any circuit design. The breadboard has many holes into which circuit components like integrated circuits and resistors can be inserted. A typical breadboard is as follows.

![](../media/612c1381811b2d780d5f6ed6a7ec3701.png)

The bread board has strips of metal which run underneath the board and connect the holes on the top of the board. The metal strips are laid out as shown below. Note that the top and bottom rows of holes are connected horizontally while the remaining holes are connected vertically.

![](../media/b45e70b961537035c85878b73d371725.png)

The first two rows (top) and the last two rows (bottom) of the breadboard are used for the positive (+) and negative (-) terminals of the power supply, respectively. The conductive layout of the breadboard is shown in the following diagram.

![](../media/d5478bd5eac558252cbc235479d979eb.png)

When we connect DIP (Dual In-line Packages) components, such as integrated circuits, microcontrollers, chips and so on, we can see that a groove in the middle isolates the middle part, so the top and bottom of the groove is not connected. DIP components can be connected as shown in the figure below.

![](../media/50caf14e911c4244779e99445c658db6.png)

![](../media/9b66ae2199e77fbc99b7b278dac0b567.png)

**4. Circuit Diagram and Wiring Diagram**

**How to use the keyestudio raspberry pico expansion board**

Stack the pico board onto the expansion board, as shown below;

![](../media/fae969ca3b1a4592a83a4e05f5795a5b.png)

Interface the pico board with your computer with a USB cable.

![image-20230424164204279](media/image-20230424164204279.png)



**5. Circuit diagrams and wiring diagram：**

Note: Cut off the pico board. Build up the circuit according to the circuit and wiring diagram.

Make sure the circuit is correct then connect the pico board to the computer.

<span style="color: rgb(255, 76, 65);">Note:</span> Avoid any possible short circuit (especially connecting 3.3V and GND)!

<span style="color: rgb(255, 76, 65);">WARNING:</span> Short circuits can cause large currents in the circuit, overheating components, and permanently damaging hardware.

**Circuit Diagram**

![](../media/cb069d7553d861e3293d8bdbe85bbd05.png)

**Wiring Diagram**

![](../media/898285da10fa9b39e52a02bc68758d27.png)


Note:

How to connect an LED

![](../media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω five-band resistor

![](../media/55c0199544e9819328f6d5778f10d7d0.png)

**6. Test Code：**

According to the circuit diagram, when Pico's GP16 outputs a high level, the LED will light up; when it outputs a low level, the LED light will be off. Therefore, we can make the LED flash repeatedly by controlling the GP16 to output high and low levels.

You can open the code we provide:


```c
/*
 * Filename    : External LED flashing
 * Description : Make an led blinking.
 * Auther      : http//www.keyestudio.com
*/
#define PIN_LED   16   //define the led pin

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED as an output.
  pinMode(PIN_LED, OUTPUT);
}

// the loop function runs over and over again forever
void loop() {
  digitalWrite(PIN_LED, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(500);                       // wait for 0.5s
  digitalWrite(PIN_LED, LOW);    // turn the LED off by making the voltage LOW
  delay(500);                       // wait for 0.5s
}
```


Before uploading Test Code to Raspberry Pi Pico, please check the configuration of Arduino IDE.

Click "Tools" to confirm that the board type and ports.

![](../media/d2dc892e6f83a37b57b02a9f05f7fc8a.png)

Click ![](../media/b0d41283bf5ae66d2d5ab45db15331ba.png) to upload the test code to the Raspberry Pi Pico board

![](../media/360c315c0d80aefa994add635bd31561.png)

The code was uploaded successfully.

![](../media/253f1992ddf73ca401dde1797fcfcfca.png)

**7. Test Result**

After the project code was uploaded successfully, the LED started flashing.

![image-20230515081316698](media/image-20230515081316698.png)
