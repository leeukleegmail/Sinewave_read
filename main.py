import time

import machine
import neopixel

np = neopixel.NeoPixel(machine.Pin(4), 64)

adc = machine.ADC(0)


def determine_leds(leds):
    if 1 <= leds <= 31:
        return 0
    if 32 <= leds <= 63:
        return 1
    if 64 <= leds <= 95:
        return 2
    if 96 <= leds <= 127:
        return 3
    if 128 <= leds <= 159:
        return 4
    if 160 <= leds <= 191:
        return 5
    if 192 <= leds <= 223:
        return 6
    if 224 <= leds <= 255:
        return 7
    if 256 <= leds <= 300:
        return 8


while True:
    for _ in range(0, 1000):
        adc_value = adc.read()  # Full range: 3.3v
        leds = determine_leds(adc_value)
        for i in range(leds):
            np[0] = (0, 125, 0)
            if 1 <= i <= 2:
                np[0] = (0, 125, 0)
                np[i] = (0, 125, 0)
            if 3 <= i <= 5:
                np[i] = (125, 125, 0)
            if 6 <= i <= 8:
                np[i] = (125, 0, 0)
        np.write()

        for i in range(64):
            np[i] = (0, 0, 0)
        np.write()
        time.sleep(0.1)
