bikecost = 2000
print("If a Motorbike costs £",bikecost,"and it's value decreses by 10% each year, the value will fall as follows:\n")

while (bikecost > 1000):
  print("£",bikecost)
  deduction = bikecost / 10
  bikecost = bikecost - deduction
else:
  print("\nAfter this point, the value of the motorbike falls below £1000.")


print("\n\nHi there!")
jokechoice = int(input("Select a number to hear a joke from 1, 2 or 3,"))
if (jokechoice ==1):
  print("Did you hear about the mathematician who was afraid od negative numbers...he would stop at nothing to avoid them")
elif (jokechoice ==2):
  print ("lol")
elif (jokechoice ==3):
  print("lmao")
else:
  print("Oops, that's not a valid selection. Try again.")
