# Project 07: Flowing Water Light

1.  **Introduction**

In our daily life, we can see many billboards made up of different colors of LED. They constantly change the light to attract the attention of customers. In this project, we will use Raspberry Pi Pico to control 10 LEDs to achieve the effect of flowing water.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/b18fe281156b29c44796f72222718d58.jpeg" style="width:2.37431in;height:0.94514in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.67014in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/3ec5906fad2172708d449390140f55e6.png" style="width:0.28056in;height:1.19722in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td><blockquote>
<p>Raspberry Pi Pico Expansion Board*1</p>
</blockquote></td>
<td>Red LED*10</td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:1.22639in;height:0.49236in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.50347in;height:1.23333in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/c801a7baee258ff7f5f28ac6e9a7097b.png" style="width:0.66736in;height:0.64097in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>220ΩResistor*10</td>
<td>Breadboard*1</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Circuit Diagram and Wiring Diagram**

![Img](./media/img-20231025163517.png)

![](../media/fc6e73a6664012c9a33262b50d6e256f.png)

**Note:**

How to connect the LED.

![](../media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor.

![](../media/55c0199544e9819328f6d5778f10d7d0.png)

4.  **Test Code**

This project is to design and manufacture a flowing water light.  Here are the steps: first , turn on LED \#1, then turn it off.  Second, turn on LED \#2, then turn off... . Do the same for the 10 LEDs until the last one is turned off. Repeating the process to achieve the "movement" of the water.

The code used in this tutorial is saved in the file **...\\Python_Codes**. You can move the code to anywhere,for example,we can save the **Python_Codes** file in the Disk(D), the route is <span style="color: rgb(0, 209, 0);">**D:\\Python_Codes**</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes”→“Project 07：Flowing Water Light”. And double left-click the“Project\_07\_Flowing\_Water\_Light.py”.

![](../media/a923fafe77f629ea8288ec40b52a6059.png)

```python
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


5.  **Test Result**
    

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.
    
![](../media/b908750521d4d2b64c55751825916a7e.png)
    
Click ![](../media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that the 10 LEDs will light up from left to right and then return from right to left. Press“Ctrl+C”or click“![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](../media/c9814fae261b7f8c9d2b33938d8e6144.png)


![Img](./media/img-20231025163603.png)
