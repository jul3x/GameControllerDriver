import sys
sys.path.append("pyserial-3.4")
sys.path.append("pynput")
sys.path.append("python-xlib-0.26")

import serial
from pynput.keyboard import Key, Controller

port_name = "/dev/ttyACM0"
keyboard = Controller()
trigger_val = 0.3

try:
    ser = serial.Serial(port_name)

    while True:
        try:
            line = ser.readline().decode('utf-8')
            if line[0] == 'P' and line[-1] == '\n':
                pass
            else:
                continue

            x_separated = line[1:].split("X")
            f_pressed = int(x_separated[0])
            y_separated = x_separated[1].split("Y")
            x_val = int(y_separated[0])
            z_separated = y_separated[1].split("Z")
            y_val = int(z_separated[0])
            z_val = int(z_separated[1])

            x_val = x_val - 255 if x_val > 122 else x_val
            y_val = y_val - 255 if y_val > 122 else y_val
            z_val = z_val - 255 if z_val > 122 else z_val

            if z_val == 0:
                keyboard.release(Key.left)
                keyboard.release(Key.up)
                keyboard.release(Key.down)
                keyboard.release(Key.right)
            else:
                rot_x = x_val / z_val
                rot_y = y_val / z_val 

                if f_pressed == 1:
                    keyboard.press(Key.ctrl)
                    keyboard.press(Key.space)
                else:
                    keyboard.release(Key.ctrl)
                    keyboard.release(Key.space)

                if rot_x < -trigger_val:
                    keyboard.press(Key.left)
                elif rot_x >= -trigger_val and rot_x <= trigger_val:
                    keyboard.release(Key.left)
                    keyboard.release(Key.right)
                else:
                    keyboard.press(Key.right)

                if rot_y < -trigger_val:
                    keyboard.press(Key.down)
                elif rot_y >= -trigger_val and rot_y <= trigger_val:
                    keyboard.release(Key.up)
                    keyboard.release(Key.down)
                else:
                    keyboard.press(Key.up)

        except (IndexError, ValueError, NameError):
            pass 
        except KeyboardInterrupt:
            break

    ser.close()
except serial.serialutil.SerialException:
    print('Error!\n')
    print('Cannot connect to serial port!')
