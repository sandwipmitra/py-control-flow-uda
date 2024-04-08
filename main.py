#1. 
# phone_balance = 3
# bank_balance = 100
# print(phone_balance, bank_balance)

# if phone_balance < 5:
#   phone_balance += 10
#   bank_balance -=10

# print(phone_balance, bank_balance)

#2.
# n = 15
# if n % 2 == 0:
#   print("Number " + str(n) + " is even")
# else:
#   print("Number " + str(n) + " is odd")
#   # print(n)

#3.
# season = "spring"
# season = "summer"
# season = "fall"
# season = "winter"
# season = "rainy"

# if season == "spring":
#   print("Plant the garden")
# elif season == "summer":
#   print("water the garden")
# elif season == "fall":
#   print("Harvest the garden")
# elif season == "winter":
#   print("Stay indoor!")
# else:
#   print("Unrecognize season")


# #4. bus fares
# age = 35

# #age limitation
# free_upto_age = 4
# child_upto_age = 18
# senior_form_age = 65

# #ticket price
# concession_ticket = 1.25
# adult_ticket = 2.50

# #condition n execution
# if age <= free_upto_age:
#   ticket_price = 0
#   print(ticket_price)
# elif age <= child_upto_age:
#   ticket_price = concession_ticket
#   print(ticket_price)
# elif age >= senior_form_age:
#   ticket_price = concession_ticket
#   print(ticket_price)
# else:
#   ticket_price = adult_ticket
  # print(ticket_price)

#5. Which price
#method 2
# points = 174

# if points <= 50:
#   print("Congratulations! You won a wooden rabbit!")
# elif points <= 150:
#   print("Oh dear, no prize this time.")
# elif points <= 180:
#   print("Congratulations! You won a wafer-thin mint!")
# elif points <= 200:
#   print("Congratulations! You won a penguin!")
# else:
#   print("Oh dear, no prize this time.")

#method 2
# points = 174

# if points <= 50:
#     result = "Congratulations! You won a wooden rabbit!"
# elif points <= 150:
#     result = "Oh dear, no prize this time."
# elif points <= 180:
#     result = "Congratulations! You won a wafer-thin mint!"
# else:
#     result = "Congratulations! You won a penguin!"

# print(result)



#6. Guess My Number
# You decide you want to play a game where you are hiding 
# a number from someone.  Store this number in a variable 
# called 'answer'.  Another user provides a number called
# 'guess'.  By comparing guess to answer, you inform the user
# if their guess is too high or too low.

# Fill in the conditionals below to inform the user about how
# their guess compares to the answer.
# '''
# answer = 10
# guess = 10

# if answer > guess:
#     result = "Oops!  Your guess was too low."
# elif answer < guess:
#     result = "Oops!  Your guess was too high."
# elif answer == guess:
#     result = "Nice!  Your guess matched the answer!"

# print(result)


#7. Tax Purchase
# Depending on where an individual is from we need to tax them 
# appropriately.  The states of CA, MN, and 
# NY have taxes of 7.5%, 9.5%, and 8.9% respectively.
# Use this information to take the amount of a purchase and 
# the corresponding state to assure that they are taxed by the right amount.

# state = "TX"
# purchase_amount = 20

# if state == "CA":
#   tax_amount = 0.075
#   total_amount = purchase_amount*(1+tax_amount)
#   result = "Since you are from {}, your total cost is {}".format(state, total_amount)
# elif state == "MN":
#   tax_amount = 0.095
#   total_amount = purchase_amount*(1+tax_amount)
#   result = "Since you are from {}, your total cost is {}".format(state, total_amount)
# elif state == "NY":
#   tax_amount = 0.089
#   total_amount = purchase_amount*(1+tax_amount)
#   result = "Since you are from {}, your total cost is {}".format(state, total_amount)
# else:
#   result = "Please enter valid state name"

# print(result)


#8. bmi calculation
# weight = 59
# height = 170
# print(weight)
# print(height)
# if 18.5 <= weight / height**2 < 25:
#   result = "BMI is consider 'normal'"
# else:
#   result = "BMI is consider 'abnormal'"

# print(result)


#9. and or not
# is_raininig = True
# is_sunny = True
# if is_raininig and is_sunny:
#   result = "Is there a rainbow"
# elif is_raininig and (not is_sunny):
#   result = "It's a rainy day"
# elif is_sunny and (not is_raininig):
#   result = "It's a sunny day"
# elif (not is_raininig) and (not is_sunny):
#   result = "It's a winter!"

# print(result)
  
#10. more - and or not

# location = "USA"
# location = "CAN"
# unsubscribed = False 
# if (not unsubscribed) and (location == "USA" or location == "CAN"):
#   print("Please send email")
# else:
#   print("Don't send email")

#11.



