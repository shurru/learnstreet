#Hangman Project
#RETURN A 'HIDDEN' VERSION OF THE SUPPLIED SECRET WORD
def get_display(word):
    disp=""
    for i in word: 
        disp= disp+ '-'
    return disp
    # Given a string, "word", return a hidden version of it consisting
    # of dashes for the display.
    "REPLACE THIS CODE WITH YOUR get_display() METHOD"

#FIND IF THE LETTER IS IN THE WORD
def is_letter_in_word(word,letter):
    if (word==None): 
        return False 
    else: 
        if (word.find(letter)!= -1): 
            #-1 is returned when there is a failure of the find 
            #this means if the word is found, it returns true
            return True
        else: 
            return False
        
    # Given the word "word", check if it contains the letter "letter".
    "REPLACE THIS CODE WITH YOUR is_letter_in_word() METHOD"

#UPDATE GAME DISPLAY IF WE'VE BEEN GIVEN A MATCHING LETTER
def get_letter(word,letter,display):
    
    if word==None: 
        return False 
    else: 
        while (word.find(letter)!=-1): 
            index= word.find(letter)
            display= display[0:index]+letter+display[index+1:]
            word= word[0:index]+ '-' + word[index+1:]
    return display
        
    # This method is called by the Hangman program when your is_letter_in_word function
    # above returns True.
    # The parameters passed in are the guessed letter, the secret word,
    # and the current display state of the secret word.
    # This method will return a new display state of the secret word based on the matching letter.
    "REPLACE THIS CODE WITH YOUR get_lette() METHOD"

'''  
    RETURN 'finished' if game has finished 
    RETURN 'lose' if game has lossed 
    RETURN 'continue' if it is not finished
'''
def is_finished(word, display, left):
    if(left!=0):
        if(word==display):
            return 'finished'
        else:
            return 'continue'
    else:
        return 'lose'
    # This method is called each time you guess a letter. Its job is to
    # determine whether you have have won the game, lost the game,
    # or if the game should continue.
    # The input parameters passed are the secret word (word), the
    # current word display (display), and the number of chances left (left)
    # to reveal the secret word.
    # Return "finished" if you have successfully guessed the word, return
    # "lose" if you did not guess the word within the remaining chances,
    # or return "continue" if there are remaining chances to fully guess the secret word.
    "REPLACE THIS CODE WITH YOUR isFinished() METHOD"
