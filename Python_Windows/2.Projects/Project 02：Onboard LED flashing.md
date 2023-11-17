# Project 02: Onboard LED flashing

1. **Introduction**

Raspberry Pi Pico has an onboard LED, which is a GP25 pin attached to the Raspberry Pi Pico. In this project, we will learn the effect of making the onboard LED blink. 

2. **Components**

| ![](media/image-20231030112709251.png) | ![](media/image-20231030112723844.png) |
| -------------------------------------- | -------------------------------------- |
| Raspberry Pi Pico*1                    | USB Cable*1                            |


3. **Wiring Up**
    

In this project, we use a USB cable to connect the Raspberry Pi Pico to the computer. Please refer to the documentation for the connection methods: Preparation for Python（Important）

![](media/image-20231030112835811.png)
4. **Test Code**

The code used in this tutorial is saved in the file **...\\Python_Codes**. You can move the code to anywhere,for example,we can save the **Python_Codes** file in the Disk(D), the route is <span style="color: rgb(0, 209, 0);">**D:\\Python_Codes**</span>..

**Code running online:**

Open“Thonny”，click“This computer”→“D:”→“Python_Codes”→“Project 02：Onboard LED flashing”.

![](../media/17519952e7c0019f1f0591903caa26d8.png)

Enter the file“Project 02：Onboard LED flashing”，double left-click the file“Project\_02\_Onboard\_LED\_flashing.py”, open it, as follows :

![](../media/87a877076f95cbe7d684ecc05de3e0cf.png)

```python
from machine import Pin
import time

led = Pin(25, Pin.OUT)   # create LED object from Pin 25, Set Pin 25 to output

try:
    while True:
        led.value(1)    # Set led turn on
        time.sleep(0.5) # Sleep 0.5s
        led.value(0)    # Set led turn off
        time.sleep(0.5) # Sleep 0.5s
except:
    pass
```


Ensure that the Raspberry Pi Pico is connected to the computer, click“![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”，then see what the **"Shell**" window displays.

![](../media/a53cb17aaa0b29d1c5f359f222868c69.png)

Click“![](../media/da852227207616ccd9aff28f19e02690.png)Run current script”， the code starts to execute, we will see that the LED on the Raspberry Pi Pico begins flashing. Press“Ctrl+C”or click“![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](../media/79796116d54281366ee2e4871dd4ca33.png)

![](media/image-20231030120025413.png)

<span style="color: rgb(255, 76, 65);">Note：</span>This is the code that runs online.  If you disconnect the USB cable and restart the Raspberry Pi Pico, the LEDS on the Raspberry Pi Pico will stop flashing. The following information will be displayed in the "Shell" window of Thonny software:  

![](../media/dde0b82feb441565c2bfa9517dedfed0.png)

Code running offline（upload the code to the Raspberry Pi Pico）：

Ensure that the Raspberry Pi Pico is connected to the computer, click“![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](../media/705d3bdd9cad821399137c7c0df72e86.png)

As shown in the following figure, right-click the file “Project\_02\_Onboard\_LED\_flashing.py” and select“**Upload to /**” to upload the code to the Raspberry Pi Pico.  

![](../media/4e83ee98b0da014fae6896f4fb14c889.png)

Upload main\.py in the same way.

![](../media/1591c6146bbcd2df9c9ba1aec14a86ca.png)

Disconnect the USB cable from the Raspberry Pi Pico and reconnect, and the LED will flash repeatedly. 


![](media/image-20231030120025413.png)

<span style="color: rgb(255, 76, 65);">Note:</span> The code here runs offline.  If you want to stop it and display the information in the "Shell" window, simply click ![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)"Stop/Restart Backend" in Thonny software.  

![](../media/f7ca5b1be220957141fb119e6cc4ab37.png)

