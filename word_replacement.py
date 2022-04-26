sentence = input("Enter the sentence: ")
print("your current sentence:\n "+sentence)
word_list = sentence.split(' ')

word = input("Enter the word you want to replace: ")


if word in sentence:
    word_to_replace = input(f'which word you want to replace {word } with: ')
    for w in word_list:
        if w == word and word_to_replace != '':
            i = word_list.index(word)
            word_list[i] = word_to_replace
            new_sentence = ' '.join(word_list)
        else:
            print('error')  
    
    print('new sentence:\n', new_sentence)
else:
    print(f'{word} word is not in sentence')


