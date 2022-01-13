# name - parameter
# "Vlad" - argument
def greet(name):
    print(f"Hello {name}")
    print("How do you do?")
    print("Isn't the weather nice today?")


def greet_with(name="Vielen", location="Chukotak"):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")


# Functions with keyword arguments
greet_with(location="Some", name="Bla")
