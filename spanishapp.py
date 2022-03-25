import random

def add():
    polish_word = input("Polish word: ")
    spanish_word = input("Spanish word: ")
    with open('dict.txt', 'a') as f:
        f.write(polish_word + "|" + spanish_word + "\n")

def display():
    with open('dict.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            polish, spanish = data.split("|")
            print(polish, "|", spanish)

def learn():
    words_polish = []
    words_spanish = []
    counter = 0
    counter_words = 0

    with open('dict.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            polish, spanish = data.split("|")
            words_polish.append(polish)
            words_spanish.append(spanish)

    words_shuffle = list(zip(words_polish, words_spanish))
    random.shuffle(words_shuffle)

    words_polish, words_spanish = zip(*words_shuffle)
    
    for polish_word in words_polish:
        print(polish_word)
        spanish_word_try = input("Spanish word: ")
        if spanish_word_try == words_spanish[counter_words]:
            print("Nice!" + "\n")
            counter += 1
        elif spanish_word_try != words_spanish[counter_words]:
            counter -= 0.5
        counter_words +=1
    print("You have", counter, "points")
while True:
    mode = input(
        "Type add or display or learn. Type q to quit. ").lower()
    if mode == "q":
        break
    if mode == "add":
        add()
    if mode == "display":
        display()
    if mode == "learn":
        learn()
    else:
        continue
