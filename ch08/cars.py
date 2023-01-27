# Exercise 8-14. Cars

def make_car(manufacturer, model, **kwargs):
    """Build a dictionary with information about a car."""
    kwargs["manufacturer"] = manufacturer
    kwargs["model"] = model
    return kwargs

print(make_car("subaru", "outback", color="blue", tow_package=True))
