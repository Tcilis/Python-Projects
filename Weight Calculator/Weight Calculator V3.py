#calculates your weight (version 1)
#makes sure to give the right letter (version 2)
#makes sure to give the right amount and also provide it in int and not float
flag = 1
while flag == 1:
      weight = int(input("How much do you weight "))
      if weight <= 0 or weight > 999:
         print ("Please provide a right amount of weight")
      else:
          flag = 0
flag = 1
while flag == 1:
      answer = input("Press 'K' for KG or Press 'L' for LB ")
      if answer.upper() != "K" and answer.upper() != "L":
         print ("Please choose the right letter")
      else:
          flag = 0
if answer.upper() == "K":
   convert = weight * 2.20462262
   print ("your weight in LB is " + str(int(convert)))
else:
   convert = weight / 2.20462262
   print ("your weight in KG is " + str(int(convert)))