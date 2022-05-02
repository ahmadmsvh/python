############### make dictionary ###############

def makeDictionary():
    words_num = int(input())
    dictionary = [input().split(' ') for x in range(words_num)]
    return dictionary
    

############### translate sentence ###############

def translate(sentence,dictionary):
    answer = []
    sentence_words = sentence.split(' ')
    for word in sentence_words:
        word_found = False
        for dictionary_word in dictionary:
            if dictionary_word.count(word) > 0:
                answer.append(dictionary_word[0])
                word_found = True
        if word_found == False:
            answer.append(word)
    sentence = ''
    for word in answer:
        sentence += ' ' + word
    sentence = sentence.strip()
    return sentence



############### Main Program ###############

dictionary = makeDictionary()
sentence = input()
answer = translate(sentence,dictionary)
print(answer)

