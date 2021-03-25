"""
PyAndon - Python module for interacting with a range of different andon lights

Copyright 2021, Metis Labs Ltd.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included
    in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import pkgutil
import os.path


def load_drivers():
    drivers = []
    loader = pkgutil.get_loader("pyandon.drivers")
    for submodule in pkgutil.walk_packages([os.path.dirname(loader.path)]):
        if submodule.name not in ["andon_driver", "andon_usb_driver", "types"]:
            l = pkgutil.get_loader("pyandon.drivers." + submodule.name)
            m = l.load_module()
            drivers.append(m.create_driver())
    return drivers
