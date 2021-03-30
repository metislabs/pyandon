# PyAndon

Python module for interacting with a range of different industrial warning light systems.

Development of PyAndon is sponsored by [Metis Labs Ltd.](https://www.metislabs.tech)

## Installation

PyAndon is available through [PyPI](https://pypi.org/project/pyandon/), so can be installed by running:

    pip3 install pyandon

## Usage

First import the module as normal:

    import pyandon

You can then discover all attached devices by running:

    devices = pyandon.find_devices()
    print(devices)

Pick the first device and turn a light on:

    device = devices[0]
    device.set_light(pyandon.LightColor.GREEN, pyandon.LightPattern.STATIC)

Enable the buzzer, playing a two tone pattern:

    device.set_buzzer(pyandon.BuzzerPattern.PATTERN_1, [pyandon.BuzzerNotes.C7, pyandon.BuzzerNotes.D7])

And finally clear all lights and buzzers:

    device.clear()

For a more advanced example, take a look at [examples/fly\_me\_to\_the\_moon.py](examples/fly_me_to_the_moon.py).

## Supported Devices

Currently only Patlite USB lights are supported. Pull requests for drivers for additional devices and manufacturers are very welcome. If you would like to discuss having a driver written for you and are able to ship a test device to the UK please contact <mike.sheldon@metislabs.tech>.
