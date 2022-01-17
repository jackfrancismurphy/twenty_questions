
#Variables and imports

    import json
    import random 
    
    guessed = False
    question_count = 1
    answer = []
    answer_dict = {}

    People = json.load(open("people_data.json", "r"))


#Randomiser and answer_dict variable

    def name_randomiser(lis_of_dics):  
    
        name_list = []
    
        for e in lis_of_dics:
            name_list.append(e["name"])
    
        return random.choice(name_list)
    
    
    answer = name_randomiser(People)
    

    
    def get_people(People, user_input):
        for person_data in People:
            if answer == person_data["name"]:
                return person_data
    

    answer_dict = get_people(People, answer)
    
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
    

