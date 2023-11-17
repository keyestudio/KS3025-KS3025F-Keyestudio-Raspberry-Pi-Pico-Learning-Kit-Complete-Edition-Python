# Project 26：Rocker control light

1.**Introduction**

The joystick module is a component with two analog inputs and one digital input. It is widely used in game operation, robot control, drone control and other fields.

In this project, we will use a Raspberry Pi Pico and a joystick module to control RGB. You can have a deeper understanding of the principle and operation of the joystick module in practice.



2.**Components Required**

| ![img](media/wps12.png)                 | ![img](media/wps13-168412843101312.jpg) | ![img](media/wps14-168412843224413.jpg) |
| --------------------------------------- | --------------------------------------- | --------------------------------------- |
| Raspberry Pi Pico*1                     | Raspberry Pi Pico Expansion Board*1     | Joystick Module*1                       |
| ![img](media/wps15-168412843433214.jpg) | ![img](media/wps16-168412843592315.jpg) | ![img](media/wps17-168412843762116.jpg) |
| RGB LED*1                               | 220ΩResistor*3                          | Jumper Wires                            |
| ![img](media/wps18-168412843945417.jpg) | ![img](media/wps19-168412844081918.jpg) | ![img](media/wps20-168412844246919.jpg) |
| USB Cable*1                             | M-F Dupont Wires                        | Breadboard*1                            |



3.**Component Knowledge**

![](../media/d087b123748cbfb8ed9f517150db71c5.png)

**Joystick module**: 

It mainly uses PS2 joystick components. In fact, the joystick module has 3 signal terminal pins, which simulate a three-dimensional space. The pins of the joystick module are GND, VCC, and signal terminals (B, X, Y). The signal terminals X and Y simulate the X-axis and Y-axis of the space. 

When controlling, the X and Y signal terminals of the module are connected to the analog port of the microcontroller. The signal terminal B simulates the Z axis of the space, it is generally connected to the digital port and used as a button.

VCC is connected to the microcontroller power output VCC (3.3V or 5V), GND is connected to the microcontroller GND, the voltage in the original state is about 1.65V or 2.5V. 

In the X-axis direction, when moving in the direction of the arrow, the voltage value increases, and the maximum voltage can be reached. Moving in the opposite direction of the arrow, the voltage value gradually decreases to the minimum voltage. 

In the Y-axis direction, the voltage value decreases gradually as it moves in the direction of the arrow on the module, decreasing to the minimum voltage. 

As the arrow is moved in the opposite direction, the voltage value increases and can reach the maximum voltage. In the Z-axis direction, the signal terminal B is connected to the digital port and outputs 0 in the original state and outputs 1 when pressed. 

In this way, we can read the two analog values and the high and low level conditions of the digital port to determine the operating status of the joystick on the module.



4.**Features:**

- Input Voltage: DC 3.3V \~ 5V

- Output Signal: X/Y dual axis analog value +Z axis digital signal

- Range of Application: Suitable for control point coordinate movement in plane as well as control of two degrees of freedom steering gear, etc.  

- Product features: Exquisite appearance, joystick feel superior, simple operation, sensitive response, long service life.  



5.**Read the Value**

We have to use analog Raspberry Pi Pico pin IO to read the data from X or Y pins, and use digital IO port to read the values of the button. Please follow the wiring diagram below for wiring.

![](../media/36004a41553a2f413ba05775e9b696eb.png)

![](../media/b843cdff62b3ccf3f3f028a834b468aa.png)

You can open the code we provide:


```c
/*  
 * Filename    : Read Rocker Value
 * Description : Read data from Rocker.
 * Auther      : http//www.keyestudio.com
*/
int xyzPins[] = {27, 26, 28};   //x,y,z pins
void setup() {
  Serial.begin(115200);
  pinMode(xyzPins[0], INPUT); //x axis. 
  pinMode(xyzPins[0], INPUT); //y axis. 
  pinMode(xyzPins[2], INPUT_PULLUP);   //z axis is a button.
}

// In loop(), use analogRead () to read the value of axes X and Y 
//and use digitalRead () to read the value of axis Z, then display them.
void loop() {
  int xVal = analogRead(xyzPins[0]);
  int yVal = analogRead(xyzPins[1]);
  int zVal = digitalRead(xyzPins[2]);
  Serial.println("X,Y,Z: " + String(xVal) + ", " +  String(yVal) + ", " + String(zVal));
  delay(500);
}
```


![](../media/f25ac7cecd02b5ed0ce41fd81093955a.png)

Click ![](../media/b0d41283bf5ae66d2d5ab45db15331ba.png) to upload the test code to the Raspberry Pi Pico board

![](../media/d34a675158c37ad97dcf719bd1231a75.png)

The code was uploaded successfully.

![](../media/4cfd0bd27cbd16f9cf24264874aee8ad.png)

Upload the code to the pico board, power up with a USB cable and open the serial monitor and set baud rate to 115200.

The monitor will show values of the joystick module while moving the joystick.

![](../media/c8097bd115d4c564192c19a08df2702a.jpeg)

![](../media/9448c2e32f64ffa31f400e678f590d50.png)

6.**Circuit Diagram and Wiring Diagram**

We just read the value of the joystick module. Now we need to do something with the joystick module and RGB, connecting according to the following diagram.

![](../media/000ec2c5dae0b0d5368569abbd026f35.png)

![](../media/68601044f75ee6840f0b97cad9bea891.png)

7.**Test Result：**

You can open the code we provide:


```c
/*  
 * Filename    : Rocker Control Light
 * Description : Control RGB to light different colors by Rocker.
 * Auther      : http//www.keyestudio.com
*/
int xyzPins[] = {27, 26, 28};   //x,y,z pins
int ledPins[] = {18, 17, 16};    //define red, green, blue led pins
void setup() {
  pinMode(xyzPins[0], INPUT); //x axis. 
  pinMode(xyzPins[0], INPUT); //y axis. 
  pinMode(xyzPins[2], INPUT_PULLUP);   //z axis is a button.
  for (int i = 0; i < 3; i++) {   //setup the pwm channels,1KHz,8bit
    pinMode(ledPins[i], OUTPUT);
  }
}

// In loop(), use analogRead () to read the value of axes X and Y 
//and use digitalRead () to read the value of axis Z, then display them.
void loop() {
  int xVal = analogRead(xyzPins[0]);
  int yVal = analogRead(xyzPins[1]);
  int zVal = digitalRead(xyzPins[2]);
  if (xVal < 200){
     analogWrite(ledPins[0], 255); //Common cathode LED, high level to turn on the led.
     analogWrite(ledPins[1], 0);
     analogWrite(ledPins[2], 0);
   }
  else if (xVal > 800){
     analogWrite(ledPins[0], 0); 
     analogWrite(ledPins[1], 255);
     analogWrite(ledPins[2], 0);
   }
  else if (yVal < 200){
     analogWrite(ledPins[0], 0); 
     analogWrite(ledPins[1], 0);
     analogWrite(ledPins[2], 255);
   }
  else if (yVal > 800){
     analogWrite(ledPins[0], 255); 
     analogWrite(ledPins[1], 255);
     analogWrite(ledPins[2], 255);
   }
}
```


Before uploading Test Code to Raspberry Pi Pico, please check the configuration of Arduino IDE.

Click "Tools" to confirm that the board type and ports.

![](../media/88ff55ea66096dafebac025d5283009b.png)

Click ![](../media/b0d41283bf5ae66d2d5ab45db15331ba.png) to upload the test code to the Raspberry Pi Pico board

![](../media/10b935cb2e374ed9625bd6ea35229836.png)

The code was uploaded successfully.

![](../media/8bb9867117a33ecd53fbb6772b35a4f0.png)

8.**Test Result：**

Upload the code and power up. If you move the joystick to the left, the RGB will turn red. If moving it to the right, the RGB will turn green; if moving it upward, the RGB will show white; if moving it downward, the RGB will become into blue.

![](../media/9c2d0d8777200827b16c49b752d45c4c.jpeg)
