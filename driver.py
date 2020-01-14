import serial
from pynput.keyboard import Key, Controller

port_name = '/dev/ttyACM0'
keyboard = Controller()

try:
    ser = serial.Serial(port_name)

    while True:
        line = ser.readline()
        y_separated = line[1:].split("Y")
        x_val = int(y_separated[0])
        z_separated = y_separated[1].split("Z")
        y_val = int(z_separated[0])
        f_separated = z_separated[1].split("F")
        z_val = int(f_separated[0])
        f_pressed = int(f_separated[1])

        print("x: " + str(x_val) + ", y: " + str(y_val) + ", z: " + str(z_val) + ", f: " + str(f_pressed)) 

        if f_pressed == 1:
            keyboard.press(Key.ctrl)
        else:
            keyboard.release(Key.ctrl)

    ser.close()
except:
    print('Error!\n')
    print('Port ' + port_name + ' is not recognised!')
