def replace_word():

    str = "Hey guys! Lets go on an adventure sometime guys"
    word_to_replace = input("Enter the word to be replaced: ")
    word_replacement = input("Enter the word to replace: ")
    print(str.replace(word_to_replace, word_replacement))
    
replace_word()