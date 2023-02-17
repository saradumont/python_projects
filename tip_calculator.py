#If the bill was $150.00, split between 5 people, with 12% tip. 

# print greeting
print("Welcome to the tip calculator.")

# get inputs
bill = input("what was the total bill? $")
tip = input("What percentagetip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

#change input strings to integers
bill_num = float(bill)
tip_percent = float(tip)
people_num = float(people)

#get tip in float
tip_num = (tip_percent/100) + 1

#Each person should pay (150.00 / 5) * 1.12 = 33.6

amount = (bill_num/people_num) * tip_num
#Format the result to 2 decimal places = 33.60
amount_final = "{:.2f}".format(amount)

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print(f"Each person should pay: ${amount_final}")