import random
name = str(input("What is your name"))
print("hello",name,"welcome to our game!")
correct_number = random.randint(0,10)
guess_no=()
no_of_guesses= int()
while guess_no != correct_number:
  guess_no= int(input("now guess a number from 1 to 10"))
  if guess_no > 10 or guess_no < 0:
    print("invalid number typed")
  if guess_no < correct_number:
    print ("too low")
    no_of_guesses= no_of_guesses + 1
  elif guess_no > correct_number:
    print("too high")
    no_of_guesses= no_of_guesses + 1
  else:
    print(" you got it correct")
    no_of_guesses= no_of_guesses + 1
print("you are the winner")
print("it took you",no_of_guesses,"tries to get it right")
add_lead = str(input("do you want to save your number of tries on the leaderboard"))
f = open("leaderboard.txt","a")
if add_lead.lower() == "yes":
  f.writelines(name + ":" + str(no_of_guesses) + "tries ")
  f.close()
elif add_lead.lower() == "no":
  print("okay, we hope you had fun")
else:
  print("answer")
