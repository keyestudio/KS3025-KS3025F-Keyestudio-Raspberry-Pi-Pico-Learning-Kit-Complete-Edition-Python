# Project 23：Flame Alarm

1.  **Introduction**

Fire is a terrible thing and fire alarm systems are very useful in houses, commercial buildings and factories. In this project, we will use a Raspberry Pi Pico to control a flame sensor , a buzzer and LEDs to make fire alarm devices, which is a meaningful maker activity.
    

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><p><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/f70a6a892505b1816d151452b9b995a7.jpeg" style="width:1.55417in;height:0.61875in" /></p></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.66944in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/a50ec3e38adf10643eafac8cb62bec8a.png" style="width:0.20278in;height:1.25764in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/ef77f5a64c382157fc2dea21ec373fef.png" style="width:0.29514in;height:1.25903in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/4b4f653a76a82a3b413855493cc58fba.png" style="width:0.86111in;height:0.70069in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Flame Sensor*1</td>
<td>Red LED*1</td>
<td>Active Buzzer*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.59028in;height:1.44583in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/845d05a6108b1662b828610ba9dcb788.png" style="width:1.55833in;height:1.13681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/b395b1cd2678f87b3a34dec15659efbc.png" style="width:1.52431in;height:1.00556in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:0.77222in;height:0.77986in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>Breadboard</td>
<td>220ΩResistor*1</td>
<td>10KΩResistor*1</td>
<td>Jumper Wires</td>
<td>USBCable*1</td>
</tr>
</tbody>
</table>


3.  **Component Knowledge**

![Img](./media/img-20231025165217.png)


**Flame Sensor**：The flame emits a certain degree of IR light, which is invisible to the human eye, but our flame sensor can detect it and alert the microcontroller. If the Raspberry Pi Pico has detected a fire, it has a specially designed infrared receiver to detect the flame, and then convert the flame brightness into a fluctuating level signal. The short pin of the receiving triode is negative pole and the other long pin is positive pole. We should connect the short pin (negative pole) to 5V and the long pin (positive pole) to the analog pin, a resistor and GND. As shown in the figure below.

![](../media/87bd204db523c602c80745266c1ee452.png)

Note: Since vulnerable to radio frequency radiation and temperature changes, the flame sensor should be kept away from heat sources like radiators, heaters and air conditioners, as well as direct irradiation of sunlight, headlights and incandescent light.

4.  **Read the Simulation Value**

We start with a simple code to read the value of the flame sensor and print it on the serial monitor. For wiring, please refer to the following wiring diagram.

![](../media/85531078db041bba05599b3a1118a7bc.png)

![](../media/1e3c424f7cc7ac797ab0b8ae4a00f4f1.png)

The code used in this tutorial is saved in the file **...\\Python_Codes**. You can move the code to anywhere,for example,we can save the **Python_Codes** file in the Disk(D), the route is <span style="color: rgb(0, 209, 0);">**D:\\Python_Codes**</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes”→“Project 23：Flame Alarm”. And double left-click the“Project\_23.1\_Read\_Analog\_Value\_Of\_Flame\_Sensor.py”.

![](../media/1022a0e91bbb58b2ef61716f04ac94c5.png)

```python
from machine import ADC, Pin
import time
# Initialize the flame sensor to pin 26 (ADC function)
adc = ADC(26)
# Read the current analog value of the flame sensor and return [0, 1023]
def get_value():
return int(adc.read_u16() * 1024 / 65536)
# Print the current value of the flame sensor cyclically, value=[0, 1023]
while True:
value = get_value()
print(value)
time.sleep(0.1)
```

Click ![](../media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the simulation value read by the flame sensor. When the flame is close to the sensor, the simulation value increases. On the contrary, the simulated value decreases. Press“Ctrl+C”or click![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](../media/c3b2a4122662e655eb45e32937732991.png)

![](../media/7c04b9dd8c4a10e7b9788ecd95eeeeaa.png)

5.  **Circuit Diagram and Wiring Diagram**

Next, we will use a flame sensor, a buzzer, and LEDs to make an interesting project, that is flame alarm. When flame is detected, the LED flashes and the buzzer alarms.

![](../media/c2b7feb8039e618ba070a9714ef06554.png)

![](../media/0cd1ee17a6f8de81464817090c5832eb.png)

6.  **Test Code**
（Note：![](../media/40a3ea572836945268b22dfc0cce29c3.png) The threshold of 500 in the code can be reset itself as required)

The code used in this tutorial is saved in the file **...\\Python_Codes**. You can move the code to anywhere,for example,we can save the **Python_Codes** file in the Disk(D), the route is <span style="color: rgb(0, 209, 0);">**D:\\Python_Codes**</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes”→“Project 23：Flame Alarm”. And double left-click the “Project\_23.2\_Flame\_Alarm.py”.

![](../media/e2d832ba9e809f04f0990d9df446acf6.png)

```python
from machine import ADC, Pin
import time
# Initialize the flame sensor to pin 26 (ADC function)
adc = ADC(26)
# create LED object from Pin 16,Set Pin 16 to output
led = Pin(16, Pin.OUT)
# create buzzer object from Pin 17, Set Pin 17 to output
buzzer = Pin(17, Pin.OUT)
# Read the current analog value of the flame sensor and return [0, 1023]
def get_value():
return int(adc.read_u16() * 1024 / 65536)
# If the flame sensor detects a flame, the buzzer will beep
# and the LED will blink when the analog value is greater than 500
# Otherwise, the buzzer does not sound and the LED goes off
while True:
value = get_value()
if value >500:
buzzer.value(1) # Set buzzer turn on
led.value(1) # Set led turn on
time.sleep(0.5) # Sleep 0.5s
led.value(0) # Set led turn off
time.sleep(0.5) # Sleep 0.5s
else:
buzzer.value(0) # Set buzzer turn off
led.value(0) # Set led turn off
```



7. **Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”.

![](../media/5197b36be26f10de1b40e5c814974ab3.png)

 Click ![](../media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that when the flame sensor detects the flame, the LED flashes and the buzzer alarms. Otherwise, the LED does not light, the buzzer does not sound. Press“Ctrl+C”or click![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](../media/536af226e9ed390ca3cc102b0f02f9cb.png)
