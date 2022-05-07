############### print table ###############
# def printTable(table):
#     print()
#     row_count = 0
#     for row in table:
#         col_count = 0
#         for element in row:
#             if col_count < 2:
#                 print('',element,'|',end='')
#                 col_count += 1
#             else:
#                 print('',element,end='\n')
#                 if row_count != 2:
#                     print('------------')
#         row_count +=1
#     print()

def printTable(table):
    print()
    row_count = 0
    for row in table:
        col_count = 0
        print('       .       .       ')
        for element in row:
            if col_count < 2:
                print('   '+element+'   .',end='')
                col_count += 1
            else:
                print('   '+element+'   ',end='\n')
        if row_count != 2:
            print('       .       .       ')
            print(' . . . . . . . . . . . ')
        else:
            print('       .       .       ')
        row_count +=1
    print()

############### check for winner ###############
def checkWinner(table):

    table_d = len(table)

    for row in range(table_d):
        winner_flag = True
        for col in range(table_d):
            if table[row][col] != table[row][0]:
                winner_flag = False
        if winner_flag == True:
            return 'winner'
        
        winner_flag = True
        for col in range(table_d):
            if table[col][row] != table[0][row]:
                winner_flag = False
        if winner_flag == True:
            return 'winner'
        
    winner_flag = True
    for row in range(table_d):
        if table[row][row] != table[0][0]:
            winner_flag = False
    if winner_flag == True:
        return 'winner'

    winner_flag = True
    for row in range(table_d):
        wor = len(table)-row-1
        if table[row][wor] != table[0][len(table)-1]:
            winner_flag = False
    if winner_flag == True:
        return 'winner'

    for row in table:
        for element in row: 
            if element in str(list(range(1,10))):
                    return 'continue'

    return 'equal'


############### get input ###############
def getInput(options):
    try:
        inp = input()
        
        if inp not in options: 
            raise Exception
    except Exception:
        print('wrong input enter again:\t')
        inp = getInput(options)
        return inp
    return inp


############### set choice ###############
def setChoice(table,choice,symbol):
    if symbol == 'x':
        symbol = 'X'
    else:
        symbol = 'O'
    dim = len(table)
    for row in range(dim):
        for col in range(dim):
            if table[row][col] == choice:
                table[row][col] = symbol


############### find available elements ###############
def findEvailable(table):
    available_elements = []
    for row in table:
        for element in row:
            if element not in ('x','o'):
                available_elements.append(element)
    return available_elements
    

############### Game Mannager ###############
def gameMannager(table):

    for row in range(len(table)):
        for col in range(len(table)):
            table[row][col] = str(table[row][col])

    player_one = input('player one, please, enter your name:\t')

    print('%s enter your symbol from "x","o" : \t' %player_one ,end='')

    options = ['x','o']
    player_one_symbol = getInput(options)


    player_two = input('player two, please, enter your name:\t')
    
    if player_one_symbol == 'x':
        player_two_symbol = 'o'
    else:
        player_two_symbol = 'x'


    game_status = 'continue'

    printTable(table)

    while game_status == 'continue':

        available_elements = findEvailable(table)

        print('%s enter your choice from table above:\t' %player_one ,end='')

        p1_choice = getInput(available_elements)
        

        setChoice(table,p1_choice,player_one_symbol)
        printTable(table)

        game_status = checkWinner(table)

        if game_status != 'continue':
            if game_status == 'winner':
                print('%s won the game' %player_one)
                return
            else:
                print('equal result')
                return

        available_elements = findEvailable(table)

        print('%s enter your choicefrom table above:\t' %player_two ,end='')

        p2_choice = getInput(available_elements)

        setChoice(table,p2_choice,player_two_symbol)
        printTable(table)

        game_status = checkWinner(table)

        if game_status != 'continue':
            if game_status == 'winner':
                print('%s won the game' %player_two)
                return
            else:
                print('equal result')
                return


############### Main Program ###############
table = [[x for x in range(1,4)],[x for x in range(4,7)],[x for x in range(7,10)]]

gameMannager(table)
