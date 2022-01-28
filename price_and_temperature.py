# Run the tests, then change the functions and test expectations
# The tests need to pass and the function needs to meet the requirements

def unit_price():
    # function requirements:
    # the user will input a price (¥), and a weight (kg). This function should return the price per kilogram
    price = input("What is the price? (¥) ")
    weight = input("What is the product weight? (kg) ")
    unit_price = float(price) / float (weight)
    return f"This product is ¥{unit_price}/kg"


def celsius_to_fahrenheit():
    # function requirements:
    # the user will input a temperature in celsius. This function should return the temperature in Fahrenheit
    celsius = input("What's the temperature in °C? ")
    fahrenheit = (9 / 5) * float(celsius) + 32
    return f"{celsius}°C is {fahrenheit}°F"
