############### print table ###############
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
            if table[row][col] != table[row][0] or table[row][col] == ' ':
                winner_flag = False
        if winner_flag == True:
            return 'winner'
        
        winner_flag = True
        for col in range(table_d):
            if table[col][row] != table[0][row] or table[col][row] == ' ':
                winner_flag = False
        if winner_flag == True:
            return 'winner'
        
    winner_flag = True
    for row in range(table_d):
        if table[row][row] != table[0][0] or table[row][row] == ' ':
            winner_flag = False
    if winner_flag == True:
        return 'winner'

    winner_flag = True
    for row in range(table_d):
        wor = len(table)-row-1
        if table[row][wor] != table[0][len(table)-1] or table[row][wor] == ' ':
            winner_flag = False
    if winner_flag == True:
        return 'winner'

    for row in table:
        for element in row: 
            if element == ' ':
                    return 'continue'

    return 'equal'


############### get input ###############
def getInput(options):
    
    try:
        inp = input()
        
        if inp == '1':
            inp = [0,0]
        elif inp == '2':
            inp = [0,1]
        elif inp == '3':
            inp = [0,2]
        elif inp == '4':
            inp = [1,0]
        elif inp == '5':
            inp = [1,1]
        elif inp == '6':
            inp = [1,2]
        elif inp == '7':
            inp = [2,0]
        elif inp == '8':
            inp = [2,1]
        elif inp == '9':
            inp = [2,2]
        
        if inp not in options: 
            raise Exception
    except Exception:
        print('wrong input enter again:\t')
        inp = getInput(options)
        return inp
    return inp


############### set choice ###############
def setChoice(table,choice,symbol):
    table[choice[0]][choice[1]] = symbol


############### find available elements ###############
def findEvailable(table):
    available_elements = []
    for row in range(len(table)):
        for col in range(len(table)):
            if table[row][col] == ' ':
                
                available_elements.append([row,col])
    return available_elements
    

############### Game Mannager ###############
def gameMannager(table):

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
table = [[' ' for x in range(1,4)] for x in range(3)]

gameMannager(table)
