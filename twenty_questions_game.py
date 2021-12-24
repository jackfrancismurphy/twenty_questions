#Hi Jack, happy birthday. Send this task to 3 more people. Please add the new people to the name_list and object_answer things 


#variables and variable creation

successful_answer = 'nay'
#answer = 'Harry Potter' 
name_list = ['Harry Potter','Elon Musk', 'Jesus']


def name_randomiser(lis):
    
    import random 
    
    return random.choice(lis)

answer = name_randomiser(name_list)





#to add
#['Beyonce', 'Will Smith', 'Bill Gates', 'Bob Marley', 'Queen Elizabeth II', 'Cleopatra', 'Kim Kardashian', 'Florence Nightingale', 'Harry Potter', 'Superman', 'Spider-Man', 'Mario', 'Santa', 'Hermione', 'Cinderella', 'Peter Pan', 'Alice', 'Marge Simpson']

# to make name catcher names will have to be list of list of names e.g
# name_list = [['Elon Musk'], ['Jesus', 'Jesus Christ']]
# in check_answer() will have to change code at line 2 to 'if player_answer in answer'
# That won't work with check answer!!!

#work out how to change check_answer() based on what the answer is 



class Person:
    def __init__(self, name, fictional, alive, male, female, historic, ruler, entertainer, singer, actor, American, English, superhero, magic, adult, child, white, POC, film, TV, book, folk_tale, wealthy, humanitarian, older, video):
        
        
        self.name = name
        self.fictional = fictional
        self.alive = alive
        self.male = male
        self.female = female
        self.historic = historic
        self.ruler = ruler
        self.entertainer = entertainer
        self.singer = singer
        self.actor = actor
        self.American = American
        self.English = English
        self.superhero = superhero
        self.magic = magic
        self.adult = adult
        self.child = child
        self.white = white
        self.POC = POC
        self.film = film
        self.TV = TV
        self.book = book
        self.folk_tale = folk_tale
        self.wealthy = wealthy
        self.humanitarian = humanitarian
        self.older = older
        self.video = video



#Instantiating the people
#Remember to add names to list below and to name_list above
Harry_Potter = Person('Harry Potter', 'Yes', 'N/A', 'Yes', 'No', 'No', 'No','No', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No') 
Elon_Musk = Person('Elon Musk', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No')
Jesus = Person('Jesus', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Yes', 'N/A', 'No' )
Cleopatra = Person('Cleopatra', 'No', 'No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No')
Queen_Elizabeth_II = Person('Queen Elizabeth II', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No')
Bob_Marley = Person('Bob Marley', 'No', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No', 'Yes', 'Yes', 'No' 'No')


Marge_Simpson = Person('Marge Simpson', 'Yes', 'N/A' 'No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'Yes', 'No', 'No', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'No', 'No', 'No','No','No')



#Creating the answer_object variable
if answer == 'Harry Potter':
    answer_object = Harry_Potter

if answer == 'Elon Musk':
    answer_object = Elon_Musk
    
if answer == 'Jesus':
    answer_object = Jesus

if answer == 'Cleopatra':
	answer_object = Cleopatra

if answer == 'Queen Elizabeth II':
	answer_object = Queen_Elizabeth_II

if answer == 'Bob Marley':
	answer_object = Bob_Marley

if answer == 'Marge Simpson':
	answer_object = Marge_Simpson
    

    
#I would like to replace this code some day.


def asking_phase():
	player_answer = input(f'Question {question_count} \n').replace('?','')
    
	return player_answer


def check_answer():
    if player_answer == answer:
        return True
    
    for e in player_answer.split():
        if e in answer_object.__dir__():
            print(getattr(answer_object,f"{e}"))
            return False  
    
    for e in player_answer.split():
        if e not in answer_object.__dir__():
            print("Guess again! \n Neither yes nor no? Check the properties!")
            return False    


    #cannot check the other condition unless the for loop completes entirely before going to the below.
    #print("please pick a property from above")
    #return False
    #wrong condition
            
#why isn't the variable 'guessed' being reassigned here?              
#how would we deal with Or questions?



#Game Logic

#Variables
guessed = False
question_count = 1

print(""" Welcome to 20 questions!
Guess the people according to their properties.  
The properties in this game are $eT, and those properties are:  
\n
Fictional, alive, male, female, historic, adult,
Child, white, POC (person of colour), ruler, 
Entertainer, singer, actor, American, 
English, wealthy, humanitarian*, older than 50,
\n 
and if the character is fictional then:
Superhero, magic, ** movie, TV, Book, folk tale, video game 
\n\
* Humanitarian here broadly means that they helped humanity 
** Is x mainly known from a movie/video game etc..? Not: do they star in one? \n """)

while guessed == False and question_count <21:

    player_answer = asking_phase()
    
    guessed = check_answer()
    question_count += 1
    
    if guessed == True:
        print(f'You guessed it! It was {answer}')

if question_count >20:
    print('You\'ve run out of questions. Try again')