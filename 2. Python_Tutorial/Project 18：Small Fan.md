# Project 18：Small Fan

1.  **Introduction**

In the hot summer, we need an electric fan to cool us down, so in this
project, we will use a Raspberry Pi Pico to control 130 motor module and
small blade to make a small fan.

2.  **Component Knowledge**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/b18fe281156b29c44796f72222718d58.jpeg" style="width:2.37431in;height:0.94514in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.67014in;height:1.28472in" /></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/5fe5f8cd6e75e7f8d4ec71f54a4ac2f5.png" style="width:0.87292in;height:0.37083in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/5eba8bae9e1d18b959ca425a9cc83fd2.jpeg" style="width:1.07569in;height:0.43472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/4e0b78edf6e4aeefa4c5191c606b2031.png" style="width:0.42847in;height:1.04931in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/655e6c465cb423279e0908513a983711.png" style="width:0.85694in;height:0.75347in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/df3db6765ee8c86beafa8410e87dd50d.png" style="width:0.77361in;height:0.76944in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>L293D Chip*1</td>
<td>DC Motor*1</td>
<td>Breadboard*1</td>
<td>Fan*1</td>
<td>Jumper Wore</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge:**

![](/media/5fe5f8cd6e75e7f8d4ec71f54a4ac2f5.png)

**L293D Chip：**

L293D is a direct current drive IC, which can be used to drive DC motor
or stepper motor in some robot projects.

It has a total of 16 pins and can drive two-channel DC motors at the
same time.

Its Input voltage range is 4.5 V \~ 36 V, the output current of per
channel is MAX 600mA, which can drive inductive loads. What’s more, its
input end can be directly connected and controlled by the single-chip
microcomputer.

When driving a small DC motor, the control of two-channel motors and the
forward and reverse rotation can be realized by changing the high and
low level of the input terminal. There are many motor drive boards using
L293D chips on the market, of course, we can also use it via simply
connecting.

**L293D Pin out：**

![](/media/2e5e0bd5b4577ac159d0568404dc21b5.png)

<table>
<tbody>
<tr class="odd">
<td>No</td>
<td>Name</td>
<td>Description</td>
</tr>
<tr class="even">
<td>1</td>
<td>Enable1,2</td>
<td>Enable pin Input 1(2)and Input 2(7)</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Input1</td>
<td>Directly input pin 1via digital circuit</td>
</tr>
<tr class="even">
<td>3</td>
<td>Output1</td>
<td>Connected to one end of motor1</td>
</tr>
<tr class="odd">
<td>4</td>
<td>GND</td>
<td>Grounded(0V)</td>
</tr>
<tr class="even">
<td>5</td>
<td>GND</td>
<td>Grounded(0V)</td>
</tr>
<tr class="odd">
<td>6</td>
<td>Output2</td>
<td>Connected to one end of motor1</td>
</tr>
<tr class="even">
<td>7</td>
<td>Input2</td>
<td>Directly output pin 2 via digital circuit</td>
</tr>
<tr class="odd">
<td>8</td>
<td>Vcc2 (Vss)</td>
<td>Connected to voltage pin of motor(4.5V-36V)</td>
</tr>
<tr class="even">
<td>9</td>
<td>Enable3,4</td>
<td>Enable pin 3(10)and 4(15)</td>
</tr>
<tr class="odd">
<td>10</td>
<td>Input3</td>
<td>Input3 pin, controlled by digital circuit</td>
</tr>
<tr class="even">
<td>11</td>
<td>Output3</td>
<td>Connected to one end of motor2</td>
</tr>
<tr class="odd">
<td>12</td>
<td>GND</td>
<td>Grounded(0V)</td>
</tr>
<tr class="even">
<td>13</td>
<td>GND</td>
<td>Grounded(0V)</td>
</tr>
<tr class="odd">
<td>14</td>
<td>Output4</td>
<td>Connected to one end of motor2</td>
</tr>
<tr class="even">
<td>15</td>
<td>Input4</td>
<td>Input4 pin, controlled by digital circuit</td>
</tr>
<tr class="odd">
<td>16</td>
<td>Vcc1(Vss)</td>
<td>Connect + 5V to enable IC function</td>
</tr>
</tbody>
</table>

4.  **Circuit diagram and wiring diagram：**

![](/media/40a4235ff016ce29140f3c7cedab4610.png)

![](/media/5d8dc14f86142189160f2c30f4641bb8.png)

5.  **Text Code**

The code used in this project is saved in the file KS3025 Keyestudio
Raspberry Pi Pico Learning Kit Complete Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 18：Small Fan. You can move
the code to anywhere, for example, we can save the code in the Disk(D),
the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
18：Small Fan”. And double left-click the“Project\_18\_ Small\_Fan.py”.

![](/media/9ba3903c9727ec2f3bf6061a79114c19.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>#Pin of each section of L293D and set as output</p>
<p>IN1_Pin = 17</p>
<p>IN2_Pin = 16</p>
<p>ENA_Pin = 18 #Control the speed of the motor</p>
<p># speed：speed，0-100</p>
<p># direction: Rotation direction,1 is clockwise,0 stops,-1 counterclockwise</p>
<p># speed_pin：Pin number that controls the start and stop of the motor</p>
<p>def motorRun(speed, direction, speed_pin, clockwise_pin, anti_clockwise_pin):</p>
<p>if speed &gt; 100: speed=100</p>
<p>if speed &lt; 0: speed=0</p>
<p>in1 = machine.Pin(anti_clockwise_pin, machine.Pin.OUT)</p>
<p>in2 = machine.Pin(clockwise_pin, machine.Pin.OUT)</p>
<p>pwm = machine.PWM(machine.Pin(speed_pin))</p>
<p>pwm.freq(50)</p>
<p>pwm.duty_u16(int(speed/100*65535))</p>
<p>if direction &lt; 0:</p>
<p>in2.value(0)</p>
<p>in1.value(1)</p>
<p>if direction == 0:</p>
<p>in2.value(0)</p>
<p>in1.value(0)</p>
<p>if direction &gt; 0:</p>
<p>in2.value(1)</p>
<p>in1.value(0)</p>
<p>while True:</p>
<p>motorRun(100, 1, ENA_Pin, IN2_Pin, IN1_Pin)</p>
<p>time.sleep(5)</p>
<p>motorRun(100, 0, ENA_Pin, IN2_Pin, IN1_Pin)</p>
<p>time.sleep(2)</p>
<p>motorRun(80, -1, ENA_Pin, IN2_Pin, IN1_Pin)</p>
<p>time.sleep(5)</p>
<p>motorRun(100, 0, ENA_Pin, IN2_Pin, IN1_Pin)</p>
<p>time.sleep(2)</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](/media/1806ed926b45c6b1d7d0b8643f2b22bf.png)

Click“![](/media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts
executing, we will see that The small fan turns counterclockwise for 5
seconds and stops for 2 seconds, and then turns clockwise for 5 seconds
and stops for 2 seconds. Repeat this rule for 5 times and then the small
fan stops. Press“Ctrl+C”or click“Stop/Restart backend”to exit the
program.

# ![](/media/2b0d6e736468ae337f52b36dfa2e7574.png)
