"""
We'll have two different classes in this app -

1) AirFryer - Has basic to somewhat complex methods that we'll use to:
    -See some modules in action (math, logging, regex)
    -write some tests with the Pytest module
    -TODO: If possible, time permitting, we'll use the JSON and pylint modules as well

2) AirFryerTests - A Test Suite where we'll write Pytest tests for AirFryer's methods

We'll call the AirFryer methods below for fun (and to see our logs at work)
"""

from models.airfryer import AirFryer

# Instantiate the AirFryer class to access its method
fryer = AirFryer()

# Invoking fry
print(fryer.fry())

# Invoking set_temperature
print(fryer.set_temperature(350)) # valid temp
print(fryer.set_temperature(3000)) # invalid temp

# Let's try to register a user
print(fryer.register_user("FryGuy")) # valid one

try:
    print(fryer.register_user("ILiekJavaScript")) # one with j********t in it - should raise an error
except ValueError as e:
    print(e)
    print("Please try again with a less vulgar name")


# Calculating tip

fryer.calculate_tip(5) # Valid weight
fryer.calculate_tip(500) # Valid but heavy

# Invalid weight
try:
    fryer.calculate_tip(-5)
except ValueError as e:
    print(e)
    print("Please don't put negative weight in the air fryer")

