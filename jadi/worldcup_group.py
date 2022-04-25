def findMax(dic):
    max_point = 0
    max_team = ''
    max_goal = -100
    for each in dic:
        if dic[each]['points'] > max_point:
            max_point = dic[each]['points']
            max_team = each
            max_goal = dic[each]['goal difference']
        elif dic[each]['points'] == max_point:
            if dic[each]['goal difference'] > max_goal:
                max_point = dic[each]['points']
                max_team = each
                max_goal = dic[each]['goal difference']

            elif dic[each]['goal difference'] == max_goal:
                if str(each) < str(max_team):
                    max_point = dic[each]['points']
                    max_team = each
                    max_goal = dic[each]['goal difference']

        
    dic.pop(max_team)
    return max_team


matches_results = {
    "first": {'Iran': None, 'Spain': None},
    "second": {'Iran': None, 'Portugal': None},
    "third": {'Iran': None, 'Morocco': None},
    "forth": {'Spain': None, 'Portugal': None},
    "fifth": {'Spain': None, 'Morocco': None},
    "sixth": {'Portugal': None, 'Morocco': None}
}

result_table = {
    'Iran' : {'wins':0, 'loses':0, 'draws':0, 'goal difference':0, 'points':0},
    'Spain' : {'wins':0, 'loses':0, 'draws':0, 'goal difference':0, 'points':0},
    'Morocco' : {'wins':0, 'loses':0, 'draws':0, 'goal difference':0, 'points':0},
    'Portugal' : {'wins':0, 'loses':0, 'draws':0, 'goal difference':0, 'points':0}
}

for match in matches_results:
    match_result = str(input())
    i = 0
    for team in matches_results[match]:
        matches_results[match][team] = int(match_result[i])
        i = 2
        

for match in matches_results:
    teams = list(matches_results[match].keys())
    if matches_results[match][teams[0]] > matches_results[match][teams[1]]:
        result_table[teams[0]]['wins'] += 1
        result_table[teams[0]]['goal difference'] += matches_results[match][teams[0]] - matches_results[match][teams[1]]
        result_table[teams[0]]['points'] += 3
        result_table[teams[1]]['loses'] += 1
        result_table[teams[1]]['goal difference'] -= matches_results[match][teams[0]] - matches_results[match][teams[1]]
    elif matches_results[match][teams[0]] == matches_results[match][teams[1]]:
        result_table[teams[0]]['draws'] += 1
        result_table[teams[1]]['draws'] += 1
        result_table[teams[0]]['points'] += 1
        result_table[teams[1]]['points'] += 1
    else :
        result_table[teams[1]]['wins'] += 1
        result_table[teams[1]]['goal difference'] -= matches_results[match][teams[0]] - matches_results[match][teams[1]]
        result_table[teams[1]]['points'] += 3
        result_table[teams[0]]['loses'] += 1
        result_table[teams[0]]['goal difference'] += matches_results[match][teams[0]] - matches_results[match][teams[1]]

result_table_copy = result_table.copy()

for i in range(4):
    each = findMax(result_table_copy)
    p = result_table[each]
    print(each,' wins:%d , loses:%d , draws:%d , goal difference:%d , points:%d' %(p['wins'],p['loses'],p['draws'],p['goal difference'],p['points']))
