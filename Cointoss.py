import random 

#Game rules 
Hero_toss = input("Heads or Tails? \n").capitalize()
print("You chose " + Hero_toss ) 
picks = ['Heads', 'Tails']
cointoss_random = random.choices(picks)
print("The toss landed on" , cointoss_random)
if Hero_toss == cointoss_random:
    print("Yessssir , you won!")
else:
    print("Hahaaaaaa , you lost try again!")