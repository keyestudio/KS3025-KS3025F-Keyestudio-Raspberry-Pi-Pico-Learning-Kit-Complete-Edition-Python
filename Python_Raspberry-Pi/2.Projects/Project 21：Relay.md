# Project 21：Relay

## 1. Introduction
    
In daily life, we generally use AC to drive electrical equipment, and sometimes we use switches to control electrical appliances. If the switch is directly connected to the AC circuit, once electricity leakage occurs, people are in danger. From a safety point of view, we specially designed this relay module with NO (normally open) and NC (normally closed) terminals. In this lesson we will learn a special and easy-to-use switch, which is the relay module.
    
## 2. Components Required

<table>
<tbody>
<tr class="odd">
<td><p><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/5207588df3059cf385957664d41e9ac6.jpeg"  /></p></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/bc08dc3772fc1fef6fa1e07bd81f6680.png"  /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/1ea87894c6aa8d475203e447ad5e930a.png" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/1fbdfe0569327d9a42600a54336bf7b5.png" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Relay Module*1</td>
<td>M-F Dupont Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

## 3. Component Knowledge
    
**Relay:** It is an "automatic switch" that uses a small current to control the operation of a large current.
    
Input voltage：3.3V-5V
    
Rated load：5A 250VAC (NO/NC) 5A 24VDC (NO/NC)
    
The rated load means that devices with dc voltage of 24V or AC voltage of 250V can be controlled using 3.3V-5V microcontrollers.  
    
**Schematic diagram of the Relay:**

![](../media/be1c90d2b52fc2489590e3f702a087bf.emf)

## 4. Wiring Diagram

![](../media/bfe4e5e68d12e715c50f8aa5797a689c.png)

![](../media/0e76ea13b2034301be2ecdfde7f21f1e.png)

## 5. Test Code

You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. <span style="color: rgb(255, 76, 65);">The path: home/pi/Python_Codes</span>.

![](../media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes”→“Project 21：Relay”. And double-click the“Project\_21\_Relay.py”.

![](../media/57310f17327299cc49eeca50bcd8b7c1.png)

```Python
from machine import Pin
import time

# create relay from Pin 16, Set Pin 16 to output 
relay = Pin(16, Pin.OUT)
 
# The relay is opened, COM and NO are connected on the relay, and COM and NC are disconnected.
def relay_on():
    relay(1)
 
# The relay is closed, the COM and NO on the relay are disconnected, and the COM and NC are connected.
def relay_off():
    relay(0)
 
# Loop, the relay is on for one second and off for one second
while True:
    relay_on()
    time.sleep(1)
    relay_off()
    time.sleep(1)
```

## 6. Test Result
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](../media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](../media/d7abc767223f8f73b7d9996316439607.png)

Click“![](../media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that the relay will cycle on and off, on for 1 second, off for 1 second.  At the same time, you can hear the sound of the relay on and off, and you can also see the change of the indicator light on the relay. Press“Ctrl+C”or click![](../media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart backend”to exit the program.

![](../media/61481c566efa37002db8b70970a81a5b.png)
