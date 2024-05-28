#!/usr/bin/python3
import uinput
import time
import math

TOGGLE_TABLET_MODE = (5, 1)


def is_tablet():
    with open("/sys/bus/iio/devices/iio:device0/in_accel_x_raw", "r") as f:
        v1 = int(f.read())
    with open("/sys/bus/iio/devices/iio:device1/in_accel_x_raw", "r") as f:
        v2 = int(f.read())
    return abs(v2 - v1) < 100

# Enable 2nd accelerometer
try:
    with open("/sys/bus/i2c/devices/i2c-0/new_device", "w") as f:
        f.write("mxc4005 0x15")
except OSError:
    print("Failed to enable 2nd accel")
time.sleep(1)


# Main program
with uinput.Device([TOGGLE_TABLET_MODE]) as device:
    last = None
    while True:
        val = 1 if is_tablet() else 0
        if val != last:
            device.emit(TOGGLE_TABLET_MODE, val)
        time.sleep(0.5)

