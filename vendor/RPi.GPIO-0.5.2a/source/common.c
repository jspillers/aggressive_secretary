/*
Copyright (c) 2013 Ben Croston

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
*/

#include "Python.h"
#include "c_gpio.h"
#include "exceptions.h"
#include "common.h"

int gpio_mode = MODE_UNKNOWN;
const int pin_to_gpio_rev1[27] = {-1, -1, -1, 0, -1, 1, -1, 4, 14, -1, 15, 17, 18, 21, -1, 22, 23, -1, 24, 10, -1, 9, 25, 11, 8, -1, 7};
const int pin_to_gpio_rev2[27] = {-1, -1, -1, 2, -1, 3, -1, 4, 14, -1, 15, 17, 18, 27, -1, 22, 23, -1, 24, 10, -1, 9, 25, 11, 8, -1, 7};
int setup_error = 0;

int get_gpio_number(int channel, unsigned int *gpio)
{
    // check module has been imported cleanly
    if (setup_error)
    {
        PyErr_SetString(SetupException, "Module not imported correctly!");
        return 1;
    }

    // check setmode() has been run
    if (gpio_mode != BOARD && gpio_mode != BCM)
    {
        PyErr_SetString(ModeNotSetException, "Please set pin numbering mode using GPIO.setmode(GPIO.BOARD) or GPIO.setmode(GPIO.BCM)");
        return 2;
    }

    // check channel number is in range
    if ( (gpio_mode == BCM && (channel < 0 || channel > 53))
      || (gpio_mode == BOARD && (channel < 1 || channel > 26)) )
    {
        PyErr_SetString(InvalidChannelException, "The channel sent is invalid on a Raspberry Pi");
        return 3;
    }

    // convert channel to gpio
    if (gpio_mode == BOARD)
    {
        if (*(*pin_to_gpio+channel) == -1)
        {
            PyErr_SetString(InvalidChannelException, "The channel sent is invalid on a Raspberry Pi");
            return 4;
        } else {
            *gpio = *(*pin_to_gpio+channel);
        }
    }
    else // gpio_mode == BCM
    {
        *gpio = channel;
    }

    return 0;
}