# Project 09：4-Digit Digital Tube

1.  **Introduction**
    
The 4-digit 7-segment digital tube is a very practical display device, and it is used for devices such as electronic clocks and score counters. Due to the low price and it is easy to use, more and more projects will use 4-digit 7-segment digital tubes. In this project, we will use the Raspberry Pi Pico to control a 4-bit 7-segment digital tube to create a manual counter.



2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/b18fe281156b29c44796f72222718d58.jpeg" style="width:2.37431in;height:0.94514in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.67014in;height:1.28472in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/ee7a4ecd35ef268149e31fb9d62c8227.png" style="width:0.94792in;height:0.71736in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:0.90833in;height:0.23681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>4-Digit Digital Tube Module*1</td>
<td>220Ω Resistor*8</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td><p><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.50347in;height:1.23333in" /></p>
<p><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/723dc2c4078b7d3f84b7f1ae76edbabe.png" style="width:0in;height:0in" /><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/723dc2c4078b7d3f84b7f1ae76edbabe.png" style="width:0in;height:0in" /><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/723dc2c4078b7d3f84b7f1ae76edbabe.png" style="width:0in;height:0in" /></p></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Python/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:0.90694in;height:0.90069in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Breadboard*1</td>
<td>Jumper Wires</td>
<td></td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

![](/media/ce987bf9a2ab398945c98b34d3f8a003.png)

4-digital tube display:

The 4-digital tube display is is a semiconductor light-emitting device. Its basic unit is a light-emitting diode (LED). The digital tube display can be divided into 7-segment digital tube and 8-segment digital tube according to the number of segments. The 8-segment digital tube has one more LED unit than the 7-segment digital tube (used for decimal point display). Each segment of the 7-segment LED display is a separate LED.

According to the connection mode of the LED unit, the digital tube can be divided into a common anode digital tube and a common cathode digital tube.

In the common cathode 7-segment digital tube, all the cathodes (or negative electrodes) of the segmented LEDs are connected together, so you should connect the common cathode to GND. To light up a segmented LED, you can set its associated pin to“HIGH”.

Pins of control bit are G1, G2, G3 and G4.

![](/media/37113fa53213973132086c285d67686b.png)
![Img](./media/Project%2009：4-Digit%20Digital%20Tube.md/img-20231025163910.png)



4.  **Circuit Diagram and Wiring Diagram**

![Img](./media/Project%2009：4-Digit%20Digital%20Tube.md/img-20231025163933.png)

![](/media/6bf1bae6af0324d50a37ab7a0cabee11.png)

5.  **Test Code**

The code used in this project is saved in the file KS3025 Keyestudio Raspberry Pi Pico Learning Kit Complete Edition\\2. Windows System\\1.Python\_Tutorial\\2. Windows System\\1. Python\_Tutorial\\2. Python Projects\\Project 09：4-Digit Digital Tube. You can move the code to anywhere, for example, we can save the code in the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project 09：4-Digit Digital Tube”. And double left-click
the“Project\_09\_Four\_Digit\_Digital\_Tube.py”.

![](/media/e30515a97d87169cc191a0c9775b78b2.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>#Pin of each digit of nixie tube</p>
<p>a = machine.Pin(21, machine.Pin.OUT)</p>
<p>b = machine.Pin(28, machine.Pin.OUT)</p>
<p>c = machine.Pin(16, machine.Pin.OUT)</p>
<p>d = machine.Pin(18, machine.Pin.OUT)</p>
<p>e = machine.Pin(19, machine.Pin.OUT)</p>
<p>f = machine.Pin(22, machine.Pin.OUT)</p>
<p>g = machine.Pin(15, machine.Pin.OUT)</p>
<p>dp = machine.Pin(17, machine.Pin.OUT)</p>
<p>G1 = machine.Pin(20, machine.Pin.OUT)</p>
<p>G2 = machine.Pin(26, machine.Pin.OUT)</p>
<p>G3 = machine.Pin(27, machine.Pin.OUT)</p>
<p>G4 = machine.Pin(14, machine.Pin.OUT)</p>
<p>#digital tube a to dp corresponding development board pins</p>
<p>d_Pins=[machine.Pin(i,machine.Pin.OUT) for i in [21,28,16,18,19,22,15,17]]</p>
<p>#Pin corresponding to digital tube segment G1, G2, G3, and G4</p>
<p>w_Pins=[machine.Pin(i,machine.Pin.OUT) for i in [20,26,27,14]]</p>
<p>number=</p>
<p>def display(num,dp):</p>
<p>global number</p>
<p>count=0</p>
<p>for pin in d_Pins:#displays the value of num</p>
<p>pin.value(number[num][count])</p>
<p>count+=1</p>
<p>if dp==1:</p>
<p>d_Pins[7].value(0)</p>
<p>def clear():</p>
<p>for i in w_Pins:</p>
<p>i.value(0)</p>
<p>for i in d_Pins:</p>
<p>i.value(1)</p>
<p>def showData(num):</p>
<p>#the hundreds, thousands, ones, and fractional values of a numeric value</p>
<p>d_num=num</p>
<p>location=d_num.find('.')</p>
<p>if location&gt;0:</p>
<p>d_num=d_num.replace('.','')</p>
<p>while len(d_num)&lt;4:</p>
<p>d_num='0'+d_num</p>
<p>for i in range(0,4):</p>
<p>time.sleep(2)</p>
<p>clear()</p>
<p>w_Pins[3-i].value(1)</p>
<p>if i==location-1:</p>
<p>display(d_num[i],1)</p>
<p>else:</p>
<p>display(d_num[i],0)</p>
<p>if location&lt;0:</p>
<p>for i in range(0,4):</p>
<p>time.sleep(2)</p>
<p>clear()</p>
<p>w_Pins[3-i].value(1)</p>
<p>display(d_num[i],0)</p>
<p>while True:</p>
<p>num='9016'</p>
<p>showData(num)</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**
    
    Ensure that the Raspberry Pi Pico is connected to the computer，click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](/media/19d980c34958a8fa991e4e77874d42e5.png)

Click“![](/media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts executing, we will see that the 4-digit digital tube circularly displays numbers from 0000 to 9999. Press“Ctrl+C”or click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](/media/d3e34471566cfbac17835b73c11ad6fa.png)
