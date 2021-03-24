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
