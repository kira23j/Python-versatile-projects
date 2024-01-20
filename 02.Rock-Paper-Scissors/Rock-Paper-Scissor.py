# this is rock , paper , scissor game made with python
    # rock wins against scissors
    # scissor win against paper
    # paper wins against rock
    
import random
rock='''
0000000000000
this is rock
0000000000000
'''
scissor='''
222222222222222
this is scissor
222222222222222
'''
paper='''
1111111111111
this is paper
1111111111111
'''
rule='''
        RULES
    # rock wins against scissors
    # scissor win against paper
    # paper wins against rock
'''
print(rule,rock, paper, scissor)
user_choice=int(input("what is your preference 0: for rock |1: for paper |2: for scissor :- "))

computer_choice=random.randint(0,2)
print(f"computer chooses: {computer_choice}")


while True:
    if user_choice==-1:
        break;
    
    elif user_choice>2 or computer_choice>2:
        print("wrong choice please update your choice")
    elif user_choice==0 and computer_choice==2:
        print("you win")
    elif user_choice==2 and computer_choice==0:
        print("computer win")
    elif user_choice==2 and computer_choice==1:
        print("you win")
    elif user_choice==1 and computer_choice==2:
        print("computer wins")
    elif user_choice==1 and computer_choice==0:
        print("you win")
    elif user_choice==0 and computer_choice==1:
        print("computer wins")
    else:
        print("no one wins, please try another game")
    
    
    user_choice=int(input("what is your preference 0: for rock |1: for paper |2: for scissor |-1: to Exit "))
    computer_choice=random.randint(0,2)
    
    
