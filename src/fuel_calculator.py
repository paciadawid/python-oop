# Fuel required to launch a given module is based on its mass. Specifically, to find the fuel
# required for a module, take its mass, divide by three, round down, and subtract 2.

def calculate_fuel(mass):
    if type(mass) not in [int, float, str]:
        print(f"Wrong type -> {type(mass)}")
        return False

    try:
        mass = int(mass)
    except ValueError as e:
        print(f"Converstion error -> {e}")
        return False

    if mass <= 0:
        return False
    elif mass <= 6:
        return 1
    return mass // 3 - 2
