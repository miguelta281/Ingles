import json
import numpy as np


def add_words():
    
    while True:

        print('Ingrese una nueva palabra')
        word = input('Ingrese la palabra en Español ')
        if word == "2145":
            break
        translate = input('Ingrese la palabra en Ingles ')

        

        with open('vocabulary.json', 'r+') as file:
            data = json.load(file)
            data[word] = translate
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()


def extract_word():
    with open('vocabulary.json') as file:
        data = json.load(file)

    keys = list(data.keys())
    index = np.random.randint(0, len(keys))

    return (keys[index], data[keys[index]])

def review_vocabulary():

    while True:
        spanish_word, english_word = extract_word()
        print(f'¿Cuál es la traducción de: {spanish_word} ?')

        translate = input()
        if translate == '2145':
            break

        if translate == english_word:
            print('Correcto!')
        else:
            print(f'La forma correcta es: {english_word}')