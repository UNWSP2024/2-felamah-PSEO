#Write a program that inputs the ages of five friends, calculates the average age
# (as a decimal) and displays the average age to the user.
def average_age():
#Get User Input
    friendAge_1=float(input('what is your age?'))
    friendAge_2=float(input('what is your age?'))
    friendAge_3=float(input('what is your age?'))
    friendAge_4=float(input('what is your age?'))
    friendAge_5=float(input('what is your age?'))

 # Sum ages
    sum_ages = friendAge_1 + friendAge_2 + friendAge_3 + friendAge_4 + friendAge_5

# Average the ages
    average_age = sum_ages / 5
# Print the results
    print(average_age)
# Line which calls the above function.
average_age()