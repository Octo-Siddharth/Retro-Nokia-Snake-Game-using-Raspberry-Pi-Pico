# Retro_Nokia_Snake_Game

Retro Nokia Snake Game using Raspberry Pi Pico made with <❤> by Siddhartha Rakshit

Very much inspired from the childhood memories, when we used to play "The Snake Game" in our good old nokia phones, I bet most of us scored a huge. So let's recall the some part of childhood with this project.

## Circuitry and Coding Part
- Follow the Schematic and connect the OLED Display and Push Button switches 
- The OLED Display is an I2C based 128x64 pixels display, you can use any other monochrome OLED display of your choise.
- After connecting all the components use the `i2c.py` code to check whether the diaplay is connected properly or not. 
- Check the display I2C address as well it should be 0X3C.
- Now check the buttons that, they are giving pull-up values or not.
- Connect the Raspberry Pi Pico with the computer configure Thonny IDE, choose proper Interpreter and COM port.
- Insatll the SSD1306 OLED Library from the Manage Packages from tools in thonny ide or simply upload the `ssd1306.py` inside lib folder in Pi Pico.
- Upload the `Retri_Snake_Pi_Code.py` to Pi Pico.
- Start the game and enjoy !! Dive into Childhood. 😎
    
## Thumbnail

![Thumbnail](/Project_Img_1.jpg)
## The Circits Images
![screenshot](/Project_Img_2.jpg)
![screenshot](/Project_Img_3.jpg)

# Follow the schematic for the circuit diagram

![Schematic](/Project_Schematic.png)


