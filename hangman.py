from words import word_list
import random

def getRandom():
  word=random.choice(word_list)
  return word.upper()

def play(word):
  word_completion='_ '*len(word)
  guessed=False
  guessed_letters=[]
  guessed_words=[]
  tries=6
  print('Lets play HANGMAN !')
  print(displayHangman(tries))
  print(word_completion)
  print('\n')

  while not guessed and tries > 0:
    guess=input('Enter your guess:').upper()
    if len(guess)==1 and guess.isalpha():
      if guess in guessed_letters:
        print('You have already guessed the letter',guess)
      elif guess not in word:
        print(guess,'is not in the word.')
        tries-=1
        guessed_letters.append(guess)

      else:
        print('good job,',guess,'is in the word')
        guessed_letters.append(guess)
        word_as_list=list(word_completion)
        indices=[i for i,letter in enumerate(word)if letter==guess]
        for index in indices:
          word_as_list[index]=guess
          word_completion=''.join(word_as_list)
          if '_ 'not in word_completion:
            guessed=True
            

    elif len(guess)==len(word) and guess.isalpha():
      if guess in guessed_words:
        print('you have already guessed the word',guess)
      elif guess != word:
        print(guess,'is not in the word.')
        tries=-1
        guessed_words.append(guess)
      else:
        guessed=True
        word_completion=word    
    else:
      print('not a valid guess :(')

    print(displayHangman(tries))  
    print(word_completion)
  if guessed:
    print('congrats,you guessed the word! you win! ')
  else:
    print('sorry,you ran out of tries.')

def displayHangman(tries):
    stages = [ #6 final stage: head, torso, both arms, both legs
            """
                 ------------
                    |     |
                    |     o
                    |    \\//
                    |     |
                    |    / \\
                    -
            """,
            #5 head, torso,both arms, and one leg
            """
                 ----------
                    |      |
                    |      o
                    |      |
                    |      /
                    -
            """,
            #4 head, torso, and both arms
            """
                 -------
                    |     |
                    |     o
                    |    \\//
                    |      |
                    |
                    -
            """,
            #3 head, torso, and one arm
            """   
                 --------
                    |      |
                    |      o
                    |     \\|
                    |      |
                    |
                    -
            """,
            #2 head and torso
            """
                    --------
                    |      |
                    |      o
                    |      |
                    |      |
                    |
                    -
            """,
            #1 head
            """
                    --------
                    |      |
                    |      o
                    |      
                    |      
                    |
                    -
            """,
            #0 intial empty stage
            """
                    --------
                    |      |
                    |      
                    |      
                    |      
                     
                    -
            """,
        ]
    return stages[tries]                     
            

def main():
  word=getRandom()
  print(word)
  play(word)

  while input('do you want to play again?(Y/N): ').upper()=='Y':
    word=getRandom()
    print(word)
    play(word)
    
main()

RECORD
Lets play HANGMAN !

                    --------
                    |      |
                    |      
                    |      
                    |      
                     
                    -
            
_ _ _ _ _ _ 


Enter your guess:r
good job, R is in the word

                    --------
                    |      |
                    |      
                    |      
                    |      
                     
                    -
            
R _ R _ _ _ 
Enter your guess:y
Y is not in the word.

                    --------
                    |      |
                    |      o
                    |      
                    |      
                    |
                    -
            
R _ R _ _ _ 
Enter your guess:m
M is not in the word.

                    --------
                    |      |
                    |      o
                    |      |
                    |      |
                    |
                    -
            
R _ R _ _ _ 
Enter your guess:record

                    --------
                    |      |
                    |      o
                    |      |
                    |      |
                    |
                    -
            
RECORD
congrats,you guessed the word! you win! 
do you want to play again?(Y/N): n
 
