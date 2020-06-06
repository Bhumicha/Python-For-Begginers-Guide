import random


def welcome():
    '''This function creates a welcome page for our gaming application.'''
    for i in range(0, 20):
        print("*\t", end="")
    print()
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 8):
        print("\t", end="")
    print("WELCOME", end="")
    for i in range(0, 10):
        print("\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*")
    print("*", end="")
    for i in range(0, 19):
        print("\t", end="")
    print("*")
    for i in range(0, 20):
        print("*\t", end="")
    print()
    input("Press any key to start:")


def mainmenu():
    print("1.Rock Paper Scissors\n2.Cows and Bulls\n3.Exit")
    ch = int(input("Enter your choice number:"))
    if ch == 1:
        rockpaperscissorsmenu()
    elif ch == 2:
        cowsandbullsmenu()
    elif ch == 3:
        exit()
    else:
        print("Invalid choice!")
        mainmenu()


def rockpaperscissorsmenu():
    print("1.Play\n2.Rules\n3.Return to Main menu")
    ch = int(input("Enter your choice number:"))
    if ch == 1:
        rockpaperscissors()
    elif ch == 2:
        rockpaperscissorsrules()
    elif ch == 3:
        mainmenu()
    else:
        print("Invalid choice!")
        rockpaperscissorsmenu()


def cowsandbullsmenu():
    print("1.Play\n2.Rules\n3.Return to Main menu")
    ch = int(input("Enter your choice number:"))
    if ch == 1:
        cowsandbulls()
    elif ch == 2:
        cowsandbullsrules()
    elif ch == 3:
        mainmenu()
    else:
        print("Invalid choice!")
        cowsandbullsmenu()


def rockpaperscissors():
    print("WELCOME TO ROCK PAPER AND SCISSORS")
    print(
        "You will be competing against the computer. The player that scores 5 points first, will be declared as the winner!")
    print("If your choice is Rock,please Enter 0")
    print("If your choice is Paper,please Enter 1")
    print("If your choice is Scissors,please Enter 2")
    print("If you wish to exit,please Enter -1")
    user = 0
    comp = 0
    cnt = 0
    chc = ["Rock", "Paper", "Scissors"]
    while (user < 5 and comp < 5 and cnt < 25):
        cnt += 1
        u_ch = int(input("Enter your choice:"))
        if u_ch == -1:
            print("Thank you")
            return
        c_ch = random.choice([0, 1, 2])
        if u_ch == 0 and c_ch == 1:
            comp += 1
        elif u_ch == 0 and c_ch == 2:
            user += 1
        elif u_ch == 1 and c_ch == 0:
            user += 1
        elif u_ch == 1 and c_ch == 2:
            comp += 1
        elif u_ch == 2 and c_ch == 0:
            comp += 1
        elif u_ch == 2 and c_ch == 1:
            user += 1
        print("You:", chc[u_ch])
        print("Computer", chc[c_ch])
        print("Your score:", user, "\t Computer's Score:", comp)
    if (user > comp):
        print("Congragulations!You win!")
    elif (comp > user):
        print("Oops!Sorry you lose. Better luck next time!")
    else:
        print("Match Draw")
    mainmenu()


def cowsandbulls():
    words = ["rate", "fail", "cake", "sore", "tear", "calm", "rage", "time", "face", "swan"]
    rand = random.randrange(0, 10)
    word = words[rand]
    cnt = 0
    while (cnt < 15):
        s = input("Enter string:")
        if s == "-1":
            print("Thank you!")
            return
        cows = 0
        bulls = 0
        # time mite
        chars = 0
        for c in s:
            if c in word:
                chars += 1  # chars=4
        for i in range(0, 4):
            if s[i] == word[i]:
                bulls += 1  # bulls=2
        cows = chars - bulls
        print("Cows:", cows, "\tBulls:", bulls)
        if bulls == 4:
            print("Congragulations!You win!")
            mainmenu()
        cnt += 1
    print("Oops!Maximum guess limit reached!")
    mainmenu()


welcome()
print("\n" * 100)
mainmenu()
