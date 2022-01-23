import random

def hangman():
    words = ["pickle","apple","house","car","power","snow","renewal"]
    wrong = 0
    stages = ["",
    "________________       ",
    "|                      ",
    "|              |       ",
    "|              0       ",
    "|             /|\      ",
    "|             / \      ",
    "|                      ",
    "|                      "
    ]
    print(str(len(words)))
    rand_end = len(words)
    rand_word = words[random.randrange(rand_end)]
    print (rand_word)
    remaining_letters = list(rand_word)
    board = ["_"] * len(rand_word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in remaining_letters:
            cind = remaining_letters.index(char)
            board[cind] = char
            remaining_letters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose! It was {}.".format(rand_word))

hangman()
