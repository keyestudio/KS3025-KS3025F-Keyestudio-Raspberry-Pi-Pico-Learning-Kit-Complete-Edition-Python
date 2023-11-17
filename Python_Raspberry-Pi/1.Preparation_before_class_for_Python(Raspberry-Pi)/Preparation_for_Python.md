# Preparation_for_Python

### About Raspberry Pi：

Raspberry Pi is a card computer whose official system is Raspberry Pi OS, which can be installed on other systems, such as: ubuntu, Windows IoT. Raspberry Pi can be used as a personal server, a router, camera monitoring and recognition, as well as voice interaction by connecting a camera and a voice interactive assistant.

Furthermore, Raspberry Pi leads out 40Pin pins that can be connected to various sensors and control LEDs, motors, etc, making it can be used to create a robot.

## Install the Raspberry Pi OS System：

### 1\. Tools needed for the Raspberry Pi system：

#### 1.1. Hardware Tool：

（1）Raspberry Pi 4B/3B/2B （2）Above 16G TFT Memory Card

（3）Card Reader （4）Computer and other parts

#### 1.2. Software tools that need to be installed：

##### Windows System：

###### (1) Install putty

Download link：[https://www.chiark.greenend.org.uk/\~sgtatham/putty/](https://www.chiark.greenend.org.uk/~sgtatham/putty/)

![](../media/c26be4cd1f5543f20f275556ce5892c0.png)

![](../media/d888918aa7bf9e5ea94597aad1ee4224.png)

A.  After downloading the package file ![](../media/e597704d7033c7c3c5da06d4f561822c.png), double-click it and tap “Next”.

![](../media/01f1b2d98915be2be9c0c2a3d330dde2.png)

B.  Click “Next”.

![Img](./media/img-20231011162933.png)


C.  Select“Install Putty files”， and click“Install”。

![](../media/071a0acc98bb2dc5cd45d85dec72d111.png)

D.  After a few seconds, the installation is complete, click "Finish".

![](../media/ec368c3a549c09edd70f9786456d5430.png)

###### (2) Remote Login software -WinSCP

A. Download link：[https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)

B. After downloading the WinSCP software file![](../media/1719daa1002d7477ad4700e1df85d2df.png), double-click it then click![](../media/e09e48a32781d08aabb06156efe1de49.png).

![Img](./media/img-20231011163038.png)


C. Click“Accept”，then select the appropriate option and click“Next”, then click“Install”.

![](../media/9c652f54f6a7d53f6b2aedba40104a00.png)

![](../media/f32891714d5966037d59d1812aa15686.png)

![](../media/57d6139ba0aac9ca996bcbe6f6fd218f.png)

![](../media/49ffed878ee84546b156af3a0bf5556e.png)

D. After a few seconds, the installation is complete, click "Finish".

![](../media/14ffa1e11243835d30ffb933219dcef5.png)

###### (3) Format TFT card tool-- SD Card Formatter

A. Download link： [http://www.canadiancontent.net/tech/download/SD\_Card\_Formatter.html](http://www.canadiancontent.net/tech/download/SD_Card_Formatter.html)

![](../media/fa229f4e063572ce1c59574c308bf452.png)

![](../media/ac5d5eb9463805484b9239b99faf04eb.png)

B. Unzip the **SD CardFormatterv5\_WinEN** package and double-click the **SD Card Formatter** file![Img](./media/img-20231011163328.png) to run it.

![](../media/046c67e4072093ee3dad27e8088fcf9f.png)

C. Click“Next”，select“![Img](./media/img-20231011163436.png)”and click“Next”.

![](../media/384203e0b54ddfe37f18b65f70e786e5.png)

![](../media/cf4e91eac0c0573cff282256a915a01a.png)

D. Click “Next”again, and then click “Install”.

![](../media/0af58ee3afb14005a884ca2dc941157f.png)

![](../media/807623ddeea20c8b61503845d8aec9bc.png)

E. After a few seconds, the installation is complete, click "Finish".

![](../media/df2deb7e04c25ee207e994f0d2808194.png)

###### (4) Burn mirror system software tool--- Win32DiskImager

A. Download link：[https://sourceforge.net/projects/win32diskimager/](https://sourceforge.net/projects/win32diskimager/)

![](../media/4ffb55fd466198ca9524afbde7806271.png)

B. After downloading the software file![](../media/63c3eaf215c92c325f95613c9d8d49ce.png)，double-click it and then click“Run”.

![](../media/0f86f055a814207b0b09e1a7e6cb20bc.png)

C. After selecting![](../media/5cdab33a0a7ddd4ab5b2ca8cb04670be.png)，and click“Next”.

![](../media/d70ecd0554cbdbd60997a2356b55dc0d.png)

D. Click “Browse...”，select the location where Win32DiskImager is installed and click“Next”.

![](../media/1cdc2638bc1e9fe214344429f5e97a13.png)

E. Click “Browse...”，select the location where Win32DiskImager is installed and click “Next”.

![](./media/img-20231009162035.png)

F. Select![](../media/99d088dd3f9e62d94fe8d56bd4638d1d.png)and click“Next”，and then click“Install”.

![](../media/c03510a9961a0e7307945dff10de3550.png)

![](../media/0c9c0d647479ee984fc29c3cedc72c79.png)

G. After a few seconds, the installation is complete, click "Finish".

![](../media/1d75c6dd9ea4a2c437a2b655b713a1db.png)

###### (5) Scan for IP address software tool---WNetWatcher

Download Link：[http://www.nirsoft.net/utils/wnetwatcher.zip](http://www.nirsoft.net/utils/wnetwatcher.zip)

#### 1.3. Raspberry Pi mirror system

Download link for the latest version：

[https://www.raspberrypi.org/downloads/raspberry-pi-os/](https://www.raspberrypi.org/downloads/raspberry-pi-os/)

Download link for the old version：

- > Raspbian：

- > [https://downloads.raspberrypi.org/raspbian/images/](https://downloads.raspberrypi.org/raspbian/images/)

- > Raspbian full：

- > [https://downloads.raspberrypi.org/raspbian\_full/images/](https://downloads.raspberrypi.org/raspbian\_full/images/)

- > Raspbian lite：

- > [https://downloads.raspberrypi.org/raspbian\_lite/images/](https://downloads.raspberrypi.org/raspbian\_lite/images/)

We use the 2020.05.28 version in the tutorial and recommend you to use this version(Please download this version as shown in the picture below.)

[https://downloads.raspberrypi.org/raspios_full_armhf/images/raspios_full_armhf-2021-05-28/](https://downloads.raspberrypi.org/raspios_full_armhf/images/raspios_full_armhf-2021-05-28/)

![](../media/857946c171dd1f5617a0cbbdd2608baf.png)

### 2\. Install Raspberry Pi OS system on Raspberry Pi 4B:

#### 2.1. Connect the TFT memory card to a card reader, then plug the card reader into a computer’s USB port.

![Img](./media/img-20231011080903.jpg)

#### 2.2. Use the SD Card Formatter to format a TFT memory card, as illustrated below：

![](../media/79d747e6f00f857a593b3327397cc44f.png)

![](../media/cbc55902de71ce984d873ca2cb67fffa.png)

![](../media/82031b5354cc4edeccf2bfa7465b7c6c.png)

#### 2.3. Burn System:

（1）Use **Win32DiskImager** to burn the official **Raspberry Pi OS** mirror to the TFT memory card.

![](../media/80d236cae8bdf63d80dc65048ffb52b3.png)

![](../media/243d1ef34211eafe1a92b67fc0ee85a2.png)

![](../media/ea854c476e9a8d4f82dd4a7c714cd5af.png)

（2）After the mirror system is burned, don’t pull out the card reader, use a notepad to create a file named **SSH** and delete **.txt** , then copy it to the boot directory of the TFT card, so that you can open the SSH login function, as shown in the following figure:

![](../media/ffb73310322accd671da373bb2e71945.png)

（3） Pull out the card reader.

#### 2.4. Log in system:

（<span style="color: rgb(255, 76, 65);">The following operations require raspberry to share the same LOCAL area network with the PC</span>）

A. Insert the burned TFT memory card into the Raspberry Pi, connect internet cables and plug in power. If there is a screen and a HDMI cable of Raspberry Pi, connect the screen, and you can see the Raspberry Pi OS startup screen. If there is not a HDMI cable of Raspberry Pi, you can enter the desktop of Raspberry Pi via SSH remote login software---WinSCP and xrdp.

![Img](./media/img-20231011100454.png)


B. Use the WNetWatcher software to find the IP address of the Raspberry Pi.
![Img](./media/img-20231011114034.png)

C. If there is no IP address as shown in the figure above, follow the following steps to set it.

![Img](./media/img-20231011114043.png)

![Img](./media/img-20231011114047.png)

D. Once the setup is complete, record the IP and MAC addresses of the Raspberry Pi. As shown in the red box below, the MAC address of the Raspberry Pi is **b8:27:eb:17:16:01**, and the ip address is **192.168.0.57**. 

![Img](./media/img-20231011114112.png)

E. If you do not know the mac address and the ip address of the Raspberry Pi, then unplug the network cable of the Raspberry PI first, open the **WNetWatcher** query, and the detection times will be displayed on the right side of the interface. Connect the Raspberry Pi cable and query it once using **WNetWatcher**, and the Raspberry Pi address is detected one less time than the other addresses. Then write down the ip and mac addresses.

#### 2.5. Remote login

Enter default user name, password and host name on WinSCP to log in. Only a Raspberry Pi is connected in the same network.

![](../media/0a41d5c629ec98afbc31dc47ff5c18ec.png)

![](../media/ff64e71b9e30df60d0b099dbc2532587.png)

![Img](./media/img-20231011114258.png)

![Img](./media/img-20231011114428.png)

#### 2.6. View the ip address and mac address

![](../media/a4285a452978026c9e60c31d35974315.png)

Click to open terminal and input the password: <span style="color: rgb(255, 76, 65);">raspberry</span>, and tap“**Enter**”on keyboard.

![](../media/a433a9ee584c821a702d0250937e2ba8.png)

![](../media/7fb10d842cc7fd824a325d30fc3ecdc7.png)

After successfully login, open the terminal, input <span style="color: rgb(255, 76, 65);">ip a</span> and tap“**Enter**”keyboard to view the ip address and mac address.

![Img](./media/img-20231011115928.png)


#### 2.7. Fix the IP address of Raspberry Pi

IP address is changeable, therefore, we need to make IP address fixed for convenient use.

Follow the below steps:

Switch to root user

If without root user’s password

① Set root password

Input password in the terminal: **sudo passwd root** to set password.

② Switch to root user

Input **su root**

③ Fix the configuration file of IP address

Firstly change IP address of the following configuration file.

（<span style="color: rgb(255, 76, 65);">\#New IP address:：address 192.168.0.57</span>）

Copy the above new address to terminal and tap“**Enter**”keyboard.

**Configuration File:**

```
echo -e '

auto eth0

iface eth0 inet static

\#Change IP address

address 192.168.0.57

netmask 255.255.255.0

gateway 192.168.1.1

network 192.168.1.0

broadcast 192.168.1.255

dns-domain 119.29.29.29

dns-nameservers 119.29.29.29

metric 0

mtu 1492

'\>/etc/network/interfaces.d/eth0
```
Example operation diagram, as follows：

![Img](./media/img-20231012084519.png)


④ Reboot the system to activate the configuration file.

Input the restart command in the terminal: **sudo reboot**

You could log in via fixed IP afterwards.

⑤ Check IP to ensure IP address fixed well.

![Img](./media/img-20231011120412.png)

#### 2.8. Log in desktop on Raspberry Pi wirelessly

If we don't have an HDMI cable to connect to the display, can we wirelessly log in to the Raspberry Pi desktop from the Windows desktop? Yes, there are many methods, VNC and Xrdp are commonly used to log in desktop of Raspberry Pi wirelessly.

Let’s take an example of Xrdp.

①Install Xrdp Service in the terminal

Installation commands:

Switch to root User: <span style="color: rgb(255, 76, 65);">su root</span>

Installation commands: <span style="color: rgb(255, 76, 65);">apt-get install xrdp</span>

Enter y and tap“**Enter**”keyboard.

As shown below:

![](/media/aa59941ff4c1e582e8183c1dc3767fce.png)

Open the remote desktop connection on Windows

Press **WIN+R** on keyboard and enter **mstsc.exe**.

As shown below:

![](../media/e5a66a3a1c998f8feb1c21c7a457ec4e.png)

Enter the IP address of the Raspberry Pi, as shown below. Click “Connect” and then click “Connect”again. **192.168.0.57** is the ip address we use, you could change it into your IP address.

![Img](./media/img-20231011120551.png)

A prompt will appear and you can click“Yes”.

![](../media/297813f1370ce5c158fac61511f61295.png)

Then enter the user name: <span style="color: rgb(255, 76, 65);">pi</span> ,and the default password: <span style="color: rgb(255, 76, 65);">raspberry</span>, as shown below:

![Img](./media/img-20231011120636.png)

Click“OK”or tap“Enter”keyboard, you will view the desktop of Raspberry Pi OS, as shown below:

![](../media/56bd5693edd484c4433dc438b58c6130.png)

Now, we finish the basic configuration of the Raspberry Pi OS system.


## Preparations for Python

Python is a programming language that lets you work more quickly and integrate your systems more effectively.

Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

Next to pick up Python to control 40 pin of Raspberry Pi.

### Hardware：

**Raspberry Pi 4B：**

|                         |                           |
| ----------------------- | ------------------------- |
| **Raspberry Pi 4B**     | **Raspberry Pi 4B Model** |
| ![Img](./media/img-20231012085039.png)|  ![Img](./media/img-20231012085045.png) |

**Hardware Interfaces：**

![Img](./media/img-20231012085134.png)


**40-Pin GPIO Header Description：**

GPIO pins are divided into BCM GPIO number, physics number and WiringPi GPIO number.

We usually use WiringPi GPIO when using C language and BCM GPIO and physics number are used to Python, as shown below:

In these lessons, we use Python, so BCM GPIO number is adopted.

![Img](./media/img-20231012085157.png)

<span style="color: rgb(255, 76, 65);">Note:</span> pin(3.3 V) on the left hand is square, but other pins are round. Turn Raspberry Pi over, there is a square GPIO on the back.(you could tell from pin(3.3V).
 
![Img](./media/img-20231012085227.png)


<span style="color: rgb(255, 76, 65);">Note:</span> the largest current of each pin on Raspberry Pi 4B is 16mA and the aggregate current of all pins is not less than 51mA.

### Copy Example Code Folder to Raspberry Pi：

Place example code folder to the pi folder of Raspberry Pi. and extract the example code from <span style="color: rgb(255, 76, 65);">**Python_Codes.ZIP**</span> file, as shown below:

![](../media/e7b577a013d27250449f6a6062f2a692.png)

![Img](./media/img-20231012085344.png)

![Img](./media/img-20231012085349.png)

Double-click **Python_Codes** file to check **.py** files.

![Img](./media/img-20231012104408.png)


## Python
    
### Update the firmware of Micropython
    
If you want to run the MicroPython on the Pi Pico board, you need to upload a firmware to the pico board.

You can program via C language or MicroPython on the pico board. But you need to download the MicroPython firmware.

<span style="color: rgb(255, 76, 65);">Note:</span> MicroPython firmware is required to be downloaded once. You don’t need to download it again when programming with MicroPython. If you have downloaded the <span style="color: rgb(255, 76, 65);">.uf2</span> program firmware written in C language, the MicroPython firmware will be overwritten, so next time you use MicroPython, you need to follow the steps below to update the Raspberry Pi Pico's firmware.

### Download the firmward of Micropython

**Method 1:** 
A. Click ![Img](./media/img-20231012085859.png) to enter the website：[<span class="underline">https://www.raspberrypi.com/documentation/microcontrollers/</span>](https://www.raspberrypi.com/documentation/microcontrollers/)

![Img](./media/img-20231012085718.png)

![Img](./media/img-20231012085723.png)

B. Click“**MicroPython(**Getting started MicroPython**)**”to go to the firmware download page.

![Img](./media/img-20231012104341.png)


**Method 2：** 
Click![Img](./media/img-20231012085859.png) to open the browser，click [https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2](https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2) to download the firmware.

<span style="color: rgb(255, 76, 65);">Note：</span>Transfer the firmware（rp2-pico-20210902-v1.17.uf2）to the desktop of Raspberry pi imager

### Program the firmware of MicroPython

Connect a microUSB cable to the USB port of the pico board and computer.

Hold down **BOOTSEL**，and connect a microUSB cable to the USB port of the pico board.

![Img](./media/img-20231012090112.png)

Release the button, then there pops up a page.

Enter raspberry in the Password box, click **OK**.

The drive RPI-RP2 will appear on the desktop of the Raspberry Pi imager

<span style="color: rgb(255, 76, 65);">Note：</span>The latest Raspberry Pi mirroring system will not display the following dialog box, and the old version will display the following dialog box.

![Img](./media/img-20231012090303.png)

![Img](./media/img-20231012090307.png)


Click **OK** and open drive(RPI-RP2). Copy the file（rp2-pico-20210902-v1.17.uf2）to the RPI-RP2.

![Img](./media/img-20231012091858.png)

![Img](./media/img-20231012091902.png)


After the firmware is programmed, the Pico board will reboot. Then you can run Micropython.

### Serial Ports

The MicroPython firmware is equipped with a virtual USB serial port which is accessed through the micro USB connector on Raspberry Pi Pico. Your computer should notice this serial port and list it as a character device, most likely **/dev/ttyACM0**.

You can run <span style="color: rgb(255, 76, 65);">ls /dev/tty\*</span> to list your serial ports. There may be quite a few, but MicroPython’s USB serial will start with <span style="color: rgb(255, 76, 65);">/dev/ttyACM</span>. If in doubt, unplug the micro USB connector and see which one disappears. If you don’t see anything, you can try rebooting your Raspberry Pi.

Enter the following command to install minicom:

<span style="color: rgb(0, 252, 255);">sudo apt install minicom</span>
<br>
<br>

![Img](./media/img-20231012092054.png)

Select <span style="color: rgb(255, 76, 65);">Y</span> .

![Img](./media/img-20231012092112.png)

Enter the following commander, press **Enter** and open minicom.

<span style="color: rgb(0, 213, 255);">minicom -o -D /dev/ttyACM0</span>
<br>
<br>

![Img](./media/img-20231012092151.png)

![Img](./media/img-20231012092155.png)

Press **Ctrl + B** .

![Img](./media/img-20231012092213.png)

Enter <span style="color: rgb(255, 76, 65);">print("Hello World")</span> at the terminal and press Enter，then Hello World will be displayed.

![Img](./media/img-20231012092231.png)

### Install Thonny

The Raspberry Pi Imager that we downloaded comes with some commonly used software, and Thonny is among them.

![Img](./media/img-20231012093823.png)

If the Raspberry Pi Imager does not have Thonny, you need to manually download it yourself. Enter the following command in the terminal to download and install Thonny.

<span style="color: rgb(0, 213, 255);">sudo apt install thonny</span>
<br>
<br>

![Img](./media/img-20231012093845.png)

Open Thonny, click“**Switch to regular mode**”to switch modes, and click **OK** to reopen the Thonny.

![Img](./media/img-20231012093905.png)

![Img](./media/img-20231012093909.png)

### Connect the Raspberry Pi Pico on the Thonny

Click “**Python3.9.2**”and select“**MicroPython(Raspberry Pi Pico)**”

![Img](./media/img-20231012094028.png)

![Img](./media/img-20231012094032.png)


Click“**Tools**”→“**Options...**”

![Img](./media/img-20231012094047.png)


Select“**Micropython (generic)**”or “**Micropython (Raspberry Pi Pico)**”. How to choose Micropython(Raspberry Pi Pico)? As shown below;

![Img](./media/img-20231012094131.png)


Click“**Port**”to select corresponding “**port**” and click “**OK**”.

![Img](./media/img-20231012094232.png)

![Img](./media/img-20231012094237.png)


Click“**View**”→“**Files**”, then“**This computer**” and “**Raspberry Pi Pico**” will appear.

![Img](./media/img-20231012094321.png)

![Img](./media/img-20231012094327.png)

![Img](./media/img-20231012094331.png)

![Img](./media/img-20231012094335.png)

### Test Code

Test the Shell commander

Enter “**print(Hello World\!)**”in the Shell and press **Enter**” .

![Img](./media/img-20231012094438.png)

#### Online running：

To run Raspberry Pi Pico online, we need to connect the Raspberry Pi Pico to our computer, which allows us to compile or debug programs using Thonny software.  

<span style="color: rgb(255, 76, 65);">Advantages:</span> you can compile or debug programs using Thonny software.


Through the "Shell" window, we can view the error information and output results generated during the operation of the program, and query related function information online to help improve the program.  

<span style="color: rgb(255, 76, 65);">Disadvantages:</span> To run Raspberry Pi Pico online, you must connect Raspberry Pi Pico to a computer and run it with Thonny software.  

If the Raspberry Pi Pico is disconnected from the computer, when they reconnect, the program won't run again.  

<span style="color: rgb(0, 209, 0);">**basic operation:**</span>

Open Thonny and click ![Img](./media/img-20231012095316.png) “**Open...**”.

![Img](./media/img-20231012095335.png)

Click“**This computer**”.

![Img](./media/img-20231012095342.png)

Enter <span style="color: rgb(255, 76, 65);">home/pi/Python_Codes/Project 01: Hello World to select **Project\_01\_HelloWorld.py**</span>, and click “**OK**”.

![Img](./media/img-20231012095700.png)

Click ![Img](./media/img-20231012095540.png)“**Run current script to program Hello World\!.** **Welcome Keyestudio**" will be displayed on the "**Shell**".

![Img](./media/img-20231012095648.png)

#### Exit online

When running online, click “**![](/media/92a50d0579b5d50ea659a6b8930da44a.png)Stop /Restart Backend**” on Thonny to exit the program.  

![Img](./media/img-20231012095710.png)


#### Offline running code

When running offline, the Raspberry Pi Pico doesn't need to connect to a computer and Thonny.  Once powered up, it can run the <span style="color: rgb(255, 76, 65);">main.py</span> program stored in the Raspberry Pi Pico.  

**Pros**: We don't need to connect a computer to Thonny's software to run the program.  

**Cons**: The program stops automatically when an error occurs or the Raspberry Pi Pico runs out of power, and the code is hard to change.

<span style="color: rgb(255, 169, 0);">**Basic Operation:**</span>
<br>
<br>

Once powered up, the Raspberry Pi Pico will  check for the presence of main\.py on the device automatically.  If so, run the program in main\.py and go to the shell command system.  (<span style="color: rgb(255, 76, 65);">If we want the code to run offline, we can save it as main\.py</span>);  If the main\.py does not exist, go directly to the shell command system.  

<!-- end list -->

(1) Click “**File**”→“**New**”, create and write code.

![Img](./media/img-20231012100211.png)


(2) Enter the code in the newly opened file. Here we use the <span style="color: rgb(255, 76, 65);">Project\_02\_Onboard\_LED\_Flashing. Py</span> code as an example.  

![Img](./media/img-20231012100248.png)


(3) Click“**Save**”on the menu bar, we can save the code in This computer or MicroPython device.

![Img](./media/img-20231012100304.png)

<!-- end list -->

(4) Select“<span style="color: rgb(255, 76, 65);">MicroPython device</span>”，enter“<span style="color: rgb(255, 76, 65);">main\.py</span>”in the new pop-up window and click“**OK**”.

![Img](./media/img-20231012100343.png)

![Img](./media/img-20231012100347.png)

![Img](./media/img-20231012100351.png)

(5) Disconnect the microUSB cable to the Raspberry Pi Pico and reconnect, and the LEDs on the Raspberry Pi Pico will  flash repeatedly. 

![Img](./media/img-20231012100457.png)

#### Exit from Offline operation

Connect Raspberry Pi Pico to the computer，click![Img](./media/img-20231012101255.png)“**Stop/Restart backend**”on Thonny to end the offline operation.  

![Img](./media/img-20231012100517.png)


If it doesn’t work, click“**Stop/Restart backend**”on Thonny several times or reconnect to the Raspberry Pi Pico.

![Img](./media/img-20231012100532.png)

We provide a main\.py file to run offline.  The code added to main\.py is the bootstrap that executes the user code file. We just need to upload the offline project's code file (.py) to the "<span style="color: rgb(255, 76, 65);">MicroPython Device</span>".

Move the folder <span style="color: rgb(255, 76, 65);">**Python_Codes**</span> to the folder <span style="color: rgb(255, 76, 65);">**home/pi** of Raspberry Pi system</span> and open Thonny.

![](/media/aa2f0b276daa0dbffb031744c3083747.png)

② Expand **Project 00 : main** in .../home/pi/Python_Codes Projects. Double-click <span style="color: rgb(255, 76, 65);">**main\.py**</span> to make the code in "<span style="color: rgb(255, 76, 65);">**MicroPython Device**</span>"run offline.  

![Img](./media/img-20231012100941.png)

Here, we use project 00 and Project 02 cases as examples.  The results are displayed using an LED(GP25 pin) on a Raspberry Pi Pico.  If we have modified the Project\_02\_Onboard\_LED\_Flashing. Py file, then we need to modify it accordingly. Right-click the Project\_02\_Onboard\_LED\_Flashing. Py file and select '<span style="color: rgb(255, 76, 65);">**Upload to/**</span>' to upload the code to Raspberry Pi Pico, as shown below.  

![Img](./media/img-20231012101132.png)


Upload the main\.py in the same way.

![Img](./media/img-20231012101139.png)


Disconnect and reconnect the microUSB cable to the Raspberry Pi Pico, and the LEDs will flash repeatedly .

![Img](./media/img-20231012100457.png)

<span style="color: rgb(255, 76, 65);">Note:</span>

The code here runs offline.  If we want to stop running offline and go to "**Shell**", simply click ![Img](./media/img-20231012101229.png)"![](/media/0b9cf6411531d005d760df16819813e3.png)Stop/Restart Backend" on Thonny software.

![Img](./media/img-20231012101215.png)


### Thonny common operations

#### Upload the code to Raspberry Pi Pico

In the **Project 01：Hello World** file, right-click and select **Project\_01\_HelloWorld.py**，select“<span style="color: rgb(255, 76, 65);">**Upload to /**</span>”and upload the code to the root directory of the Raspberry Pi Pico.

![Img](./media/img-20231012102010.png)

#### Download the code to the computer

In the“**MicroPython device**”, right-click and select **Project\_01\_HelloWorld.py**，select“**Download to ...**”to download the code to our computer.

![Img](./media/img-20231012102103.png)


#### Delete the files in the Raspberry Pi Pico root directory

In the“**MicroPython device**”，right-click and select **Project\_01\_HelloWorld.py**，select“**Delete”**，delete the **Project\_01\_HelloWorld.py** from the Raspberry Pi Pico root directory.

![Img](./media/img-20231012102111.png)


#### Delete files from the computer's directory

In the Project\_01 : Hello World file, right-click and select Project\_01\_HelloWorld.py，select“**Move to Recycle Bin**”，then it can be deleted from the Project\_01\_HelloWorld file.

![Img](./media/img-20231012102120.png)


#### Create and Save Code

①Click“**File**”→“**New**”to create and compile code.

![Img](./media/img-20231012102128.png)

②Enter code in the newly opened file, here we use **Project\_02\_Onboard\_LED\_Flashing.py** code as an example.

![Img](./media/img-20231012102136.png)

③Click“**Save**”，and we can save the code to our computer or the Raspberry Pi Pico.

![Img](./media/img-20231012102144.png)

④ Select“**MicroPython device**”，enter“**main\.py**”in the new pop-up window and click“**OK**”.

![Img](./media/img-20231012102152.png)

![Img](./media/img-20231012102157.png)


⑤ We can see the code has been uploaded to the Raspberry Pi Pico.

![Img](./media/img-20231012102203.png)


⑥Click“**Run current script**”, the LED on the Raspberry Pi Pico will flash periodically.

![Img](./media/img-20231012102210.png)



















