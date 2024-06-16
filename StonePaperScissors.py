'''Rock, Paper, Scissors. The familiar game of Rock, 
Paper, Scissors is played like this: at the same time, 
two players display one of three symbols: a rock, paper, 
or scissors. A rock beats scissors, scissors beat 
paper by cutting it, and paper beats rock by covering it.'''

import random

def Check(computer, user):
 if computer == user :
  return 0 

 if computer == 0 and user == 2 :
  return -1

 if computer == 1 and user == 0 :
  return -1
 
 if computer == 2 and user == 1 :
  return -1
 
 return 1
 


computer = random.randint(0, 2)
user = int(input("Choose (0) for Rock, (1) for Paper and (2) for Scissors : "))


score = Check(computer, user)

print("You Choosed : ", user)
print("The Computer Choosed : ",computer)

if (score == 0) :
 print('"The Round Is Draw."')
 print("Better Luck Next Time.")
elif (score == -1) :
 print('"You Lose The Round."')
 print("Better Luck NExt Time")
else : 
 print('"You Won The Round"')
 print("Congratulations")