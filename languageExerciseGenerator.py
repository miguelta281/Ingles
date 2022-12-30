from service import add_words, review_vocabulary

def study_vocabulary ():
    print(f'Opciones: 1-> Agregar una nueva palabra, 2 -> repasar' )
    option = input()

    if option == "1":
        add_words()
    elif option == "2":
        review_vocabulary()