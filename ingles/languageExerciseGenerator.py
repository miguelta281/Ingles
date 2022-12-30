from ingles.service import  add_words, review_vocabulary

def study_vocabulary (file_path):
    print(f'Opciones: 1-> Agregar una nueva palabra, 2 -> repasar' )
    option = input()

    if option == "1":
        add_words(file_path)
    elif option == "2":
        review_vocabulary(file_path)