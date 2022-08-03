# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 17:02:47 2022

@author: SUHAANI
"""

''' 
In this game the player’s input should be
authenticated to ensure that they are an authorised player.

Then song names are inputted to the program and the first
letter of every word in the song and the artist is displayed.

Then the player has to guess the song name in two
guesses. 

If the guess is correct on the first try 3 points are
added to the players score 

If it is guessed correct on the
second time one point is added to their score 
if they guess

it incorrectly on the second try the game ends, game then
repeats. 

The player score is displayed at the end of the game.

I am going to split the program up into sections. 
Section 1 will be a username and password verification to make sure they are an authorised player.
Section 2 will be displaying the song name and the artist 
Section 3 will be to print out their final score

---------------------
Allows a player to enter their details, which are then authenticated to ensure that they are an
authorised player.
2. Stores a list of song names and artists in a 1d array.
3. Selects a song from the array, displaying the artist and the first letter of each word of the song title.
4. Allows the user up to two chances to guess the name of the song, stopping the game if they guess
a song incorrectly on the second chance.
5. If the guess is correct, add the points to the player’s score depending on the number of guesses.
6. Displays the number of points the player has when the game ends.
7. Stores the name of the player and their score in a 2d array.
8. Displays the score and player name of the top 5 winning scores from the 2d array.
'''

#usernames will be their insta username 
#password will be - yolo4eva

#SECTION1: authorization. are they allowed to play? 

name = input("Please enter your username: ")
flag = "false"

while flag == "false":
    password = input("Please enter the password: ")
    if password == "yolo4eva":
        print("Welcome ", name, " !")
        flag == "true"
        break
    else:
        print("Wrong password. Try again. ")
        
songs = [
    ["old town road", "lil nas x "],
    ["starving", "hailee steinfeld"],
    ["watermelon sugar", "harry styles"],
    ["kill my mind", "louis tomlinson"],
    ["blur ", "johnny orlando"],
    ["night changes", "one direction"]
    ]

print("Here is your hint. ")
print()

chosen_song = songs[1][0]
chosen_artist = songs[1][1]
chosen = chosen_song[0], chosen_artist
print(chosen)

points = 0 

guess1 = input("Please enter your first guess: ")

if guess1 == chosen_song:
    print("Awesome! You guessed it. ")
    points = points + 3
    
else:
    print("Try again. ")
    guess2 = input("Please enter your second guess: ")
    
    if guess2 == chosen_song:
        print("Awesome! You guessed it. ")
        points = points + 1 
    else:
        print("Game over. ")

print("Your total score is: ", str(points))

#repeat





