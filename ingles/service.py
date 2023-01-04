import json
import numpy as np


def add_words(file_path):
    
    while True:

        print('Ingrese una nueva palabra')
        word = input('Ingrese la palabra en Español ')
        if word == "2145":
            break
        translate = input('Ingrese la palabra en Ingles ')

        

        with open(file_path, 'r+') as file:
            data = json.load(file)
            data[word] = translate
            file.seek(0)
            json.dump(data, file, indent=4)
            file.truncate()


def extract_word(file_path):
    with open(file_path) as file:
        data = json.load(file)

    keys = list(data.keys())
    index = np.random.randint(0, len(keys))

    return (keys[index], data[keys[index]])

def review_vocabulary(file_path):

    total = 0
    correct = 0
    while True:
        spanish_word, english_word = extract_word(file_path)
        print(f'¿Cuál es la traducción de: {spanish_word} ?')

        translate = input()
        if translate == '2145':
            print(f'{correct} de {total}')
            break

        if translate == english_word:
            correct += 1
            print('Correcto!')
        else:
            print(f'La forma correcta es: {english_word}')
        
        total += 1