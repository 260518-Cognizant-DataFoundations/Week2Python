import logging

# Configuring a Logger with the Python Logging Module
logging.basicConfig(
    level=logging.INFO, # Allow all levels of logs (INFO and everything more severe)
    format="%(asctime)s - %(levelname)s - %(message)s", # Format what the logs look like
    # handlers are where our logs will be stored/displayed
    handlers=[
        logging.FileHandler("airfryer.logs"), # Logs will get stored in a file
        logging.StreamHandler() # They'll also get printed to console
    ]
)

class AirFryer:

    # Skipping the Constructor - no attributes in this demo

    # Basic method that will be easy to test (nothing can go wrong)
    def fry(self):

        # Our first log - just a basic INFO log
        logging.info("AirFryer is frying food!")

        return "AirFryer is frying food!"

    # This method has something that can go wrong - makes for more interesting tests
    def set_temperature(self, temp):
        if temp < 0 or temp > 400:

            # Warning log - typical for user error
            logging.warning("Attempted to set temp to %d", temp)

            raise ValueError("Temp must be between 0 and 400")

        logging.info("Set temp to %d", temp)

        return "AirFryer temp set to %d degrees", temp

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

            logging.warning("User tried to say a nono word")

            raise ValueError("Username cannot contain vulgarity")

        logging.info("User %s registered successfully", username)
        return "User %s registered successfully!", username


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

            logging.warning("Invalid weight of %.2f", weight)
            raise ValueError("Weight must be greater than 0")

        # calculate the tip exponentially based on weight
        tip = math.pow(weight, 1.2) * .18

        print(f"Suggested tip of {tip:.2f} will be charged automatically")
        print(f"You may round up to {math.ceil(tip)} if you'd like")
        print(f"Or you may round down to {math.floor(tip)} if you watch an ad")

        # ceil() rounds up to the nearest integer
        # floor() rounds down to the nearest integer

        logging.info("Calculated tip of %.2f", tip)

        return tip
