import pkgutil
import os.path

def load_drivers():
    drivers = []
    loader = pkgutil.get_loader("pyandon.drivers")
    for submodule in pkgutil.walk_packages([os.path.dirname(loader.path)]):
        print(submodule)
        if submodule.name != "andon_driver" and submodule.name != "andon_usb_driver":
            l = pkgutil.get_loader("pyandon.drivers." + submodule.name)
            m = l.load_module()
            drivers.append(m.create_driver())
    return drivers
