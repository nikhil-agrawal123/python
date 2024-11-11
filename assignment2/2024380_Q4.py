import random
import requests

words = ['Apple','Beach''Brain','Bread','Brush','Chair','Chest','Chord','Click','Clock','Cloud','Dance','Diary','Drink','Earth','Flute','Fruit','Ghost','Grape','Green','Happy','Heart','House','Juice','Light','Money','Music','Party','Pizza','Plant','Radio','River','Salad','Sheep','Shoes','Smile','Snack','Snake','Spice','Spoon','Storm','Table','Toast','Tiger','Train','Water','Whale','Wheel','Woman','World','Write','Youth']

def check(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

def word_list():
    word = random.choice(words)
    word = word.lower()
    word = list(word)
    return word



word = word_list()
attempts = 6

if attempts == 0:
    print('You have used all your attempts')
else:
    print(f'Welcome to the Guessing Game, You have {attempts} attempts to guess the word')

print(len(word)*'-')  
x = ['-']*5
correct_words = []
while attempts>0:
    guess = input('Guess the word: ')
    if check(guess) == False:
        print('Invalid word')
        continue
    else:
        if guess == ''.join(word):
            print('You guessed it right!')
            break
        else:
            for i in range(5):
                if guess[i] == word[i]:
                    x[i] = guess[i]
                else:
                    if guess[i] in word and guess[i] not in correct_words:
                        correct_words.append(guess[i])
            print(correct_words)
            print(''.join(x))
            print(f'You have {attempts-1} attempts left')
        attempts -= 1

def test():
    assert check('apple') == True
    assert check('appl') == False

test()