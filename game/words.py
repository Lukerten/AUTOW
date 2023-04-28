def generate_answer_list ():
    word_list = open("game/data/answers.txt","r")
    data = word_list.read()
    word_array = data.replace('\n', ' ').split(" ")
    word_array = [element.upper() for element in word_array]
    word_list.close()
    return word_array

def generate_word_list ():
    word_list = open("game/data/words.txt", "r")
    data = word_list.read()
    word_array = data.replace('\n', ' ').split(" ")
    word_array = [element.upper() for element in word_array]
    word_list.close()
    return word_array

# Call the function

generate_word_list()