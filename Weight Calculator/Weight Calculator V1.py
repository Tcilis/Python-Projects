# This program prompts the user to input their weight and unit of measurement, and then converts the weight to the opposite unit of measurement.

# Prompt the user to input their weight in any unit of measurement.
weight = int(input("How much do you weigh? "))

# Prompt the user to choose a unit of measurement ('K' for kilograms or 'L' for pounds).
answer = input("Press K for kilograms or L for pounds. ")

# If the user chooses 'K' for kilograms, convert the weight to pounds.
if answer.upper() == "K":
   convert = weight * 2.2046226218
   print ("Your weight in pounds is " + str(convert))

# If the user chooses 'L' for pounds, convert the weight to kilograms.
else:
   convert = weight / 2.2046226218
   print ("Your weight in kilograms is " + str(convert)) 