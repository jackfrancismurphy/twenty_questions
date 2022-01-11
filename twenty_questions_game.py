
import json

#Tidy code 

#to add
# Add a hint function!



Harry_Potter = {
    "fictional":"Yes",
    "alive":"N/A",
    "male":"Yes",
    "female":"No",
    "historic":"No",
    "ruler":"No",
    "entertainer":"No",
    "singer":"No",
    "actor":"No",
    "American":"No",
    "English":"Yes",
    "superhero":"No",
    "magic":"Yes",
    "adult":"No",
    "child":"No",
    "white":"Yes",
    "POC":"No",
    "film":"No",
    "TV":"No",
    "book":"Yes",
    "folk tale":"No",
    "wealthy":"No",
    "humanitarian":"No",
    "older":"No",
    "video":"No"
    }
Elon_Musk = {
   "fictional":"No",
    "alive":"Yes",
    "male":"Yes",
    "female":"No",
    "historic":"No",
    "ruler":"No",
    "entertainer":"No",
    "singer":"No",
    "actor":"No",
    "American":"No",
    "English":"No",
    "superhero":"No",
    "magic":"No",
    "adult":"Yes",
    "child":"No",
    "white":"Yes",
    "POC":"No",
    "film":"No",
    "TV":"No",
    "book":"No",
    "folk tale":"No",
    "wealthy":"Yes",
    "humanitarian":"No",
    "older":"No",
    "video":"No",
}
Cleopatra = {
    "fictional":"No",
    "alive":"No",
    "male":"No",
    "female":"Yes",
    "historic":"Yes",
    "ruler":"Yes",
    "entertainer":"No",
    "singer":"No",
    "actor":"No",
    "American":"No",
    "English":"No",
    "superhero":"No",
    "magic":"No",
    "adult":"Yes",
    "child":"No",
    "white":"No",
    "POC":"Yes",
    "film":"No",
    "TV":"No",
    "book":"No",
    "folk tale":"No",
    "wealthy":"No",
    "humanitarian":"No",
    "older":"Yes",
    "video":"No",
}
Jesus = {
    "fictional":"No",
    "alive":"No",
    "male":"Yes",
    "female":"No",
    "historic":"No",
    "ruler":"No",
    "entertainer":"No",
    "singer":"No",
    "actor":"No",
    "American":"No",
    "English":"No",
    "superhero":"No",
    "magic":"No",
    "adult":"Yes",
    "child":"No",
    "white":"Yes",
    "POC":"Yes",
    "film":"No",
    "TV":"No",
    "book":"Yes",
    "folk tale":"No",
    "wealthy":"Yes",
    "humanitarian":"Yes",
    "older":"No",
    "video":"No",
}
Queen_Elizabeth_II ={
    "fictional":"No",
    "alive":"Yes",
    "male":"No",
    "female":"Yes",
    "historic":"No",
    "ruler":"Yes",
    "entertainer":"No",
    "singer":"No",
    "actor":"No",
    "American":"No",
    "English":"Yes",
    "superhero":"No",
    "magic":"No",
    "adult":"Yes",
    "child":"No",
    "white":"Yes",
    "POC":"No",
    "film":"No",
    "TV":"No",
    "book":"No",
    "folk tale":"No",
    "wealthy":"Yes",
    "humanitarian":"No",
    "older":"Yes",
    "video":"No"
}
Bob_Marley = {
    "fictional":"No",
    "alive":"No",
    "male":"Yes",
    "female":"No",
    "historic":"No",
    "ruler":"No",
    "entertainer":"No",
    "singer":"Yes",
    "actor":"No",
    "American":"No",
    "English":"No",
    "superhero":"No",
    "magic":"No",
    "adult":"Yes",
    "child":"No",
    "white":"No",
    "POC":"Yes",
    "film":"No",
    "TV":"No",
    "book":"No",
    "folk tale":"No",
    "wealthy":"Yes",
    "humanitarian":"No",
    "older":"No",
    "video":"No"
}
Marge_Simpson = {
    "fictional":"Yes",
    "alive":"N/A",
    "male":"No",
    "female":"Yes",
    "historic":"No",
    "ruler":"No",
    "entertainer":"No",
    "singer":"No",
    "actor":"No",
    "American":"Yes",
    "English":"No",
    "superhero":"No",
    "magic":"No",
    "adult":"Yes",
    "child":"No",
    "white":"Yes",
    "POC":"No",
    "film":"No",
    "TV":"Yes",
    "book":"No",
    "folk tale":"No",
    "wealthy":"No",
    "humanitarian":"No",
    "older":"No",
    "video":"No"
}
Kim_Kardashian = {
    "fictional":"No",
    "alive":"Yes",
    "male":"No",
    "female":"Yes",
    "historic":"No",
    "ruler":"No",
    "entertainer":"Yes",
    "singer":"No",
    "actor":"No",
    "American":"Yes",
    "English":"No",
    "superhero":"No",
    "magic":"No",
    "adult":"Yes",
    "child":"No",
    "white":"Yes",
    "POC":"No",
    "film":"No",
    "TV":"No",
    "book":"No",
    "folk tale":"No",
    "wealthy":"No",
    "humanitarian":"Yes",
    "older":"No",
    "video":"No"
}
Florence_Nightingale = {
    "fictional":"No",
    "alive":"No",
    "male":"No",
    "female":"Yes",
    "historic":"Yes",
    "ruler":"No",
    "entertainer":"No",
    "singer":"No",
    "actor":"No",
    "American":"No",
    "English":"Yes",
    "superhero":"No",
    "magic":"No",
    "adult":"Yes",
    "child":"No",
    "white":"Yes",
    "POC":"No",
    "film":"No",
    "TV":"No",
    "book":"No",
    "folk tale":"No",
    "wealthy":"No",
    "humanitarian":"Yes",
    "older":"Yes",
    "video":"No",
}
Superman = {
    "fictional":"Yes",
    "alive":"N/A",
    "male":"Yes",
    "female":"No",
    "historic":"No",
    "ruler":"No",
    "entertainer":"No",
    "singer":"No",
    "actor":"No",
    "American":"Yes",
    "English":"No",
    "superhero":"Yes",
    "magic":"No",
    "adult":"Yes",
    "child":"No",
    "white":"Yes",
    "POC":"No",
    "film":"Yes",
    "TV":"No",
    "book":"No",
    "folk tale":"No",
    "wealthy":"No",
    "humanitarian":"No",
    "older":"No",
    "video":"No",
}
Spider_man = {
    "fictional":"Yes",
    "alive":"N/A",
    "male":"Yes",
    "female":"No",
    "historic":"No",
    "ruler":"No",
    "entertainer":"No",
    "singer":"No",
    "actor":"No",
    "American":"Yes",
    "English":"No",
    "superhero":"Yes",
    "magic":"No",
    "adult":"No",
    "child":"No",
    "white":"Yes",
    "POC":"No",
    "film":"Yes",
    "TV":"No",
    "book":"No",
    "folk tale":"No",
    "wealthy":"No",
    "humanitarian":"No",
    "older":"No",
    "video":"No"
}
Mario = {
    "fictional":"Yes",
    "alive":"N/A",
    "male":"Yes",
    "female":"No",
    "historic":"No",
    "ruler":"No",
    "entertainer":"No",
    "singer":"No",
    "actor":"No",
    "American":"No",
    "English":"No",
    "superhero":"No",
    "magic":"No",
    "adult":"Yes",
    "child":"No",
    "white":"Yes",
    "POC":"No",
    "film":"No",
    "TV":"No",
    "book":"No",
    "folk tale":"No",
    "wealthy":"No",
    "humanitarian":"No",
    "older":"No",
    "video":"Yes"
}
Santa = {
    "fictional":"Yes",
    "alive":"N/A",
    "male":"Yes",
    "female":"No",
    "historic":"No",
    "ruler":"No",
    "entertainer":"No",
    "singer":"No",
    "actor":"No",
    "American":"No",
    "English":"No",
    "superhero":"No",
    "magic":"Yes",
    "adult":"Yes",
    "child":"No",
    "white":"Yes",
    "POC":"No",
    "film":"No",
    "TV":"No",
    "book":"No",
    "folk tale":"No",
    "wealthy":"No",
    "humanitarian":"Yes",
    "older":"Yes",
    "video":"No"
    }

Cinderella = {
    "fictional":"Yes",
    "alive":"N/A",
    "male":"No",
    "female":"Yes",
    "historic":"No",
    "ruler":"No",
    "entertainer":"No",
    "singer":"No",
    "actor":"No",
    "American":"No",
    "English":"No",
    "superhero":"No",
    "magic":"No",
    "adult":"Yes",
    "child":"No",
    "white":"Yes",
    "POC":"No",
    "film":"No",
    "TV":"No",
    "book":"No",
    "folk tale":"Yes",
    "wealthy":"No",
    "humanitarian":"No",
    "older":"No",
    "video":"No"
    }

Peter_Pan = {
    "fictional":"Yes",
    "alive":"N/A",
    "male":"Yes",
    "female":"No",
    "historic":"No",
    "ruler":"No",
    "entertainer":"No",
    "singer":"No",
    "actor":"No",
    "American":"No",
    "English":"No",
    "superhero":"No",
    "magic":"Yes",
    "adult":"No",
    "child":"Yes",
    "white":"Yes",
    "POC":"No",
    "film":"No",
    "TV":"No",
    "book":"No",
    "folk tale":"Yes",
    "wealthy":"No",
    "humanitarian":"No",
    "older":"No",
    "video":"No"
    }

Alice = {
    "fictional":"Yes",
    "alive":"N/A",
    "male":"No",
    "female":"Yes",
    "historic":"No",
    "ruler":"No",
    "entertainer":"No",
    "singer":"No",
    "actor":"No",
    "American":"No",
    "English":"Yes",
    "superhero":"No",
    "magic":"No",
    "adult":"No",
    "child":"Yes",
    "white":"Yes",
    "POC":"No",
    "film":"No",
    "TV":"No",
    "book":"Yes",
    "folk tale":"No",
    "wealthy":"No",
    "humanitarian":"No",
    "older":"No",
    "video":"No"
    }

name_list = ['Harry Potter','Elon Musk', 'Jesus', 'Cleopatra', 'Queen Elizabeth II', 'Bob Marley', 'Marge Simpson', 'Kim Kardashian', 'Florence Nightingale', "Superman", "Spider man", "Mario", "Santa", "Cinderella", "Alice", "Peter Pan"]


def name_randomiser(lis):
    
    import random 
    
    return random.choice(lis)

answer = name_randomiser(name_list)



#Creating the answer_dict variable

if answer == 'Harry Potter':
    answer_dict = Harry_Potter

if answer == 'Elon Musk':
    answer_dict = Elon_Musk
    
if answer == 'Jesus':
    answer_dict = Jesus

if answer == 'Cleopatra':
	answer_dict = Cleopatra

if answer == 'Queen Elizabeth II':
	answer_dict = Queen_Elizabeth_II

if answer == 'Bob Marley':
	answer_dict = Bob_Marley

if answer == 'Marge Simpson':
	answer_dict = Marge_Simpson
    
if answer == 'Kim Kardashian':
    answer_dict = Kim_Kardashian

if answer == 'Florence Nightingale':
    answer_dict = Florence_Nightingale

if answer == "Superman":
    answer_dict = Superman

if answer == "Spider man": 
    answer_dict = Spider_man

if answer == "Mario":
    answer_dict = Mario

if answer == "Santa":
    answer_dict = Santa 

if answer == "Cinderella":
    answer_dict = Cinderella

if answer == "Peter Pan":
    answer_dict = Peter_Pan

if answer == "Alice":
    answer_dict = Alice




#functions for game logic

def asking_phase():
	player_answer = input(f'Question {question_count} \n').replace('?','')
    
	return player_answer


def check_answer():
    if player_answer == answer:
        return True
    
    for e in player_answer.split():
        if e in answer_dict.keys():
           print(answer_dict[f"{e}"])
           return False  
    
    for e in player_answer.split():
        if e not in answer_dict.keys():
            print("Guess again! (and state your guess, i.e: \"Jack Murphy\".) \nNeither yes nor no? Check the properties!")
            return False    




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


