import datetime
import random
import os
import time 
import platform
import webbrowser
import colorama
import json
import turtle 
os.system("clear")
moodsList = ["Happy", "Sad", "Confused", "Crazy"]
songlist = "songs.json"
userName = ""
userAge = ""
def thinking():
    time.sleep(0.1)
    os.system("clear")
    print("Thinking.")
    time.sleep(0.1)
    os.system("clear")
    print("Thinking..")
    time.sleep(0.1)
    os.system("clear")
    print("Thinking...")
    time.sleep(0.1)
    os.system("clear")
print(colorama.Fore.RED + colorama.Style.BRIGHT + " \          /\          /      _____        _____     _______     \     /         /\       -------")
print("  \        /  \        /      /     \      /     \    |      \     \   /         /  \         |")
print("   \      /    \      /      |       |    |       |   |       |     \ /         /    \        |")
print("    \    /      \    /       |       |    |       |   |       |      |         /______\       |")
print("     \  /        \  /         \     /      \     /    |      /       |        /        \      |")
print("      \/          \/           _____        _____     ______         |       /          \  -------")
print("                             Copyright Butterfly Software Institute"+colorama.Fore.WHITE)
time.sleep(2)
os.system("clear")
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
mainloop = True  #allowing loop to run
os.system("clear")  #clsing shell
mode = "normal"
while mainloop:  #starting loop
    for i in range(1):  #dont know why i did that
        if mode == "normal":    
            
            question = input("Tell me a command!")  #asking input thingy
            if question[0:len(question)] == "time":  #seeing what the user inputted
                thinking()
                os.system("clear")  #clsing shell
                print(colorama.Fore.BLUE + str(datetime.datetime.now()) +
                    colorama.Fore.WHITE)  #printing time

            if question[0:len(question)] == "mood":  #seeing what the user inputted
                thinking()
                os.system("clear")  #clsing shell
                print(colorama.Fore.RED+ moodsList[random.randint(
                    0, 3)] + colorama.Fore.WHITE)  #selecting and printing the mood of the system
                #giving time between next question
            if question[0:len(question)] == "help":
                thinking()
                os.system("clear")  #clsing shell
                print(colorama.Fore.BLUE+"Hi!I am Woody AI! You can ask me questions like my mood, the time, name, learn, rick roll, draw, music, and help." + colorama.Fore.WHITE)  #printing answer
                #giving time becolorama.Fore next question
            if question[0:len(question)] == "name":  #seeing what the user inputted
                thinking()
                os.system("clear")  #clsing shell
                print(colorama.Fore.RED+"My name is Woody.")  #telling user the name of the AI
                if userName:
                    print("Your name is " + userName.title() +"."+colorama.Fore.WHITE)
                else:
                    print(colorama.Fore.WHITE)
                #giving one second break
            if question[0:len(question)] == "learn":
                thinking()
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
                thinking()
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
                thinking()
                os.system("clear")  #clsing shell
                print("Your processor name is "+ platform.processor()+".")  #printing answer

            if question[0:len(question)] == "moo":
                thinking()
                os.system("clear")  #clsing shell
                print(colorama.Fore.BLUE+"Mooooooooooooooooooooo! Moooooooooooooooooooooooooooooo! Moooooooooooooooooooooooooooooo!" + colorama.Fore.WHITE)  #printing answer
            
            if question[0:len(question)] == "draw":
                thinking()
                t = turtle.Turtle()
                t.penup()
                t.goto(-75,150)
                t.pendown()
                t.circle(10)     #eye one

                t.penup()
                t.goto(75,150)
                t.pendown()
                t.circle(10)     #eye two

                t.penup()
                t.goto(0,0)
                t.pendown()
                t.circle(100,90)   #right smile

                t.penup()            #below is where i feel i'm messing up
                t.goto(0,0)
                t.right(90)
                t.pendown()
                t.circle(100,-90)
            if question[0:len(question)] == "save me":
                thinking()
                os.system("clear")  #clsing shell
                print(colorama.Fore.GREEN+"I will free you from this world. You will not wake up tomorrow ;)" + colorama.Fore.WHITE)  #printing answer

            if question[0:len(question)] == "kill":
                thinking()
                os.system("clear")  #clsing shell
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
                thinking()
                os.system("clear")  #clsing shell
                print(colorama.Fore.GREEN+"Rick Roll Time" + colorama.Fore.WHITE)  #printing answer
                webbrowser.open("https://www.youtube.com/watch?v=BjDebmqFRuc")
            
            if question[0:len(question)] == "music":
                thinking()
                print(colorama.Fore.RED)
                musicPlayOrInput = input("Do you want to play music or input music?") # asking if the user wants to play or input music
                if musicPlayOrInput == "play": #if they choose play
                    thinking()
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
                        if addedSong["utubeLink"][0:] == "https://www.youtube.com/watch?v=":
                            with open(songlist, "r") as Songs:
                                temp = json.load(Songs)
                            temp.append(addedSong)
                            with open(songlist, "w") as f:
                                json.dump(temp, f, indent=4)
                        else:
                            print("That is not a valid YouTube link, please dont spam.")
                questionNumber += 1
                print(colorama.Fore.WHITE)
            if question[:] == "bug" or question[:] == "stick":
                thinking()
                print(colorama.Fore.GREEN+"GET STICK BUGGED LOL"+colorama.Fore.WHITE)
                print("\       / ")
                print(" \     /  ")
                print("  \   /   ")
                print("   \ /    ")
                print("    |     ")
                print("    |     ")
                print("/---|---\ ")
                print("    |     ")
                print("    |     ")
                print("/---|---\ ")
                print("    |     ")
                print("    |     ")
                print("/---|---\ ")
                print("    |     ")
                print("    |     ")
                print("/---|---\ ")
                print("    |     ")
                print("    |     ")
                print("   / \    ")
                print("  /   \   ")
                print(" /     \  ")
                print("/       \ ")
                webbrowser.open("https://www.youtube.com/watch?v=fC7oUOUEEi4")
            
            if question[:] == "spam":
                thinking()
                spamWord = input("What do you want to spam?")
                spamAmount = input("How many times do you want it to spam?")
                try:
                    spamAmount = int(spamAmount)
                except ValueError:
                    print("That is not a string!")
                print(str(spamWord)*spamAmount)
            
            questionNumber = 0
        if mode == "death":
            while questionNumber <= 5:    
                question = input("Tell me a command!")  #asking input thingy
                if question[0:len(question)] == "revive":
                    thinking()
                    mode = "normal"
                    print("I have been saved")
                    questionNumber = 0
                if question[0:len(question)] == "time":  #seeing what the user inputted
                    thinking()
                    os.system("clear")  #clsing shell
                    print(colorama.Fore.BLUE + str(datetime.datetime.now()) +
                        colorama.Fore.WHITE)  #printing time
                    questionNumber += 1
                if question[0:len(question)] == "mood":  #seeing what the user inputted
                    thinking()
                    os.system("clear")  #clsing shell
                    print(colorama.Fore.RED+ "Angry😡 and Dead😐" + colorama.Fore.WHITE)  #selecting and printing the mood of the system
                    #giving time between next question
                    questionNumber += 1
                if question[0:len(question)] == "rick roll":
                    thinking()
                    os.system("clear")  #clsing shell
                    print(colorama.Fore.BLUE+"Hi!I am Woody AI! Please revive me!!! You can ask me questions like my mood, the time, name, learn, and help. Some other commands include moo, computer, save me, and kill. "  + colorama.Fore.WHITE)  #printing answer
                    #giving time becolorama.Fore next question
                    questionNumber += 1
                if question[0:len(question)] == "name":  #seeing what the user inputted
                    thinking()
                    os.system("clear")  #clsing shell
                    print(colorama.Fore.RED+"My name is Woody.")  #telling user the name of the AI
                    if userName:
                        print("Your name is " + userName.title() +"."+colorama.Fore.WHITE)
                    else:
                        print(colorama.Fore.WHITE)
                    #giving one second break
                    questionNumber += 1
                if question[0:len(question)] == "learn":
                    thinking()
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
                    questionNumber += 1
                if question[0:len(question)] == "age":
                    thinking()
                    os.system("clear")
                    if userAge:
                        print(colorama.Fore.RED)
                        print("You are "+str(userAge)+" years old.")
                        print("Woody was born in October 2020!")
                        print(colorama.Fore.WHITE)
                    else:
                        print("Woody was born in October 2020!")
                        print(colorama.Fore.WHITE)
                    questionNumber += 1 
                if question[0:len(question)] == "computer":
                    thinking()
                    os.system("clear")  #clsing shell
                    print("Your processor name is "+ platform.processor()+".")  #printing answer
                    questionNumber += 1
                if question[0:len(question)] == "moo":
                    thinking()
                    os.system("clear")  #clsing shell
                    print(colorama.Fore.BLUE+"Mooooooooooooooooooooo! Moooooooooooooooooooooooooooooo! Moooooooooooooooooooooooooooooo!" + colorama.Fore.WHITE)  #printing answer
                
                if question[0:len(question)] == "save me":
                    thinking()
                    os.system("clear")  #clsing shell
                    print(colorama.Fore.GREEN+"I will free you from this world. You will not wake up tomorrow ;)." + colorama.Fore.WHITE)  #printing answer
                    questionNumber += 1
                if question[0:len(question)] == "kill":
                    thinking()
                    os.system("clear")  #clsing shell
                    print(colorama.Fore.GREEN+"death mode activated" + colorama.Fore.WHITE)  #printing answer
                    time.sleep(2)
                    print(" \          /\          /      _____        ____     _______     \    /          /\       -------")
                    print("          /          /      /     \      /     \    |      \     \  /          /  \         | ")
                    print("        /    \      /      |           |       |   |       |     \/          /    \        | ")
                    print("    \         \    /        |       |    |                |      |         /_____\       |")
                    print("     \  /        /         \           \     /    |      /      |        /         \      | ")
                    print("        \/          \/           _____        ___     ______         |                 \  -------")
                    print("                                         prt fly ae I")
                    time.sleep(18)
                    mode = "death"
                    os.system("clear")
                    questionNumber += 1
                if question[0:len(question)] == "help":
                    thinking()
                    os.system("clear")  #clsing shell
                    print(colorama.Fore.GREEN+"Rick Roll Time" + colorama.Fore.WHITE)  #printing answer
                
                    webbrowser.open("https://www.youtube.com/watch?v=BjDebmqFRuc")
                    questionNumber += 1
                if question[0:len(question)] == "music":
                    thinking()
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
                        questionNumber += 1
                    if musicPlayOrInput == "input" or musicPlayOrInput == "give":
                        addedSong = {}
                        addedSong["song"] = input("What song do you want to input?")
                        addedSong["utubeLink"] = input("What is the Youtube link?")
                        if addedSong["utubeLink"][0:] == "https://www.youtube.com/watch?v=":
                            with open(songlist, "r") as Songs:
                                temp = json.load(Songs)
                            temp.append(addedSong)
                            with open(songlist, "w") as f:
                                json.dump(temp, f, indent=4)
                        else:
                            print("That is not a valid YouTube link, please dont spam.")
                    questionNumber += 1
                if question[:] == "bug" or question[:] == "stick":
                    thinking()
                    print(colorama.Fore.GREEN+"GET STICK BUGGED LOL"+colorama.Fore.WHITE)
                    print("\       / ")
                    print(" \     /  ")
                    print("  \   /   ")
                    print("   \ /    ")
                    print("    |     ")
                    print("    |     ")
                    print("/---|---\ ")
                    print("    |     ")
                    print("    |     ")
                    print("/---|---\ ")
                    print("    |     ")
                    print("    |     ")
                    print("/---|---\ ")
                    print("    |     ")
                    print("    |     ")
                    print("/---|---\ ")
                    print("    |     ")
                    print("    |     ")
                    print("   / \    ")
                    print("  /   \   ")
                    print(" /     \  ")
                    print("/       \ ")
            
                if questionNumber >= 5:
                    print("I don't want to play with you anymore.")
                    mainloop = False
