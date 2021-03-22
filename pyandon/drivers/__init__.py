import pkgutil

def create_drivers():
    drivers = []
    for submodule in pkgutil.walk_packages(["drivers"]):
        if submodule.name != "driver":
            l = pkgutil.get_loader("drivers." + submodule.name)
            m = l.load_module()
            drivers.append(m.create_driver())
    return drivers
