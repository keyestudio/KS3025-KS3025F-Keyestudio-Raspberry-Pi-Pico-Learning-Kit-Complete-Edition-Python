# Project 07: Flowing Water Light


## 1. Introduction

In our daily life, we can see many billboards made up of different colors of LED. They constantly change the light to attract the attention of customers. In this project, we will use Raspberry Pi Pico to control 10 LEDs to achieve the effect of flowing water.

## 2. Components Required

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/b18fe281156b29c44796f72222718d58.jpeg"  /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png"  /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/3ec5906fad2172708d449390140f55e6.png" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Red LED*10</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png"  /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/e380dd26e4825be9a768973802a55fe6.png"  /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/c801a7baee258ff7f5f28ac6e9a7097b.png" /></td>
<td></td>
</tr>
<tr class="even">
<td>220ΩResistor*10</td>
<td>Breadboard*1</td>
<td>Jumper Wires</td>
<td></td>
</tr>
</tbody>
</table>

## 3. Circuit Diagram and Wiring Diagram

![](../media/e6f92039d131685369db2d1ac2c30267.png)

..media/fc6e73a6664012c9a33262b50d6e256f.png)

**Note:**

How to connect the LED

![](../media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor

![](../media/55c0199544e9819328f6d5778f10d7d0.png)

## 4. Test Code

This project is to design and manufacture a flowing water light.  Here are the steps: first , turn on LED \#1, then turn it off.  Second, turn on LED \#2, then turn off... . Do the same for the 10 LEDs until the last one is turned off.  Repeating the process to achieve the "movement" of the water.


You can move the code to anywhere. For example, we save it in the pi folder of the Raspberry Pi system, the route is <span style="color: rgb(255, 76, 65);">home/pi/Python_Codes</span>.

![](../media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny, click“This computer”→“home”→“pi”→“Python_Codes”→”Project 07：Flowing Water Light”and double-click“Project\_07\_Flowing\_Water\_Light.py”

![](../media/7b5bf98a689171d60a3601f16e0ad283.png)

```Python
from machine import Pin
import time

#Use an array to define 10 GPIO ports connected to LED Bar Graph for easier operation.
pins = [16, 17, 18, 19, 20, 21, 22, 26, 27, 28]
#Use two for loops to turn on LEDs separately from left to right and then back from right to left
def showLed():
    for pin in pins:
        print(pin)
        led = Pin(pin, Pin.OUT)
        led.value(1)
        time.sleep_ms(100)
        led.value(0)
        time.sleep_ms(100)        
    for pin in reversed(pins):
        print(pin)
        led = Pin(pin, Pin.OUT)
        led.value(1)
        time.sleep_ms(100)
        led.value(0)
        time.sleep_ms(100)
          
while True:
    showLed()
```

## 5. Test Result：

Connect the pico board to the Raspberry Pi. Click![](../media/32e03e9d4211e9ef97c1d2b18f05c902.png)to check the Shell.

![](../media/909f8976896d54a32d84d7ac1f0537c1.png)

Click ![](../media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the 10 LEDs will light up like a flowing light. 
Click ![](../media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart backend”to exit the program.

![](../media/723dd7931ac070cf30719700f47f6850.png)

![](../media/912e2c3f88b522b89b9935548bae3bd9.png)
