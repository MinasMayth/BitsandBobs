#Name, Age and in which year you'll turn 100 years old
currentyear = int (input("What is the current year? "))
print ("Alright, nice to meet you! We're starting with something very simple.")
name = str(input ("So, first I'll need you to tell me your name: "))

age = int(input(name + ", what a nice name! \nHow old are you, " + name+"? "))

age_until_100 = int (100 - age)

year_when_100 = currentyear + int (age_until_100)

print ("You'll be 100 years old in the year " + str (year_when_100) + "!")


number = int (input( "Alright, give me a number, any number! "))

print ("Now, I'm going to repeat the sentence about your age the number of times you just said!")

print (( name + ", You'll be 100 years old in the year " + str (year_when_100) + "!\n") * number)
