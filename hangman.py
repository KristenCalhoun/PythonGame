# -*- coding: utf-8 -*-
  
import matplotlib.pyplot as plt # standard short name
import random

plt.ion() # sets “interactive on”: figures redrawn when updated

def picks():
    a = [] # make an empty list

    # Why all the brackets below? 
    # a += [  brackets here to add an iterable onto a list      ]
    #    random.choice(   [brackets here to choose from a list] )
    a += [random.choice([1, 3, 10])]

    for choices in range(5):
        a += [random.choice([1, 3, 10])]

    plt.hist(a)
    plt.show()
    
def roll_hundred_pair():
    total=[] #my total is the sum of the 2 dice per roll
    for rolls in range(100):#range means number of rolls
        dice1= random.choice([1,2,3,4,5,6])
        dice2= random.choice([1,2,3,4,5,6])
        total+=[dice1+dice2] #add the dice together from each roll
        print(total)
    plt.hist(total)
    plt.show()
    
def dice(n):
    total=0 #sum of random roll (initialized at zero)
    for rolls in range(n):#number of user input rolls
        dice1=random.choice([1,2,3,4,5,6]) #dice options
        total+=dice1#add total to dice
    print(total)#print total 
    
        
        
def hangman_display(guessed,secret): #name function
        for guessed in "secret": #compare the letter guessed to the secret word
        
        #put letter(s) that matched in the correct location 
        #keep guessing until the entire word is revealed
       estring=[]
    estring+=['a']
        