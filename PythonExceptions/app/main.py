# Let's start by raising an Exception on purpose and see what happens
# result = 5 / 0

# We can also raise Exceptions OURSELVES as a way to validate user behaviors
def print_money(amount):
    if amount < 0:
        raise ValueError("Amount can't be negative!")

    print(f"You printed ${amount}!")

print_money(1)

# This time, we won't let the runtime stop. We'll HANDLE the Exception!
try:
    print_money(-1)
except ValueError as e: # Exceptions are just objects! We can store them in variables!
    print(f"Error occured! {e}")
finally:
    # The finally block always runs -
    # typically used for stuff like cleanup (closing files, DB connections, etc)
    print("I'm always gonna run no matter what")

print("I DO run, because we handled the Exception instead of letting the app crash")


# We can also CHAIN exceptions if multiple things could go wrong
# We can have as many except blocks as we want! To account for different problems
# The first Except block that matches the problem will run
    # Read below on why this is technically bad code:
def divide(a, b):
    try:
        print(a/b)
    except ArithmeticError:
        print("Something mathematical went wrong ")
    except ZeroDivisionError:
        print("Can't divide by zero!")
    except Exception:
        print("This block would have caught any exception at all")
    # We could have had a finally block here, but it's optional

divide(5, 0)

"""
MAKE SURE TO PUT THE MORE SPECIFIC EXCEPT BLOCKS FIRST!

In the try/except above, the more generic ArithmeticError gets caught
But we could have been more clear to the user, who's real problem is that they divided by zero
"""

print("=================(Using our custom exception)")

#Import and instantiate Cookie Eating Monster

# Just like any other Exception, if we don't handle it, the code will crash

from app.cookie_eating_monster import CookieEatingMonster, NotACookieError

monster = CookieEatingMonster()

# monster.eat("oatmeal") <---NOT HANDLED! Runtime will terminate!!!

# Let's handle it instead
try:
    monster.eat("brussels sprouts")
except NotACookieError as e:
    print(f"Monster is mad! Exception Message: {e}")

# Just cuz I feel bad
monster.eat("cookie")
