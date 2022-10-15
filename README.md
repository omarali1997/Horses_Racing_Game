# LAB - Class 06

## Project: Horses_Racing_Game

### Author: Omar Ali  & Amani M AL-Zoubi

### Game Description:
- This game has created by using OOP 
- the game runs on the cli 
    - it depends on the horse and how many rounds it races before it faints...
    - ask a user to enter the horse's name 
    and choose its breed; the user should choose from the list or he/she will get a message to 
    to choose it in the correct way 
    - the game will specify his/her contender randomly by calling the function "random_contender"
    - for more interaction we used time.sleep to keep the user seeing his/her game round by round and 
    also, we create a "Load Bar" to make the game more professional. 
    - and the game will start by call method that specifies the winner depends on its breed
    - if the horse wins it will go to the next round and the next round until it faints 
    - In each round, the horse wins horse's points will increase by 10 ...
    - if the result is tied horse points will decrease by 10...
    - if it fails its points will be zero 
    - same things for contender's points
    - user can play again and continue with the same number of rounds (not begin from zero) 
    - the game will finish once the user writes "n/N".

### Links and Resources

- No need for this lab

### Setup
- use python version 3.10.7
#### `.env` requirements (where applicable)

- For this lab we did not use .env

#### How to initialize/run your application (where applicable)

- python Horses_Racing_Game/horses_racing.py

#### How to use your library (where applicable)
- you need to install requirements.txt by using
- > pip install -r requirements.txt
#### Tests

- pytest tests/test_game.py 

#### Pull Requests
- [PULL REQUEST LINK](https://github.com/amani51/Horses-Racing-Game/pull/2)