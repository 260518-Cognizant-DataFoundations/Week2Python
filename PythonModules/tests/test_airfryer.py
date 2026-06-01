"""
TODO: my typical blurb
"""

import pytest

from app.models.airfryer import AirFryer

# To run your test class, just run "pytest /path/to/file/filename.py"

# Very first test - super simple green test
def test_fry():
    fryer = AirFryer()
    assert fryer.fry() == "AirFryer is frying food!"

