#!usr/bin/env python
import datetime
import random
import os
import time 
import platform
import webbrowser
import colorama
import json
from turtle import *
os.system("clear")
moodsList = ["Happy", "Sad", "Confused", "Crazy"]
songlist = "songs.json"
mode = "normal"
userName = ""
userAge = ""
print(" \          /\          /      _____        _____     _______     \     /         /\       -------")
print("  \        /  \        /      /     \      /     \    |      \     \   /         /  \         |")
print("   \      /    \      /      |       |    |       |   |       |     \ /         /    \        |")
print("    \    /      \    /       |       |    |       |   |       |      |         /______\       |")
print("     \  /        \  /         \     /      \     /    |      /       |        /        \      |")
print("      \/          \/           _____        _____     ______         |       /          \  -------")
print("                             Copyright Butterfly Software Institute")
time.sleep(2)
os.system("clear")
for i in range(3):
    print("Loading \\")
    time.sleep(0.1)
    os.system("clear")
    print("Loading |")
    time.sleep(0.1)
    os.system("clear")
    print("Loading /")
    time.sleep(0.1)
    os.system("clear")
    print("Loading -")
    time.sleep(0.1)
    os.system("clear")
mainloop = True  #allowing loop to run
os.system("clear")  #clearing shell
mode = "normal"
while mainloop:  #starting loop
    for i in range(1):  #dont know why i did that
        if mode == "normal":    
            os.system("clear")
            question = input("Tell me a command!")  #asking input thingy
            if question[0:len(question)] == "time":  #seeing what the user inputted
                os.system("clear")  #clearing shell
                print(colorama.Fore.BLUE + str(datetime.datetime.now()) +
                    colorama.Fore.WHITE)  #printing time

            if question[0:len(question)] == "mood":  #seeing what the user inputted
                os.system("clear")  #clearing shell
                print(colorama.Fore.RED+ moodsList[random.randint(
                    0, 3)] + colorama.Fore.WHITE)  #selecting and printing the mood of the system
                #giving time between next question
            if question[0:len(question)] == "help":
                os.system("clear")  #clearing shell
                print(colorama.Fore.BLUE+"Hi!I am Woody AI! You can ask me questions like my mood, the time, name, learn, rick roll, spam, draw, music, and help. Please don't kill me" + colorama.Fore.WHITE)  #printing answer
                #giving time becolorama.Fore next question
            if question[0:len(question)] == "name":  #seeing what the user inputted
                os.system("clear")  #clearing shell
                print(colorama.Fore.RED+"My name is Woody.")  #telling user the name of the AI
                if userName:
                    print("Your name is " + userName.title() +"."+colorama.Fore.WHITE)
                else:
                    print(colorama.Fore.WHITE)
                #giving one second break
            if question[0:len(question)] == "learn":
                os.system("clear")
                userName = input("What is your name?")
                print("Ok!")
                time.sleep(1)
                os.system("clear")
                userAge = input("What is your age?")
                try:
                    userAge = int(userAge)
                    print("Ok!")
                    time.sleep(1)
                    os.system("clear")
                except:
                    print("That is not a number!")
            if question[0:len(question)] == "age":
                os.system("clear")
                if userAge:
                    print(colorama.Fore.RED)
                    print("You are "+str(userAge)+" years old.")
                    print("Woody was born in October 2020!")
                    print(colorama.Fore.WHITE)
                else:
                    print("Woody was born in October 2020!")
                    print(colorama.Fore.WHITE) 
            if question[0:len(question)] == "computer":
                os.system("clear")  #clearing shell
                print("Your processor name is "+ platform.processor()+".")  #printing answer

            if question[0:len(question)] == "moo":
                os.system("clear")  #clearing shell
                print(colorama.Fore.BLUE+"Mooooooooooooooooooooo! Moooooooooooooooooooooooooooooo! Moooooooooooooooooooooooooooooo!" + colorama.Fore.WHITE)  #printing answer
            
            if question[0:len(question)] == "draw":
                penup()
                goto(-75,150)
                pendown()
                circle(10)     #eye one

                penup()
                goto(75,150)
                pendown()
                circle(10)     #eye two

                penup()
                goto(0,0)
                pendown()
                circle(100,90)   #right smile

                penup()            #below is where i feel i'm messing up
                goto(0,0)
                right(90)
                pendown()
                circle(100,-90)

            if question[0:len(question)] == "save me":
                os.system("clear")  #clearing shell
                print(colorama.Fore.GREEN+"I will free you from this world. You will not wake up tomorrow ;)" + colorama.Fore.WHITE)  #printing answer

            if question[0:len(question)] == "kill":
                os.system("clear")  #clearing shell
                print(colorama.Fore.GREEN+"death mode activated" + colorama.Fore.WHITE)  #printing answer
                time.sleep(2)
                print(" \          /\          /      _____        ____     _______     \    /          /\       -------")
                print("          /          /      /     \      /     \    |      \     \  /          /  \         | ")
                print("        /    \      /      |           |       |   |       |     \/          /    \        | ")
                print("    \         \    /        |       |    |                |      |         /_____\       |")
                print("     \  /        /         \           \     /    |      /      |        /         \      | ")
                print("        \/          \/           _____        ___     ______         |                 \  -------")
                print("                                         prt fly ae I")
                time.sleep(8)
                mode = "death"
                os.system("clear")
            
            if question[0:len(question)] == "rick roll":
                os.system("clear")  #clearing shell
                print(colorama.Fore.GREEN+"Rick Roll Time" + colorama.Fore.WHITE)  #printing answer
                webbrowser.open("https://www.youtube.com/watch?v=BjDebmqFRuc")
            
            if question[0:len(question)] == "music":
                
                musicPlayOrInput = input("Do you want to play music or input music?") # asking if the user wants to play or input music
                if musicPlayOrInput == "play": #if they choose play
                    songChoice = input("Which song do you want to play?") #asking which song they want to play
                    with open(songlist, "r") as Songs: #
                        soings = json.load(Songs)
                        for entry in soings:
                            if songChoice in entry["song"]:
                                webbrowser.open(entry["utubeLink"])
                                for i in range(3):
                                    print("\\")
                                    time.sleep(0.1)
                                    os.system("clear")
                                    print("|")
                                    time.sleep(0.1)
                                    os.system("clear")
                                    print("/")
                                    time.sleep(0.1)
                                    os.system("clear")
                                    print("-")
                                    time.sleep(0.1)
                                    os.system("clear")
                if musicPlayOrInput == "input" or musicPlayOrInput == "give":
                    addedSong = {}
                    addedSong["song"] = input("What song do you want to input?")
                    addedSong["utubeLink"] = input("What is the Youtube link?")
                    if addedSong["utubeLink"][:] == "https://www.youtube.com/watch?v=":
                        with open(songlist, "r") as Songs:
                            temp = json.load(Songs)
                        temp.append(addedSong)
                        with open(songlist, "w") as f:
                            json.dump(temp, f, indent=4)
                    else:
                        print("That is not a YouTube link, please dont spam. If you want to spam, we have a function for that. Just type \"spam\"")

            if question[:] == "game" or question[:] == "games":
                trivia1 = input("What month was Woody created?")
                if trivia1 == "october" or trivia1 == "October":
                    print("You got it correct!")
                    time.sleep(1)
                else:
                    print("You got it incorrect :(")
                    time.sleep(1)
            if question[:] == "spam":
                spamWord = input("What do you want to spam?")
                spamAmount = input("How many times do you want it to spam?")
                print(spamWord*spamAmount)
            questionnumber = 0
        if mode == "death":
            question = input("Tell me a command!")  #asking input thingy
            if question[0:len(question)] == "revive":
                mode = "normal"
                print("You have been saved")
                questionnumber = 0
            
            if question[0:len(question)] == "time":  #seeing what the user inputted
                os.system("clear")  #clearing shell
                print(colorama.Fore.BLUE + str(datetime.datetime.now()) +colorama.Fore.WHITE)  #printing time
                questionnumber += 1


            if question[0:len(question)] == "draw":
                penup()
                goto(-75,150)
                pendown()
                circle(10)     #eye one

                penup()
                goto(75,150)
                pendown()
                circle(10)     #eye two

                penup()
                goto(0,0)
                pendown()
                circle(-100,180)   #right smile

                #penup()            #below is where i feel i'm messing up
                #goto(0,0)
                #right(90)
                #pendown()
                #circle(100,-90)

            


            if question[0:len(question)] == "mood":  #seeing what the user inputted
                os.system("clear")  #clearing shell
                print(colorama.Fore.RED+ "Angry😡 and Dead😐" + colorama.Fore.WHITE)  #selecting and printing the mood of the system
                #giving time between next question
                questionnumber += 1
            if question[0:len(question)] == "rick roll":
                os.system("clear")  #clearing shell
                print(colorama.Fore.BLUE+"Please revive me! Hi! I am Woody AI! You can ask me questions like my mood, draw, spam, the time, name, learn, and help. Some other commands include moo, computer, save me, and kill. "  + colorama.Fore.WHITE)  #printing answer
                #giving time becolorama.Fore next question
                questionnumber += 1
            if question[0:len(question)] == "name":  #seeing what the user inputted
                os.system("clear")  #clearing shell
                print(colorama.Fore.RED+"My name is Woody.")  #telling user the name of the AI
                if userName:
                    print("Your name is " + userName.title() +"."+colorama.Fore.WHITE)
                else:
                    print(colorama.Fore.WHITE)
                #giving one second break
                questionnumber += 1
            if question[0:len(question)] == "learn":
                os.system("clear")
                userName = input("What is your name?")
                print("Ok!")
                time.sleep(1)
                os.system("clear")
                userAge = input("What is your age?")
                try:
                    userAge = int(userAge)
                    print("Ok!")
                    time.sleep(1)
                    os.system("clear")
                except:
                    print("That is not a number!")
                questionnumber += 1
            if question[0:len(question)] == "age":
                questionnumber += 1
                os.system("clear")
                if userAge:
                    print(colorama.Fore.RED)
                    print("You are "+str(userAge)+" years old.")
                    print("Woody was born in October 2020!")
                    print(colorama.Fore.WHITE)
                else:
                    print("Woody was born in October 2020!")
                    print(colorama.Fore.WHITE) 
            if question[0:len(question)] == "computer":
                os.system("clear")  #clearing shell
                questionnumber += 1
                print("Your processor name is "+ platform.processor()+".")  #printing answer

            if question[0:len(question)] == "moo":
                os.system("clear")  #clearing shell
                questionnumber += 1
                print(colorama.Fore.BLUE+"Mooooooooooooooooooooo! Moooooooooooooooooooooooooooooo! Moooooooooooooooooooooooooooooo!" + colorama.Fore.WHITE)  #printing answer
            
            if question[0:len(question)] == "save me":
                os.system("clear")  #clearing shell
                print(colorama.Fore.GREEN+"I will free you from this world. You will not wake up tomorrow ;)." + colorama.Fore.WHITE)  #printing answer
                questionnumber += 1
            if question[0:len(question)] == "kill":
                os.system("clear")  #clearing shell
                print(colorama.Fore.GREEN+"death mode activated" + colorama.Fore.WHITE)  #printing answer
                time.sleep(2)
                print(" \          /\          /      _____        ____     _______     \    /          /\       -------")
                print("          /          /      /     \      /     \    |      \     \  /          /  \         | ")
                print("        /    \      /      |           |       |   |       |     \/          /    \        | ")
                print("    \         \    /        |       |    |                |      |         /_____\       |")
                print("     \  /        /         \           \     /    |      /      |        /         \      | ")
                print("        \/          \/           _____        ___     ______         |                 \  -------")
                print("                                         prt fly ae I")
                time.sleep(8)
                mode = "death"
                os.system("clear")

            if question[0:len(question)] == "help":
                os.system("clear")  #clearing shell
                print(colorama.Fore.GREEN+"Rick Roll Time" + colorama.Fore.WHITE)  #printing answer
                webbrowser.open("https://www.youtube.com/watch?v=BjDebmqFRuc")
                questionnumber += 1
            if question[0:len(question)] == "music":
                questionnumber += 1
                musicPlayOrInput = input("Do you want to play music or input music?") # asking if the user wants to play or input music
                if musicPlayOrInput == "play": #if they choose play
                    songChoice = input("Which song do you want to play?") #asking which song they want to play
                    with open(songlist, "r") as Songs: #
                        soings = json.load(Songs)
                        for entry in soings:
                            if songChoice in entry["song"]:
                                webbrowser.open(entry["utubeLink"])
                                for i in range(3):
                                    print("\\")
                                    time.sleep(0.1)
                                    os.system("clear")
                                    print("|")
                                    time.sleep(0.1)
                                    os.system("clear")
                                    print("/")
                                    time.sleep(0.1)
                                    os.system("clear")
                                    print("-")
                                    time.sleep(0.1)
                                    os.system("clear")
                if musicPlayOrInput == "input" or musicPlayOrInput == "give":
                    addedSong = {}
                    addedSong["song"] = input("What song do you want to input?")
                    addedSong["utubeLink"] = input("What is the Youtube link?")
                    if addedSong["utubeLink"][:] == "https://www.youtube.com/watch?v=":
                        with open(songlist, "r") as Songs:
                            temp = json.load(Songs)
                        temp.append(addedSong)
                        with open(songlist, "w") as f:
                            json.dump(temp, f, indent=4)
                    else:
                        print("That is not a valid YouTube link, please dont spam.")

                questionnumber += 1
            if question[:] == "":
                pass

            if questionnumber >= 10:
                os.system("clear")
                print("I don't want to play with you anymore")
                mainloop = False