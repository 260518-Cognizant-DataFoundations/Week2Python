



class AirFryer:

    # Skipping the Constructor - no attributes in this demo

    # Basic method that will be easy to test (nothing can go wrong)
    def fry(self):
        return "AirFryer is frying food!"

    # This method has something that can go wrong - makes for more interesting tests
    def set_temperature(self, temp):
        if temp < 0 or temp > 400:
            raise ValueError("Temp must be between 0 and 400")
        return f"AirFryer temp set to {temp} degrees"

    # User Registration method - will use the regex module to validate username
    def register_user(self, username):
        """
        Importing Python's Regex module
        Regex (Regular Expressions) is a way to pattern match, search, and change strings
        Regex syntax is normally very ugly
        But the Python regex module makes it way easier to accomplish regex tasks
        """
        import re

        # Reject usernames that contain vulgarity
        if re.search(r"javascript", username, re.IGNORECASE):
            raise ValueError("Username cannot contain vulgarity")

        return f"User {username} registered successfully!"


    # Using the math module to charge the user a tip after every airfry
    def calculate_tip(self, weight):
        """
        Importing the Python Math Module
        This module contains TONS of useful math operations and constants (like pi)
        We'll just use a couple functions, but there are a lot
        """
        import math

        # First, check for valid weight
        if weight <= 0:
            raise ValueError("Weight must be greater than 0")

        # calculate the tip exponentially based on weight
        tip = math.pow(weight, 1.2) * .18

        print(f"Suggested tip of {tip:.2f} will be charged automatically")
        print(f"You may round up to {math.ceil(tip)} if you'd like")
        print(f"Or you may round down to {math.floor(tip)} if you watch an ad")

        # ceil() rounds up to the nearest integer
        # floor() rounds down to the nearest integer

        return tip
