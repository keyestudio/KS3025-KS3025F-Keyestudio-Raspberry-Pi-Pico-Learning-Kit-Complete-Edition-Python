# Project 01: Hello World

## 1. Introduction
    
For Raspberry Pi Pico beginners, we will start with some simple things. In this project, you only need a Raspberry Pi Pico and a USB cable to complete the "Hello World\!" project, which is a test of communication between Raspberry Pi Pico and the PC as well as a primary project.
    
## 2. Components

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/2e2bec86b3985dab2f1c07dfdb89ba73.jpeg" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3025-KS3025F-Keyestudio-Raspberry-Pi-Pico-Learning-Kit-Complete-Edition-Raspberry-Pi/master/media/3bdcc62cfa661d2b860a76e28537e21e.png" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

## 3. Wiring Up
    
In this project, we use a USB cable to connect the Raspberry Pi Pico to the computer.
    
![](../media/img-20231012090112.png)
    
## 4. Test Code
    
Connect the pico board to the Raspberry Pi, then the Thonny can compile or debug.
    
**Advantages：**
    
1\. You can use Thonny software to compile or debug programs.
    
2\. In the "<span style="color: rgb(255, 76, 65);">Shell</span>" window, you can view the error information and output results generated during the running of the program, and you can query related functional information online to help improve the program.
    
   
**Disadvantages：**

1\. You have to connect the pico board with the Raspberry Pi then run the Thonny.
    
2\. If disconnecting pico board and the Raspberry Pi and rebooting them, programming may fail.
    
Open Thonny and click![](../media/aedf8b88905c3cbb3c9c7015f14d3c74.png)“<span style="color: rgb(255, 76, 65);">Open...</span>”.
    
![](../media/0da7962f717a49547b37a223f78bd4c6.png)
    
Then click“<span style="color: rgb(255, 76, 65);">This computer</span>”.
    
![](../media/5bdbc66ef89b41a53e46696c07b2c282.png)
    
Select“**Project\_01\_HelloWorld.py**”and click“<span style="color: rgb(255, 76, 65);">OK</span>”.
    
Check the code in the folder <span style="color: rgb(255, 76, 65);">...\\4.Python_Tutorial(Raspberry-Pi)\\2. Projects</span>.
    
You can move the code anywhere. We copy the <span style="color: rgb(255, 76, 65);">**Python_Codes.ZIP**</span> to the <span style="color: rgb(0, 209, 0);">pi folder of the Raspberry Pi system</span>.
    
<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes</span>
<br>
<br> 

![](../media/d2395e9b262a28bd14ae7727e4e1f8c4.png)

Click ![](/media/bb4d9305714a178069d277b20e0934b7.png)to run the code <span style="color: rgb(255, 76, 65);">Hello World\!</span>. Then Welcome Keyestudio will be displayed on the <span style="color: rgb(255, 76, 65);">**Shell**</span>.

![](../media/0e8e900658e71b157e1f5b41f224a93c.png)

**Exit online running**

When running online，click![](../media/32e03e9d4211e9ef97c1d2b18f05c902.png)“Stop /Restart backend”to exit

![](../media/92ea345930ed8be1b8e04b341f20f2b6.png)

**Test Code：**

```Python
print("Hello World!")
print("Welcome Keyestudio")
```
