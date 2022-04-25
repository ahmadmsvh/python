
message = str(input())

sentences = message.split('.')

words = []
for sentence in sentences:
    sentence = sentence.lstrip()
    word = sentence.split(' ')  
    word[0] = word[0].casefold() 
    words.append(word)


all_words = []
for word in words:
    all_words.extend(word)

counter = 0

result = {}
for word in all_words:
    counter += 1
    if word.istitle():
        for letter in word:
            if letter == ',':
                word = word.replace(',','')
        result[counter] = word        
            


for index in result:
    print('%d:%s' %(index,result[index]))

if len(result) ==0:
    print('None')