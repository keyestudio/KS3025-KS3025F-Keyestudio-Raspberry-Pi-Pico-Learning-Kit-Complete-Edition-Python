# Project 30：Keypad Door

1.  **Introduction**
    

In common digital button sensors, one button uses an IO port . However, sometimes it will occupy several IO ports when we need a lot of buttons . In order to save the use of IO ports, we are supposed to make a plurality of buttons into a matrix type, through the control of lines to achieve less IO port control the multiple buttons. In this project, we will learn a Raspberry Pi Pico and a 4\*4 membrane matrix keyboard control a servo and a buzzer.   
    
2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/ea74681ffd2116a2434692d34c25e829.jpeg" "width:1.92569in;height:0.76667in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" "width:1.66944in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/cd0bc424e9916881a1a903793821a042.png" "width:1.25417in;height:1.04792in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/4b4f653a76a82a3b413855493cc58fba.png" "width:0.86111in;height:0.70069in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Servo*1</td>
<td>Active Buzzer*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/fcd187eb009098d691927511606c991b.jpeg" "width:1.70972in;height:1.74931in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" "width:0.90694in;height:0.90139in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/e380dd26e4825be9a768973802a55fe6.png" "width:0.50347in;height:1.23333in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" "width:0.99028in;height:0.52986in" /></td>
</tr>
<tr class="even">
<td>Membrane Matrix Keyboard*1</td>
<td>Jumper Wires</td>
<td>Breadboard*1</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**
    

**4\*4 Matrix keyboard:** The keyboard is a device that integrates many keys. As shown in the figure below, a 4x4 keyboard integrates 16 keys.
    
![](../media/fcd187eb009098d691927511606c991b.jpeg)
    
As with the LED matrix integration, in the 4x4 keyboard, each row of keys is connected to a pin, each column of keys is the same. This connection reduces the use of processor ports. The internal circuit is shown below:
    
![](../media/5ebdacba906622079e0ef41dc1ea3fdf.png)

You can use row scan or column scan methods to detect the state of the keys on each column or each line. Take the column scan method as an example. Send a low level to column 4 (Pin4), detect the state of rows 1, 2, 3 and 4, and determine whether the A, B, C and D keys are pressed. Then send the low level to columns 3, 2, 1 in turn, and detect whether other keys are pressed. Then you can get the state of all keys.

4.  **Read the Value**
    

We start with a simple code to read the values of the 4\*4 matrix keyboard and print them in the serial monitor. Its wiring diagram is shown below.

![](../media/a673f15964984f61170e2d7690e959c1.png)

![](../media/681be86e91946320131d4b11b12b77c2.png)

The code used in this tutorial is saved in the file **...\\Python_Codes**. You can move the code to anywhere,for example,we can save the **Python_Codes** file in the Disk(D), the route is <span "color: rgb(0, 209, 0);">**D:\\Python_Codes**</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes”→“Project 30：Keypad Door”. Select“keypad\.py”， right-click and select“**Upload to/**”，waiting for“keypad\.py”to be uploaded to the Raspberry Pi Pico. And double left-click the “Project\_30.1\_4x4\_Matrix\_Keypad\_Display.py”.

![](../media/dbd629ecc3d6aa2517664241dfd82378.png)

![](../media/fc45dccc4f55940c69bd4619f83ddb16.png)

```python
from keypad import KeyPad
import time
keyPad = KeyPad(26, 22, 21, 20, 19, 18, 17, 16)
def key():
keyvalue = keyPad.scan()
if keyvalue != None:
print(keyvalue, end="\t")
time.sleep_ms(300)
return keyvalue
while True:
key()
```


Ensure that the Raspberry Pi Pico is connected to the computer，click![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”.

![](../media/768be990e8474f048c5c9a27aee3ac6a.png)

Click ![](../media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that press the keyboard and the "Shell" window of Thonny IDE will print the corresponding key value, as shown below. Press“Ctrl+C”or click![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](../media/c2aef97460cbf061a51e9da6217efadb.png)

![](../media/2f82f861d68daaaad8085b6a1bcc2e8d.png)

5.  **Circuit Diagram and Wiring Diagram**

In the last experiment, we have known the key values of the 4\*4 matrix keyboard. Next, we use it as the keyboard to control the servo and the buzzer.  

![](../media/f08b9ee128bc06300b3f8a05c73c2375.png)

![](../media/ccb5914d82d2b220e8a6afb944d13c54.png)

6.  **Test Code**

The code used in this tutorial is saved in the file **...\\Python_Codes**. You can move the code to anywhere,for example,we can save the **Python_Codes** file in the Disk(D), the route is <span "color: rgb(0, 209, 0);">**D:\\Python_Codes**</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes”→“Project 30： Keypad Door”. Select“keypad\.py”and“myservo\.py”， right-click and select“**Upload to /**”，waiting for the “keypad\.py”and“myservo\.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_30.2\_Keypad\_Door.py”.

![](../media/dbd629ecc3d6aa2517664241dfd82378.png)

![](../media/1e0349c41461a2894e0fcc1896b1f537.png)

![](../media/67282f4349b0196cc734e5ef8c1cbfa5.png)

```python
from myservo import Servo
from keypad import KeyPad
from machine import Pin
import time
keyPad = KeyPad(26, 22, 21, 20, 19, 18, 17, 16)
servo = Servo(2)
servo.ServoAngle(0)
activeBuzzer = Pin(0, Pin.OUT)
passWord = "1234"
keyIn = ""
def key():
keyvalue = keyPad.scan()
if keyvalue != None:
print('Your input:', keyvalue)
time.sleep_ms(200)
return keyvalue
while True:
keydata = key()
if keydata != None:
activeBuzzer.value(1)
time.sleep_ms(100)
activeBuzzer.value(0)
keyIn += keydata
if len(keyIn) == 4:
if keyIn == passWord:
print("passWord right!")
servo.ServoAngle(90)
time.sleep_ms(1000)
servo.ServoAngle(0)
else:
print("passWord error!")
activeBuzzer.value(1)
time.sleep_ms(1000)
activeBuzzer.value(0)
keyIn = ""
```


7.  **Test Result**
    

Ensure that the Raspberry Pi Pico is connected to the computer，click![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”.

![](../media/a3d47f9117b2df01852411444cc9c860.png)

Click ![](../media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that press the keyboard to enter a four-character password. If the password is correct (correct password: 1234), the servo will turn at an angle and return to its original position. If the input is incorrect, an input error alert will be issued. Press“Ctrl+C”or click![](../media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](../media/578f2921f4a88bbbda0fa18f62a579db.png)

![](../media/d45bd766b2b2630219f8bef283a07417.png)
