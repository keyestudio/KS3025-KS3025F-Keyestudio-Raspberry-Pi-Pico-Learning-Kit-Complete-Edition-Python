# Project 26：Rocker Control Light

1.  **Introduction**

The joystick module is a component with two analog inputs and one digital input. It is widely used in game operation, robot control, drone control and other fields.

In this project, we will use a Raspberry Pi Pico and a joystick module to control RGB. You can have a deeper understanding of the principle and operation of the joystick module in practice.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/b18fe281156b29c44796f72222718d58.jpeg" "width:2.37431in;height:0.94514in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" "width:1.67014in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/d087b123748cbfb8ed9f517150db71c5.png" "width:1.91042in;height:0.75139in" /></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Joystick Module*1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/af749ecbde89c728a8c63e6527781cac.png" "width:0.16806in;height:0.93194in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" "width:1.22639in;height:0.49236in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/c801a7baee258ff7f5f28ac6e9a7097b.png" "width:0.92778in;height:0.89167in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" "width:1.275in;height:0.68264in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/f1aed48e2c02214415853ad2358f3744.png" "width:1.21875in;height:1.02986in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/e65c16153d0ca27891c8c08092d96d5a.png" "width:0.47292in;height:1.15833in" /></td>
</tr>
<tr class="even">
<td>RGB LED*1</td>
<td>220ΩResistor*3</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
<td>M-F Dupont Wires</td>
<td>Breadboard*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

![Img](./media/img-20231025165420.png)



**Joystick module**: It mainly uses PS2 joystick components. In fact, the joystick module has 3 signal terminal pins, which simulate a three-dimensional space. The pins of the joystick module are GND, VCC, and signal terminals (B, X, Y). The signal terminals X and Y simulate the X-axis and Y-axis of the space. When controlling, the X and Y signal terminals of the module are connected to the analog port of the microcontroller. The signal terminal B simulates the Z axis of the space, it is generally connected to the digital port and used as a button.

VCC is connected to the microcontroller power output VCC (3.3V or 5V), GND is connected to the microcontroller GND, the voltage in the original state is about 1.65V or 2.5V. In the X-axis direction, when moving in the direction of the arrow, the voltage value increases, and the maximum voltage can be reached. Moving in the opposite direction of the arrow, the voltage value gradually decreases to the minimum voltage. In the Y-axis direction, the voltage value decreases gradually as it moves in the direction of the arrow on the module, decreasing to the minimum voltage. 

As the arrow is moved in the opposite direction, the voltage value increases and can reach the maximum voltage. In the Z-axis direction, the signal terminal B is connected to the digital port and outputs 0 in the original state and outputs 1 when pressed. In this way, we can read the two analog values and the high and low level conditions of the digital port to determine the operating status of the joystick on the module.

**Features:**

- Input Voltage：DC 3.3V \~ 5V

- Output Signal：X/Y dual axis analog value +Z axis digital signal.

- Range of Application ：Suitable for control point coordinate movement in plane as well as control of two degrees of freedom steering gear, etc.  

- Product feature s：Exquisite appearance, joystick feel superior, simple operation, sensitive response, long service life.  

4.  **Read the Value**

We have to use analog Raspberry Pi Pico pin IO to read the data from X or Y pins, and use digital IO port to read the values of the button. Please follow the wiring diagram below for wiring.

![](../media/36004a41553a2f413ba05775e9b696eb.png)

![](../media/b843cdff62b3ccf3f3f028a834b468aa.png)

The code used in this tutorial is saved in the file **...\\Python_Codes**. You can move the code to anywhere,for example,we can save the **Python_Codes** file in the Disk(D), the route is <span "color: rgb(0, 209, 0);">**D:\\Python_Codes**</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes”→“Project 26：Rocker control light”. And double left-click the“Project 26：Rocker control light.py”.

![](../media/21d8af01875dc2200fe145d78e94d63e.png)

```python
from machine import Pin, ADC
import time
# Initialize the joystick module (ADC function)
rocker_x = ADC(27)
rocker_y = ADC(26)
button = Pin(28, Pin.IN, Pin.PULL_UP)
# Read the value of the X axis and return [0, 1023]
def read_x():
value = int(rocker_x.read_u16() * 1024 / 65536)
return value
# Read the value of Y axis and return [0, 1023]
def read_y():
value = int(rocker_y.read_u16() * 1024 / 65536)
return value
# Read the state of the button, press to return to True, release to return to False
def btn_state():
press = False
if button.value() == 0:
press = True
return press
# Print the current value of the X axis,Y axis,Z axis cyclically.
while True:
value_x = read_x()
value_y = read_y()
state = btn_state()
print("x:%d, y:%d, press:%s" % (value_x, value_y, state))
time.sleep(0.1)
```


Ensure that the Raspberry Pi Pico is connected to the computer，click![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png) “Stop/Restart backend”.

![](../media/890604b49c6525bc64293f3f684ba9a8.png)

Click ![](../media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the analog and digital values of the current joystick. Moving the joystick or pressing it will change the analog and digital values in "Shell". Press“Ctrl+C”or click![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](../media/7d74a234d80b87a253a79c91a07fca47.png)

![](../media/c8097bd115d4c564192c19a08df2702a.jpeg)

![](../media/20904cf7c75d3dd861da3b3575670a0e.png)

5.  **Circuit Diagram and Wiring Diagram**

We just read the value of the joystick module. Now we need to do something with the joystick module and RGB, connecting according to the following diagram.

![](../media/000ec2c5dae0b0d5368569abbd026f35.png)

![](../media/68601044f75ee6840f0b97cad9bea891.png)

6.  **Test Code**

The code used in this tutorial is saved in the file **...\\Python_Codes**. You can move the code to anywhere,for example,we can save the **Python_Codes** file in the Disk(D), the route is <span "color: rgb(0, 209, 0);">**D:\\Python_Codes**</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes”→“Project 26：Rocker control light”. And double left-click the“Project 26：Rocker control light.py”.

![](../media/2195ead04e28141ca028bb7a6aecb1c3.png)

```python
from machine import Pin, PWM
import time
#Set RGB light interface and frequency
rgb_r = PWM(Pin(18))
rgb_g = PWM(Pin(17))
rgb_b = PWM(Pin(16))
rgb_b.freq(1000)
rgb_r.freq(1000)
rgb_g.freq(1000)
#Set rocker pin
rocker_y = machine.ADC(26)
rocker_x = machine.ADC(27)
y=500
x=500
while True:
y = rocker_y.read_u16()#Get Y value of rocker
x = rocker_x.read_u16()#Get X value of rocker
if x < 6400: #left
 rgb_b.duty_u16(0)
rgb_r.duty_u16(65535)
rgb_g.duty_u16(0)
elif x > 38400: #right
rgb_b.duty_u16(0)
rgb_r.duty_u16(0)
rgb_g.duty_u16(65535)
elif y < 6400: #down
rgb_b.duty_u16(65535)
rgb_r.duty_u16(0)
rgb_g.duty_u16(0)
elif y > 38400: #up
rgb_b.duty_u16(65535)
rgb_r.duty_u16(65535)
rgb_g.duty_u16(65535)
time.sleep(0.01)
```


7.  **Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click ![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”.

![](../media/a6446ce880f5eb7672672186f7ad3c89.png)

Click ![](../media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that ①If the joystick is moved to the far left in the X direction, the RGB light turns red. ② If the joystick is moved to the far right in the X direction, the RGB light turns green. ③If the joystick is moved to the top in the Y direction, the RGB light turns white. ④If the joystick is moved to the bottom in the Y direction, the RGB light turns blue. Press“Ctrl+C”or click![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](../media/15ab19c2c5e7334463b17a4f63cb381e.png)

![](../media/9c2d0d8777200827b16c49b752d45c4c.jpeg)
