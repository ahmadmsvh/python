participants_number = int(input())

participants = []

for i in range(participants_number):
    participants.append(str(input()).split('.'))

f_participants=[]
m_participants=[]
for i in range(participants_number):
    if participants[i][0] == 'f':
        f_participants.append(participants[i])
    else:
        m_participants.append(participants[i])


for i in range(len(f_participants)):
    f_participants[i][1] = f_participants[i][1].casefold().capitalize()

for i in range(len(m_participants)):
    m_participants[i][1] = m_participants[i][1].casefold().capitalize()

for i in range(len(f_participants)):
    for j in range(i+1,len(f_participants)):
        if f_participants[i][1] > f_participants[j][1]:
            temp = f_participants[i]
            f_participants[i] = f_participants[j]
            f_participants[j] = temp

for i in range(len(m_participants)):
    for j in range(i+1,len(m_participants)):
        if m_participants[i][1] > m_participants[j][1]:
            temp = m_participants[i]
            m_participants[i] = m_participants[j]
            m_participants[j] = temp
    
f_participants.extend(m_participants)

for participant in f_participants:
    print('%s %s %s' %(participant[0],participant[1],participant[2]))