#Program so that in order for somebody to actually purchase a ticket to go on the rollercoaster ride, they will need to be over 120 centimeters and check for multiple conditions even if the previous one was already true. In addition people who want to keep a picture for the memories should be charged an extra $3.

#If condition 1 is true, then do A, but then the code is going to go to the next case and check if condition 2 is also true, in which case it will do B and if the final condition is also true, it's going to do C. And if all three conditions are checked and if it's so happens that all three conditions are true, then A, B and C will all be executed. 

#So we have three conditions: age, less than 12, age between 12 and 18, and finally everybody else, except a separate price category for those people who are aged between 45 and 55 and those people get to ride for free.


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

# We need to create a variable up here called bill and to set it to equal zero. And further below we need to set the bill to the price that they're supposed to pay.

bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  
    #We're going to print something like: "Everything's going to be ok. Have a free ride on us!"
  
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  
  #And we've been able to do this because we know about the and logical operator.
  
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  # And this is going to apply to everybody of above mentioned 3 age groups no matter their age.
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3 
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")  