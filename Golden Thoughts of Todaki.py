# creating a file 'GoldenThoughts.txt' in the same location like *.py file is //'w'
FileWithParagraphs=open('GoldenThoughts.txt','w')

# I save both paragraphs of the text into the created file
FileWithParagraphs.write('What if I said that randomness, coincidence, chance, karma, miracle—all such notions do not exist? That from the moment a being is born, their future is already carved into stone? \nIf so, a being’s actions do not truly stem from his own choices, but are manipulated to suit the performance of a “conductor”. In that sense—prayer, perfection and imperfection, reality and dream, hope and despair, righteousness and wickedness, love and hatred and even life and death are but illusionary  oncepts—equally and utterly devoid of meaning.')


# I'm opening the file for reading purpouse //'r'
FileWithParagraphs=open('GoldenThoughts.txt','r')

#the writer can choose 1st or 2nd paragraph\\ loop: another answer will repeat the question
paragraph_number=input("Which paragraph number you want to display, 1st or 2nd? : ")
while paragraph_number!='1' and paragraph_number!='2':
    print("\nSorry, but you can choose only 1 or 2. \nYou can try again :)")
    paragraph_number=input(" Which paragraph number you want to display, 1st or 2nd?: ")
print("You choose ",paragraph_number," paragraph.")
print("\n\n******************************************************************")

# defining the response as an integer
paragraph_number=int(paragraph_number)

# defining a class for paragraph, name, aurhor rights
class Paragraphs:
    def __init__(self, paragraph, name, aurhorRights):
        self.paragraph = paragraph
        self.name = name
        self.aurhorRights = aurhorRights
   
# displaying an paragraph depending on the writer's choice
if paragraph_number==1:
	text1 = Paragraphs(str(FileWithParagraphs.readlines()[0]), '\nAuthor name: Todoki', '\n© Copyright 2021 Todoki. All Rights Reserved. ')
	print (text1.paragraph)
	print (text1.name)
	print (text1.aurhorRights)
elif paragraph_number==2:
	text2 = Paragraphs(str(FileWithParagraphs.readlines()[1]), '\nAuthor name: Todoki','\n© Copyright 2021 Todoki. All Rights Reserved. ')
	print (text2.paragraph)
	print (text2.name)
	print (text2.aurhorRights)
# I close the previously opened file for reading
FileWithParagraphs.close()

# it is an Coding Exercise 4 Piotr Fraczek