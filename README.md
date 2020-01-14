# GameControllerDriver
Simple driver handling communication of system with GameControllerSTM32 via USB.

# Dependencies
* python3
* libs provided in repository

# Usage  
Connect microcontroller with appropriate software [(GameControllerSTM32)](http://github.com/jul3x/GameControllerSTM32) or any other that sends data via serial port in format `P{fire_pressed}X{val_x}Y{val_y}Z{val_z}\r\n` (fire_pressed - boolean, values from 0 to 255 - e.g. `P0X231Y35Z64\r\n`).

Change value of `port_name` in `driver.py` file to one used in your operating system.  

Run `python3 driver.py` and enjoy steering Left, Right, Up, Down and Ctrl buttons using your own microcontroller.
