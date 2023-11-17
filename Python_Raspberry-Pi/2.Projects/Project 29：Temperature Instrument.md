# Project 29：Temperature Instrument

## 1. Introduction
    
Thermistor is a kind of resistor whose resistance depends on temperature changes, which is widely used in gardening, home alarm system and other devices. Therefore, we can use this feature to make a temperature instrument.
    
## 2. Components Required

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/8f45d8141f23885af95f870ab64a859c.jpeg" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/b45bb81bb3763377c63accce606ac5f2.png" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/b395b1cd2678f87b3a34dec15659efbc.png" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Thermistor*1</td>
<td>10KΩResistor*1</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/74ca4fa6d49dbd04de6a603c6e55a9ee.png" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/e380dd26e4825be9a768973802a55fe6.png" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/9232141f8a3166a8a6cdd43b78edd4e3.png" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" /></td>
<td></td>
</tr>
<tr class="even">
<td>10CM M-F Dupont Wires</td>
<td>Breadboard*1</td>
<td>LCD 128X32 DOT*1</td>
<td>Jumper Wires</td>
<td></td>
</tr>
</tbody>
</table>

## 3. Component Knowledge
    
**hermistor:** A thermistor is a temperature sensitive resistor. When it senses a change in temperature, the thermistor's resistance changes. We can use this feature to detect temperature intensity with thermistor. Thermistors and its electronic symbols are shown below:

![](../media/809b8634747fb295021f12e3b92b7894.png)

The relation between thermistor resistance and temperature is:

**in the formula:**

**Rt** is the resistance of the thermistor at T2 temperature.

**R** is the nominal resistance value of the thermistor at T1 room temperature.

**EXP\[n\]** is the nth power of e.

**B** is the temperature index

T1 and T2 refer to K degrees, that is, Kelvin temperature. Kelvin temperature =273.15 + Celsius temperature. For thermistor parameters, we use : B=3950, R=10KΩ，T1=25℃.The circuit connection method of thermistor is similar to that the photoresistor, as shown below :

![](../media/ac0d68aac58bffa5c99e1d0ed3a8bc37.jpeg)

We can use the value measured by the ADC converter to get the resistance value of the thermistor, and then use the formula to get the temperature value. Therefore, the temperature formula can be deduced as:

![Img](./media/img-20231019153206.png)

## 4. Read the Values
    
First we will learn the thermistor to read the current ADC value, voltage value and temperature value and print them out . Please connect the wires according to the following wiring diagram.

![](../media/c143dc239ceaa5e65a63f47d6512630c.png)

![](../media/c0ad763fa1dda5ce55d03fe9b3d61bcd.png)

You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. The path: <span style="color: rgb(255, 76, 65);">home/pi/Python_Codes</span>.

![](../media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes”→“Project 29：Temperature Instrument”. And double left-click the“Project\_29.1\_Read\_the\_thermistor\_analog\_value.py”.

![](../media/67ffde6cfd9e5326ad581477a2b4b5c7.png)

```Python
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
        print("ADC value:", adcValue, "  Voltage: %0.2f"%voltage + "V",
              "  Temperature: " + str(tempC) + "C")
        time.sleep(1)
except:
    pass
```

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](../media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”.

![](../media/dc1304adc2ae7f4c578e67eb39561fcc.png)

Click “![](../media/b8c516557596c51f73780a628fc6a933.png)Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will continuously display the thermistor's current ADC value, voltage value, and temperature value.  Try pinching the thermistor with your index finger and thumb (don't touch the wire) for a while, and you will see the temperature increase. 
Press“Ctrl+C”or click“![](../media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”to exit the program.

![](../media/00a21ac15ac2615e42d42ccd8864db12.png)

![](../media/0a035900fbc73a112eced64a926872ad.png)

## 5. Circuit Diagram and Wiring Diagram

<span style="color: rgb(255, 76, 65);">Note:</span> LCD\_128X32\_DOT must be connected with a 10CM M-F Dupont wire, the LCD\_128X32\_DOT will display normally. Otherwise, using a 20CM M-F Dupont wire may cause the LCD\_128X32\_DOT display abnormally.  

![](../media/281774a4fbf4f7f2ca0fd1e60c89516c.png)

![](../media/91445212232765942d482b84da03f598.png)

## 6. Test Code

You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. The path: <span style="color: rgb(255, 76, 65);">home/pi/Python_Codes</span>.

![](../media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click “This computer”→“home”→“pi”→“Python_Codes”→“Project 29：Temperature Instrument”. Select“lcd128\_32.py”and“lcd128\_32\_fonts.py”， right-click and select“**Upload to /**”，waiting for the “lcd128\_32.py”and“lcd128\_32\_fonts.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_29.2\_Temperature\_Instrument.py”.

![](../media/06a29489b325bf473c101b759b20e141.png)

![](../media/a9a4c977abc25966eb569a3ce6d05fa4.png)

```Python
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

## 7. Test Result
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](../media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”.
    
![](../media/6055091673c845212b077aa1ee0a5062.png)
    
Click“![](../media/b8c516557596c51f73780a628fc6a933.png)Run current script”, the code starts executing, we will see that the LCD 128X32 DOT displays the voltage value of the thermistor and the temperature value in the current environment. 
Press“Ctrl+C”or click“![](../media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”to exit the program.

![](../media/9ba3d3dff27e9b7bd0fa0f2859c9b67e.png)



































