def rsp_game_winner(arr):
    strategies = ['R', 'P', 'S']
    strategy1 = arr[0][1]
    strategy2 = arr[1][1]
    if len(arr) != 2:
        raise Exception('WrongNumberOfPlayers')
    if strategy1 not in strategies or strategy2 not in strategies:
        raise Exception('NoSuchStrategyError')
    if strategy1 == 'P':
        if strategy2 in ['P', 'R']:
            return arr[0]
        return arr[1]
    elif strategy1 == 'R':
        if strategy2 in ['S', 'R']:
            return arr[0]
        return arr[1]
    else:
        if strategy2 in ['P', 'S']:
            return arr[0]
        return arr[1]


#print(*rsp_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
#print(*rsp_game_winner([['player1', 'P'], ['player2', 'A']]))
print(*rsp_game_winner([['player1', 'P'], ['player2', 'S']]))
print(*rsp_game_winner([['player1', 'P'], ['player2', 'P']]))
