"""
 Here lies the TEST SUITE for the AirFryer class
 Tests are meant to check that our code is working as expected,
 and catch any issues BEFORE your erroneous code is unleashed on the world.

 "Why WOULDN'T my code work??? I wrote it..."
 First off, it's a good way to ensure that your code truly does everything it's supposed to.
 Also, your code will change as you develop. You might break something that was working before.

 Companies will have you ensure company code is covered by some percentage of tests
 "I want 80% test coverage on the new AirFryer class before we can deploy i
"""

import pytest

from app.models.airfryer import AirFryer

# To run your test class, just run "pytest /path/to/file/filename.py"

# This is a "fixture", which gives us a reusable object for use in our tests
# This helps us avoid re-instantiating the same object in each test.
@pytest.fixture(scope="module")
def fryer():
    return AirFryer()

# Very first test - super simple green test
def test_fry(fryer):
    assert fryer.fry() == "AirFryer is frying food!"

# A GREEN TEST for set_temp (expected behavior)
def test_set_temp_valid(fryer):
    assert fryer.set_temperature(350) == ("AirFryer temp set to %d degrees", 350)

# A RED TEST for set_temp (erroneous behavior)
def test_set_temp_invalid(fryer):
    with pytest.raises(ValueError) as e:
        fryer.set_temperature(3000)
        assert str(e.value) == "Temp must be between 0 and 400"

# TODO: You can test register_user, but I'm cutting it for calculate_tip


# You can have multiple asserts in one test
# NOTE: is this a good test? It's a little bulky and unfocused - maybe split it up
def test_calculate_tip(fryer):

    # Valid weight
    assert fryer.calculate_tip(5) == 1.2417566953150931

    # Valid but heavy weight
    assert fryer.calculate_tip(5000) == 4943.522444877528

    # Assert result is the correct datatype
    assert isinstance(fryer.calculate_tip(5), float)

    # Invalid weight
    with pytest.raises(ValueError) as e:
        fryer.calculate_tip(-5)
        assert str(e.value) == "Weight must be greater than 0"

