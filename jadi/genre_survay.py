def findMax(dic):
    max = 0
    max_genre = 'zzzz'
    for genre in dic:
        if dic[genre] > max:
            max = dic[genre]
            max_genre = genre 
        elif dic[genre] == max:
            if genre < max_genre:
                max = dic[genre]
                max_genre = genre
    dic.pop(max_genre)
    return max_genre 

interviewee_number = int(input())

result = {
    'Action':0,
    'Comedy':0,
    'History':0,
    'Horror':0,
    'Romance':0,
    'Adventure':0
}

for i in range(interviewee_number):
    inp = str(input())
    respon = inp.split(' ')
    for genre in respon[1:]:
        result[genre] += 1

# print (result)
# interview ={}
# for i in range(interviewee_number):
#     inp = str(input())
#     respon = inp.split(' ')
#     res = respon.pop(0)
#     interview[res] = respon


# for interviewee in interview:
#     vote = interview[interviewee]
#     for genre in vote:
#         result[genre] += 1

temp_result = result.copy()
for i in range(6):
    genre = findMax(temp_result)
    print('%s : %d' %(genre,result[genre]))

