# Project 25：**Human Induction Lamp

## 1. Introduction
    
With the development of science and technology, the use of human induction lamp that usually used in the dark corridor area is very common in our real life, such as the corridor of the community, the bedroom of the room, the garage of the dungeon, the bathroom and so on. The human induction lamp are generally composed of a PIR Motion Sensor, a lamp, a photoresistor sensor and so on. In this project, we will learn how to use a PIR Motion Sensor, LEDs, and a photoresistor to make a human induction lamp.
    
## 2. Components Required

<table>
<tbody>
<tr class="odd">
<td><p><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/f70a6a892505b1816d151452b9b995a7.jpeg"  /></p></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png"  /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/9e553e75b6f976f33438171eb2f2e775.png" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/7eb361d680dfa351f07f8527aeb37abd.png" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/8cf9b1b3a5fec374cde3c5f0537567cb.png" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Photoresistor*1</td>
<td>Red LED*1</td>
<td>10KΩResistor*1</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/e380dd26e4825be9a768973802a55fe6.png" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/99272d75b3f952a0c2dd770e2f6f5a7c.png"/></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/51ab4ab6eefe8ba8f66234989d5282de.png"/></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/c80f7e0e045c10576b3120eea281502f.png" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" /></td>
<td></td>
</tr>
<tr class="even">
<td>Breadboard*1</td>
<td>PIR Motion Sensor*1</td>
<td>220ΩResistor*1</td>
<td>F-F Dupont Wires</td>
<td>Jumper Wires</td>
<td></td>
</tr>
</tbody>
</table>

## 3. Circuit Diagram and Wiring Diagram
    
![](../media/79c069794eed2b3eb611f4aee7952862.png)

![](../media/643c9552a922ed3ddde80be42481481d.png)

## 4. Test Code
 
You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. The path: <span style="color: rgb(255, 76, 65);">home/pi/Python_Codes</span>.

![](../media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes”→“Project 25：Human Induction Lamp”. And double left-click the “Project\_25\_Human\_ Induction\_Lamp.py”.

![](../media/f0b469934c60f65bb9c4f318551fd03b.png)

```Python
from machine import Pin, ADC
import time
 
# Human infrared sensor pin
human = Pin(2, Pin.IN)
 
# Initialize the photosensitive sensor pin to GP26 (ADC function)
light = ADC(26)
#create the External LED object from Pin 16, Set Pin 16 to output 
led1 = Pin(16, Pin.OUT)
#create the built-in LED on the Pico board from Pin 25, Set Pin 25 to output 
led2 = Pin(25, Pin.OUT) 
 
# Turn off the External LED
def led1_off():
    led1.value(0)
 
# Turn on the External LED
def led1_on():
    led1.value(1)
    
# Open the built-in LED on the Pico board
def led2_on():
    led2.value(1)
 
# Close the built-in LED on the Pico board
def led2_off():
    led2.value(0)
 
# Read the current analog value of the photosensitive sensor, range [0, 1023]
# The stronger the light intensity, the smaller the value.
def get_value():
    return int(light.read_u16() * 1024 / 65536)
 
 
def detect_someone():
    if human.value() == 1:
        return True
    return False
 
abc = 0
 
while True:
    val = get_value()
#     print('val=', val)
 
    if val >= 500:
        led2_on()
        if detect_someone() == True:
            abc += 1
            led1_on()
            print("value=", abc)
            time.sleep(1)
        else:
            if abc != 0:
                abc = 0
                led1_off()
    else:
        led2_off()
        led1_off()
 
    time.sleep(0.1)
```

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](../media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](../media/99cc13c8fe7576e631c0cf9147a324a7.png)

Click ![](../media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that When your hand covers the light-sensitive part of the photoresistor to simulate darkness, the Raspberry Pi Pico's built-in LED will light up. Then shake it in front of the PIR motion sensor with your other hand, the external LED will light up, too, and after a delay of a few seconds, the external LED will automatically turn off.  

At the same time, the "Shell" window of Thonny IDE will print the delay time when the external LED lights up . If the sensitive part of the photoresistor is not covered, you can see that the the Raspberry Pi Pico's built-in LED lights go out , at this time, shake in front of the PIR motion sensor with your hand, the external LED is off. 
Click“![](../media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](../media/1e713643e34dad2e48541a9ec20afbb9.png)

![](../media/af94ad9d2f008956592ee64e207aa8b5.png)



