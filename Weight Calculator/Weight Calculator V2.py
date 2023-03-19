# This program prompts the user to input their weight and unit of measurement, and then converts the weight to the opposite unit of measurement.

# Prompt the user to input their weight in any unit of measurement.
weight = int(input("How much do you weigh? "))

# Set flag variable to 1 initially to start the while loop.
flag = 1

# This while loop will keep running until the user inputs a valid unit of measurement ('K' for kilograms or 'L' for pounds).
while flag == 1:
      answer = input("Press 'K' for kilograms or 'L' for pounds. ")
      if answer.upper() != "K" and answer.upper() != "L":
         print ("Please choose the correct letter ('K' or 'L').")
      else:
          flag = 0

# If the user chooses 'K' for kilograms, convert the weight to pounds.
if answer.upper() == "K":
   convert = weight * 2.20462262
   print ("Your weight in pounds is " + str(convert))

# If the user chooses 'L' for pounds, convert the weight to kilograms.
else:
   convert = weight / 2.20462262
   print ("Your weight in kilograms is " + str(convert))
 