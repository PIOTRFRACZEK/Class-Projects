import random

#builbing colors and styles
class color:
   PURPLE = '\033[95m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   
# introducing frame
# welcoming
# title
# version
# autor
# rights
print("+---------------------------------------------------------------+")
print("|                          W E L C O M E !                      |")
print("|                              I N                              |")
print("|                  ``T H E   M E G A M A I N D  ``              |")
print("|                          version 1.2                          |")
print("+---------------------------------------------------------------+")
print("|                Game written by Piotr Fraczek                  |")
print("+---------------------------------------------------------------+")
print("|     © Copyright 2021 Piotr Fraczek. All Rights Reserved.      |")
print("+---------------------------------------------------------------+")

# players name and his greeting
playerName=input("\n\n > > > >Please enter your name: ")
print("#######################################################################\n")
print(color.BOLD +color.UNDERLINE+"Welcome "+playerName+color.END +". ’’THE MEGAMAID’’is a multiple-choice quiz \nthat is fully interactive. To beat the game, you'll have to answer \na series of questions correctly. So your aim should be to score \nas many points as possible. There's no timer, so take your time \nanswering the questions. The rules of ’’THE MEGAMAID’’are simple: ")
print("   *     *     *     *     *     *     *     *     *     *     *     *")
print("...before we start!")

# rules of the game
print(color.BOLD+color.UNDERLINE+"Rules in the game:"+ color.END +"\n\n1. First, choose the number of questions you would like to answer \nin the round. You can choose between 3 or 5 questions.\n2. Once a question is posed, you'll be given three options: a, b and c. \nUse your judgement to select the correct answer. That means you can \nonly choose a, b or c. When entering your answer, ensure that you use \na lowercase letter. Take the following example:\nQ1. What is the main ingredient of marshmallow: \n   a) Egg whites \n   b) Glucose Syrup, Sugar \n   c) gelatine\n If you feel b is the correct answer, when prompted, enter simply the letter b.\n3. If you answer the question posed correctly, you get 10 points. Conversely, \na wrong answer is worth 0 points.\n4. To be the victor, a certain number of points must be obtained:\n   a) round with 3 questions 20 points.\n   b) round with 5 questions 40 points.")

# the player must implement accept or not the rules
agreement_answere=input("\n\n > > > >Are you happy to play the game with those rules? (yes or no):").lower()


# verification of the answer entered by the player
#(only yes or no accepted otherwise repeat the question)//lowercase
while agreement_answere!='no' and agreement_answere!='n' and agreement_answere!= 'yes' and agreement_answere!='y':
    print("I`m so sorry but you can choose only yes or no. \n...Let`s try again :)")
    agreement_answere =input(" > > > >Enter your answere? (yes or no):").lower() 
print("You choose ", agreement_answere,"!\n")

# verification of the player's answer
# yes - we play
# no - the end of the game
if agreement_answere=='no' or agreement_answere=='n':
    print("“Thank you for visit "+playerName+". See you next time!”. \nEnd the game")
    exit()
print("“Thank you for playing "+playerName+"!”")


  
# establish a list with a (question/answers) and the correct answer
def get_game_statements():
    
    statements=[]
# I used spaces because '\t' made too big gaps -...\n   a) Five, \n   b) Seven, \n   c) Nine", "c"]    
    statements.append(["According to the old adage, how many lives does a cat have? \n   a) Five, \n   b) Seven, \n   c) Nine", "c"])
    statements.append(["Which country shares a land border with the UK? \n   a) Portugal, \n   b) Ireland, \n   c) Vietnam", "b"])
    statements.append(["By what abbreviation is a compact disc commonly known? \n   a) CD, \n   b) COD, \n   c) CDIS", "a"])
    statements.append(["Which salad dressing is named after a group of islands in the St Lawrence river? \n   a) Ten Island, \n   b) Hundred Island, \n   c) Thousand Island", "c"])
    statements.append(["What is the French for 'king'? \n   a) Kaiser, \n   b) Roi, \n   c) Herzog", "b"])
    statements.append(["From which of these do cats commonly suffer? \n   a) Fastballs, \n   b) Hairballs, \n   c) Meatballs", "b"])
    statements.append(["Black Eyed Peas had a UK charttopper in 2003 with 'Where is the...'? \n   a) Love, \n   b) Chip Shop, \n   c) Bus Stop", "a"])
    statements.append(["Which brothers finished first and second in the 2003 Canadian Formula 1 Grand Prix? \n   a) The Montoyas, \n   b) The Schumachers, \n   c) The Barrichellos", "b"])
    statements.append(["Which of the following involves events such as bareback riding and bull riding? \n   a) Threeday eventing, \n   b) Show jumping, \n   c) Rodeo", "c"])
    statements.append(["Which law states that if anything can go wrong, it will? \n   a) Parkinson's Law, \n   b) Boyle's Law, \n   c) Murphy's Law", "c"])
              
    return statements

#the player can choose 3 or 5 questions per round - player choice
number_of_questions=input(" > > > >How many questions you want to answer in a given round, 3 or 5? : ")

# players answer verification
# only the number 3 or 5 is acceptable
# another prompt repeats the question
while number_of_questions!='3' and number_of_questions!='5':
    print("\nI`m so sorry but you can choose only number 3 or 5. \nLet`s try again :)")
    number_of_questions=input(" > > > >How many questions you want to answer in a given round, 3 or 5? : ")
print("You choose ",number_of_questions," question in this round.")
print("\n\n*****START***************\n**********START**********\n***************START*****")

# defining the response as an integer
number_of_questions=int(number_of_questions) 

# main game function
def play_quiz():

#get game_statments
    game_statements=get_game_statements()
    
#randomise statments
    random.shuffle(game_statements)

#set player score to 0
    score = 0;
    
#set players question number to 1  
    questionNumber= 1;
    
# show statment using the loop//Q numeration
    for single_statement in game_statements[:number_of_questions]:
# present statment
        print("Choose only one answere a, b or c:"+"\nQ"+ str(questionNumber)+ "." + single_statement[0])
# user guess input//lowercase
        guess=input(" > > > >Enter your answere: ").lower()
       
#choice of a,b or c only
        while guess!='a' and guess!='b' and guess!='c':
            print("I`m so sorry but you can choose only a, b or c:. Let`s try again :)")
            guess=input(" > > > >Enter your answere: ")
        print("You choose ",guess,".")
# update players question number//integer
        questionNumber=int(questionNumber)+1
        
        
# check if guess is correct
        if guess== single_statement[1]:
            print(" # “Congrats "+playerName+". You got 10 points!!!“ # \n")
# update score
            score=score+10
        else:
            print(" # “Aww, what a shame. That wasn’t the correct answer. You got 0 points.“ # \n")
        
#final score
    maxPoints=str(10*number_of_questions)
    print(playerName + " your final score is: "  + str(score)+" / "+str(maxPoints))
    
# player is victor or not
# victor for 5Q
# victor for 3Q
# lost a game
    if number_of_questions==5 and score>=40:
        print("******************************************************************")
        print("“Bravo, bravo "+playerName+"! You’ve won the round!” \n")
        print("******************************************************************")
    elif number_of_questions==3 and score>=20:
        print("******************************************************************")
        print("“Bravo, bravo "+playerName+"! You’ve won the round!” ")
        print("******************************************************************")
    else:
        print("******************************************************************")
        print("“Oh dear. So close and yet so far. Good luck next time "+playerName+"!” ")
        print("******************************************************************")
    
    
# do you want to play again
# only acceptable yes or no//lowercase
# another answer repeats the question
def play_again():
    response=input("\n > > > >Would you like to play again? (yes or no):").lower() 
    while response!='no' and response!='n' and response!= 'yes' and response!='y':
        print("I`m so sorry but you can choose only yes or no. Let`s try again :)")
        response =input("Enter your answere? (yes or no):").lower() 
    print("You choose ", response,".\n\n\n")
    
    if response=='yes'or response=='y':
        print("**********************************************************************\nNEXT ROUND!!!\n\n***************START**************************************************")
        return True
    else:
        return False
play_quiz()
# play again function in a loop until response: no
while play_again():
    play_quiz()
print("“Thank you for playing "+playerName+". See you next time!”. \nEnd the game")



