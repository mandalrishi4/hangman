from wordpicker import wordpickeer



# Hello game Hangman
#________________________________________________________________welcome____________________________________________________________
def wlcome():

    print("Hi Welcome to Hangman")
    print("------------------------------------------------------------------------------------------------")
    print("-----------------------------------The game is--------------------------------------------------")
    print("------------------------------------------------------------------------------------------------")
    print("You have to guess a letter in the word. If you guess incorectly the hangman will die")
    print("------------------------------------------------------------------------------------------------")
    print(" "*200)

    runner(chances)



#Word will be imported

word = list(wordpickeer())



#cahnces and empty guessed word

chances = 5
guessing_word=[]
for i in word:
    guessing_word.append("_")

guessed_word=[]






#hangman

def hangman(lo):
    if lo == 5:
        print("0")
        
    elif lo == 3:
        print(" 0 ")
        print(" | ")
        print("/|\ ")

    elif lo == 4:
        print("0")
        print("|")

    elif lo == 2:
        print(" 0 ")
        print(" | ")
        print("/|\ ")
        print(" | ")
    elif lo == 1:
        print(" 0 ")
        print(" | ")
        print("/|\ ")
        print(" | ")
        print("/ \ ")
    

                   





#Winning fucntion

def win():
        print("You saved the man")








#Loop will run till game won or  lost
#________________________________________________________________runner____________________________________________________________
def runner(chances):

    game = True
    while game != False:

       
    
    
    
    
    
        #Chances Left , word
    
        #guess a letter
    
        letterg= input("Guess a Letter User: ").upper()            
               
    
        #if letter in word
                
        if letterg in word:
    
            if letterg in guessed_word:
                print("You have Already guessed")
    
            else:
    
                guessed_word.append(letterg)
                for i in range(len(word)):
    
                    charac = word[i]
                    if charac == letterg:
                        guessing_word[i] = word[i]                        
    
        else:
    
            if letterg in guessed_word:
                print("You have Alreaddy guessed")
                print("                  ")
    
            else:
                guessed_word.append(letterg)
                print(" ")
                print("Wrong Choice")
                print(" ")
                chances = chances - 1
                
    
    
        
        


        print(guessing_word)
        print(" ")
        hangman(chances)  
        print(" ")          
        print("chances left are: "+ str(chances))
        print(" ")
       
        #game won all letter guessed

        if guessing_word == word:
            win()
            game = False
    
    #chance lost game lost
        if chances == 0:
            game = False
            print(" 0 ")
            print("---")
            print(" | ")
            print("/|\ ")
            print(" | ")
            print("/ \ ")
            print(" ")
            print("HE DIED")


#spacing_______________________________________


        print(" "*1000)

wlcome()