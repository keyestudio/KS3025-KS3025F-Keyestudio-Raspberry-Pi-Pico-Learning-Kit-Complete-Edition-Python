# Project 29：Temperature Instrument

1.  **Introduction**
    
Thermistor is a kind of resistor whose resistance depends on temperature changes, which is widely used in gardening, home alarm system and other devices. Therefore, we can use this feature to make a temperature instrument.
    
2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><p><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/8f45d8141f23885af95f870ab64a859c.jpeg" "width:1.76389in;height:0.70278in" /></p></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" "width:1.66944in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/b45bb81bb3763377c63accce606ac5f2.png" "width:0.25in;height:1.11597in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/b395b1cd2678f87b3a34dec15659efbc.png" "width:1.52431in;height:1.00556in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Thermistor*1</td>
<td>10KΩResistor*1</td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/74ca4fa6d49dbd04de6a603c6e55a9ee.png" "width:1.15347in;height:0.9625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/e380dd26e4825be9a768973802a55fe6.png" "width:0.56736in;height:1.38958in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/9232141f8a3166a8a6cdd43b78edd4e3.png" "width:1.29722in;height:0.625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" "width:1.10139in;height:1.03472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" "width:0.99028in;height:0.52986in" /></td>
</tr>
<tr class="even">
<td>10CM M-F Dupont Wires</td>
<td>Breadboard*1</td>
<td>LCD 128X32 DOT*1</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**
    

Thermistor: A thermistor is a temperature sensitive resistor. When it senses a change in temperature, the thermistor's resistance changes. We can use this feature to detect temperature intensity with thermistor. Thermistors and its electronic symbols are shown below:

![](../media/809b8634747fb295021f12e3b92b7894.png)

The relation between thermistor resistance and temperature is:
![Img](./media/img-20231025165842.png)

**In the formula:**

**Rt** is the resistance of the thermistor at T2 temperature.

**R** is the nominal resistance value of the thermistor at T1 room temperature.

**EXP\[n\]** is the nth power of e.

**B** is the temperature index

T1 and T2 refer to K degrees, that is, Kelvin temperature. Kelvin temperature =273.15 + Celsius temperature. For thermistor parameters, we use : B=3950, R=10KΩ，T1=25℃.The circuit connection method of thermistor is similar to that the photoresistor, as shown below :

![](../media/ac0d68aac58bffa5c99e1d0ed3a8bc37.jpeg)

We can use the value measured by the ADC converter to get the resistance value of the thermistor, and then use the formula to get the temperature value. Therefore, the temperature formula can be deduced as:
![Img](./media/img-20231025165900.png)

4.  **Read the Values**
    

First we will learn the thermistor to read the current ADC value, voltage value and temperature value and print them out . Please connect the wires according to the following wiring diagram.

![](../media/c143dc239ceaa5e65a63f47d6512630c.png)

![](../media/c0ad763fa1dda5ce55d03fe9b3d61bcd.png)

The code used in this tutorial is saved in the file **...\\Python_Codes**. You can move the code to anywhere,for example,we can save the **Python_Codes** file in the Disk(D), the route is <span "color: rgb(0, 209, 0);">**D:\\Python_Codes**</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes”→“Project 29：Temperature Instrument”. And double left-click the“Project 29：Temperature Instrument\.py”.

![](../media/ba1f9274b61caca4500172168941614c.png)

```python
from machine import Pin, ADC
import time
import math
#Set ADC
adc=ADC(27)
try:
while True:
adcValue = adc.read_u16()
voltage = adcValue / 65535.0 * 3.3
Rt = 10 * voltage / (3.3-voltage)
tempK = (1 / (1 / (273.15+25) + (math.log(Rt/10)) / 3950))
tempC = int(tempK - 273.15)
print("ADC value:", adcValue, " Voltage: %0.2f"%voltage + "V",
" Temperature: " + str(tempC) + "C")
time.sleep(1)
except:
pass
```


Ensure that the Raspberry Pi Pico is connected to the computer，click“![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](../media/2dd164403807ea7047143444407cc695.png)

Click ![](../media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will continuously display the thermistor's current ADC value, voltage value, and temperature value.  Try pinching the thermistor with your index finger and thumb (don't touch the wire) for a while, and you will see the temperature increase. Press“Ctrl+C”or click“![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](../media/b5c07f4cda023a43d086d41bd451b7cf.png)

![](../media/0a035900fbc73a112eced64a926872ad.png)

5.  **Circuit Diagram and Wiring Diagram**

<span "color: rgb(255, 76, 65);">Note :</span> LCD\_128X32\_DOT must be connected with a 10CM M-F Dupont wire, the LCD\_128X32\_DOT will display normally. Otherwise, using a 20CM M-F Dupont wire may cause the LCD\_128X32\_DOT display abnormally.  

![](../media/281774a4fbf4f7f2ca0fd1e60c89516c.png)

![](../media/91445212232765942d482b84da03f598.png)

6.  **Test Code**

The code used in this tutorial is saved in the file **...\\Python_Codes**. You can move the code to anywhere,for example,we can save the **Python_Codes** file in the Disk(D), the route is <span "color: rgb(0, 209, 0);">**D:\\Python_Codes**</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes”→“Project 29：Temperature Instrument”.
Select“lcd128\_32.py”and“lcd128\_32\_fonts.py”， right-click and select“**Upload to /**”，waiting for the “lcd128\_32.py”and“lcd128\_32\_fonts.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_29.2\_Temperature\_Instrument.py”.

![](../media/c5678862078fbd138bc2d3d841d6c184.png)

![](../media/9ebbc9f92556aa1a7ad8b4d9ff92debe.png)

![](../media/670f87b63caf3f2eec1fa383efc70902.png)

```python
from machine import Pin, ADC, I2C
import time
import math
import lcd128_32_fonts
from lcd128_32 import lcd128_32
#Set ADC
adc=ADC(27)
#i2c config
clock_pin = 21
data_pin = 20
bus = 0
i2c_addr = 0x3f
use_i2c = True
def scan_for_devices():
i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))
devices = i2c.scan()
if devices:
for d in devices:
print(hex(d))
else:
print('no i2c devices')
try:
while True:
adcValue = adc.read_u16()
voltage = adcValue / 65535.0 * 3.3
Rt = 10 * voltage / (3.3-voltage)
tempK = (1 / (1 / (273.15+25) + (math.log(Rt/10)) / 3950))
tempC = int(tempK - 273.15)
if use_i2c:
scan_for_devices()
lcd = lcd128_32(data_pin, clock_pin, bus, i2c_addr)
lcd.Clear()
lcd.Cursor(0, 0)
lcd.Display("Voltage:")
lcd.Cursor(0, 8)
lcd.Display(str(voltage))
lcd.Cursor(0, 20)
lcd.Display("V")
lcd.Cursor(2, 0)
lcd.Display("Temperature:")
lcd.Cursor(2, 12)
lcd.Display(str(tempC))
lcd.Cursor(2, 15)
lcd.Display("C")
time.sleep(0.5)
except:
pass
```

7.  **Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.
    
![](../media/d81b90ec4aca1c76d02f50c9858c6192.png)
    
 Click “![](../media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts executing, we will see that the LCD 128X32 DOT displays the voltage value of the thermistor and the temperature value in the current environment. Press“Ctrl+C”or click“![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](../media/39c7bd10b5bf436c42e552f697e9f9c0.png)
