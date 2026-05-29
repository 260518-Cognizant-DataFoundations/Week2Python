"""
This Class represents a Cookie Eating Monster. A Cookie Monster if you will

He likes to eat cookies,
but he HATES anything that's not a cookie

*He will raise an Exception if you try to feed him a non-cookie*
"""

class CookieEatingMonster:

    # No constructor - no attributes I care to include

    # TODO: maybe make a Food class with a boolean for isCookie?

    def eat(self, food):
        if food.lower() != "cookie":
            # Raise our custom exception
            raise NotACookieError("ABSOLUTELY DISGUSTING!")

        print("Thanks for the cookie :)")


# CUSTOM EXCEPTION - make these when no built-in python Exception fits your problem
class NotACookieError(Exception):
    # Every Exception has a message that comes with it
    # We can just define it in the constructor
    def __init__(self, message):
        self.message = message