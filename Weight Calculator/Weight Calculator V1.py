#calculates your weight (version 1)
weight = int(input("How much do you weight "))
answer = input("Press K for KG or L for LB ")
if answer.upper() == "K":
   convert = weight * 2.2046226218
   print ("your weight in LB is " + str(convert))
else:
   convert = weight / 2.2046226218
   print ("your weight in KG is " + str(convert)) 