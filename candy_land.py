import random
import numpy as np
from copy import deepcopy
import matplotlib.pyplot as plt 
'''
    Color cards:
        Single color:
            green: 6
            red: 6
            purple: 5
            orange: 6
            yellow: 6
            blue: 6
        Double colors:
            green: 3
            red: 4
            purple: 4
            orange: 3
            yellow: 4
            blue: 4
    Special Cards:
        Popsicle (red)
        Lollipop (purple)
        Chocolate (brown)
        Gingerbread man
        Ice Cream
        Cupcake
        Gummy Star
    Map: 
        RPYBOGRP(Cupcake)YBOGRPYBOG(Ice Cream)RPYBOGRPYBOGRPYBOGRPY(Gummy Star)BOGRPYBOGRPYBOGRPYBOGRPYBO(Gingerbread)
           |                                          |           |              |              |
           1                                          2           3              4              5 
        GRPYBOGRPYBOGRPYBOGRPY(Lollipop)BOGRPYBOG(Popsicle)RPYBOGRPYBOGRP(Chocolate)BOGRPYBOGRPYBOG(Rainbow)
              |
              6
    Special passes:
        Peppermint pass: 1---> 5
        Gummy pass 2---> 3
    Licorice:
        Positions: 4 (index = 44), 6 (index = 75)
    Players:
        Red, Yellow, Green, Blue pawns
'''
## STEP 1: Record all cards
colors = ['green', 'red', 'purple', 'orange', 'yellow', 'blue']
num_cards_single_color = [6, 6, 5, 6, 6, 6]
num_cards_double_colors = [3, 4, 4, 3, 4, 4]
single_color_cards = [color + '_x1' for color, num_card in zip(colors, num_cards_single_color) for i in range(num_card)]
double_color_cards = [color + '_x2' for color, num_card in zip(colors, num_cards_double_colors) for i in range(num_card)] 
special_cards = ['cupcake', 'ice_cream', 'gummy_star','gingerbread', 'lollipop', 'popsicle', 'chocolate']
all_cards = single_color_cards + double_color_cards + special_cards

## STEP 2: Construct the map
map_string = 'RPYBOGRP YBOGRPYBOG RPYBOGRPYBOGRPYBOGRPY BOGRPYBOGRPYBOGRPYBOGRPYBO GRPYBOGRPYBOGRPYBOGRPY BOGRPYBOG RPYBOGRPYBOGRP BOGRPYBOGRPYBOG'
map_list = []
special_cards_dict = dict() 
color_map = {'R': 'red', 'P': 'purple', 'Y': 'yellow', 'B': 'blue', 'O': 'orange', 'G': 'green'}
special_card_pointer = 0
for index, s in enumerate(map_string):
    if s != ' ':
        map_list.append(color_map[s])
    else:
        special_card = special_cards[special_card_pointer]
        map_list.append(special_card)
        special_cards_dict[special_card] = (index, special_card)
        special_card_pointer += 1
map_list.append('goal')

INDEX_GOAL = 132 
LICORICE_INDEXES = [44, 75]
# Peppermint pass 3, blue --> 59, yellow
# Gummy pass 28, yellow --> 40, yellow 

def a_single_move(card_drawn, current_pos):
    # current_pos e.g (0, 'red')
    cur_index, cur_color = current_pos
    if cur_index == INDEX_GOAL:
        return (INDEX_GOAL, 'win')
    map_list_right = deepcopy(map_list[cur_index + 1:])
    if card_drawn in special_cards_dict:
        return special_cards_dict[card_drawn]
    else:
        color, num_colors = card_drawn.split('_')
        num_colors = int(num_colors[-1])    
        if num_colors == 1:
            if color not in map_list_right:
                return (INDEX_GOAL, 'win')
            for i, c in enumerate(map_list_right):
                if c == color:
                    if cur_index + i + 1  == 3: # peppermint pass 
                        return (59, 'yellow')
                    elif cur_index + i + 1 == 28: # gummy pass 
                        return (40, 'yellow')
                    return (cur_index + i + 1, c)
        else:
            if map_list_right.count(color) < num_colors:
                return (INDEX_GOAL, 'win')
            count_colors = num_colors - 1
            for i, c in enumerate(map_list_right):
                if c == color:
                    if count_colors:
                        count_colors -= 1
                        continue 
                    else:
                        if cur_index + i + 1  == 3: # peppermint pass
                            return (59, 'yellow')
                        elif cur_index + i + 1 == 28: # gummy pass 
                            return (40, 'yellow')
                        return (cur_index + i + 1, c)

'''
    To do: implement licorice
'''
def play_game(game_cards):
    # consider three players for now
    results = [None, None, None]
    player_1_pos, player_2_pos, player_3_pos = (-1, None),  (-1, None),  (-1, None)

    while game_cards:
        # first player 1 move
        player_1_pos = a_single_move(game_cards.pop(), player_1_pos)
        if player_1_pos[0] in LICORICE_INDEXES:
            player_2_pos = a_single_move(game_cards.pop(), player_2_pos)
            if player_2_pos[1] == 'win':
                results[1] = 1
                while game_cards:
                    player_1_pos = a_single_move(game_cards.pop(), player_1_pos)
                    if player_1_pos[1] == 'win':
                        results[0] = 2
                        results[2] = 3
                        return results
                    player_3_pos = a_single_move(game_cards.pop(), player_3_pos)
                    if player_3_pos[1] == 'win':
                        results[0] = 3
                        results[2] = 2
                        return results  

            player_3_pos = a_single_move(game_cards.pop(), player_3_pos)
            if player_3_pos[1] == 'win':
                results[2] = 1
                while game_cards:
                    player_1_pos = a_single_move(game_cards.pop(), player_1_pos)
                    if player_1_pos[1] == 'win':
                        results[0] = 2
                        results[1] = 3
                        return results
                    player_2_pos = a_single_move(game_cards.pop(), player_2_pos)
                    if player_2_pos[1] == 'win':
                        results[0] = 3
                        results[1] = 2
                        return results 

        if player_1_pos[1] == 'win':
            results[0] = 1
            while game_cards:
                player_2_pos = a_single_move(game_cards.pop(), player_2_pos)
                if player_2_pos[1] == 'win':
                    results[1] = 2
                    results[2] = 3
                    return results
                player_3_pos = a_single_move(game_cards.pop(), player_3_pos)
                if player_3_pos[1] == 'win':
                    results[1] = 3
                    results[2] = 2
                    return results

        # next player 2 move
        player_2_pos = a_single_move(game_cards.pop(), player_2_pos)
        if player_2_pos[0] in LICORICE_INDEXES:
            player_3_pos = a_single_move(game_cards.pop(), player_3_pos)
            if player_3_pos[1] == 'win':
                results[2] = 1
                while game_cards:
                    player_1_pos = a_single_move(game_cards.pop(), player_1_pos)
                    if player_1_pos[1] == 'win':
                        results[0] = 2
                        results[1] = 3
                        return results
                    player_2_pos = a_single_move(game_cards.pop(), player_2_pos)
                    if player_2_pos[1] == 'win':
                        results[0] = 3
                        results[1] = 2
                        return results 

            player_1_pos = a_single_move(game_cards.pop(), player_1_pos)
            if player_1_pos[1] == 'win':
                results[0] = 1
                while game_cards:
                    player_2_pos = a_single_move(game_cards.pop(), player_2_pos)
                    if player_2_pos[1] == 'win':
                        results[1] = 2
                        results[2] = 3
                        return results
                    player_3_pos = a_single_move(game_cards.pop(), player_3_pos)
                    if player_3_pos[1] == 'win':
                        results[1] = 3
                        results[2] = 2
                        return results 

        if player_2_pos[1] == 'win':
            results[1] = 1
            while game_cards:
                player_1_pos = a_single_move(game_cards.pop(), player_1_pos)
                if player_1_pos[1] == 'win':
                    results[0] = 2
                    results[2] = 3
                    return results
                player_3_pos = a_single_move(game_cards.pop(), player_3_pos)
                if player_3_pos[1] == 'win':
                    results[0] = 3
                    results[2] = 2
                    return results  

        # finally player 3 move  
        player_3_pos = a_single_move(game_cards.pop(), player_3_pos)
        if player_3_pos[0] in LICORICE_INDEXES:
            player_1_pos = a_single_move(game_cards.pop(), player_1_pos)
            if player_1_pos[1] == 'win':
                results[0] = 1
                while game_cards:
                    player_2_pos = a_single_move(game_cards.pop(), player_2_pos)
                    if player_2_pos[1] == 'win':
                        results[1] = 2
                        results[2] = 3
                        return results
                    player_3_pos = a_single_move(game_cards.pop(), player_3_pos)
                    if player_3_pos[1] == 'win':
                        results[1] = 3
                        results[2] = 2
                        return results 

            player_2_pos = a_single_move(game_cards.pop(), player_2_pos)
            if player_2_pos[1] == 'win':
                results[1] = 1
                while game_cards:
                    player_1_pos = a_single_move(game_cards.pop(), player_1_pos)
                    if player_1_pos[1] == 'win':
                        results[0] = 2
                        results[2] = 3
                        return results
                    player_3_pos = a_single_move(game_cards.pop(), player_3_pos)
                    if player_3_pos[1] == 'win':
                        results[0] = 3
                        results[2] = 2
                        return results 

        if player_3_pos[1] == 'win':
            results[2] = 1
            while game_cards:
                player_1_pos = a_single_move(game_cards.pop(), player_1_pos)
                if player_1_pos[1] == 'win':
                    results[0] = 2
                    results[1] = 3
                    return results
                player_2_pos = a_single_move(game_cards.pop(), player_2_pos)
                if player_2_pos[1] == 'win':
                    results[0] = 3
                    results[1] = 2
                    return results 

def play_multiple_games(num_games_played, game_cards):
    count_player_1_wins, count_player_2_wins, count_player_3_wins = 0, 0, 0
    for i in range(num_games_played):
        cur_deck_1 = deepcopy(game_cards)
        random.shuffle(cur_deck_1)
        cur_deck_2 = deepcopy(game_cards)
        random.shuffle(cur_deck_2)
        cur_deck_3 = deepcopy(game_cards)
        random.shuffle(cur_deck_3)

        cur_cards = cur_deck_1 + cur_deck_2 + cur_deck_3
        
        results = play_game(cur_cards)
        if results[0] == 1:
            count_player_1_wins += 1
        elif results[1] == 1:
            count_player_2_wins += 1
        else:
            count_player_3_wins += 1
    return [count_player_1_wins / num_games_played, 
            count_player_2_wins / num_games_played,
            count_player_3_wins / num_games_played]


num_games = [1, 2, 3, 4, 5, 6] # 10**4
player_1_win_pct = []
player_2_win_pct = []
player_3_win_pct = []
for num_game in num_games:
    p1_win, p2_win, p3_win = play_multiple_games(10**num_game, all_cards)
    player_1_win_pct.append(p1_win)
    player_2_win_pct.append(p2_win)
    player_3_win_pct.append(p3_win)

player_1_win_pct = np.array(player_1_win_pct)
player_2_win_pct = np.array(player_2_win_pct)
player_3_win_pct = np.array(player_3_win_pct)

width = 0.5
fig, ax = plt.subplots(figsize = (10, 8))
ax.hlines(y=[1./3, 2./3], xmin=-0.1, xmax=len(num_games) + width, colors='black', linestyles='--', lw=1)
ax.bar(num_games, player_3_win_pct, width, label='Player_3_win_probability')
ax.bar(num_games, player_2_win_pct, width, bottom = player_3_win_pct,  label='Player_2_win_probability')
ax.bar(num_games, player_1_win_pct, width, bottom = player_3_win_pct + player_2_win_pct, label='Player_1_win_probability')
ax.set_ylabel('Winning Probability', fontsize = 20)
ax.set_title('Candy Land - Chance of winning for three players', fontsize = 20)
ax.set_xlabel('number of games played, at exponential form of 10', fontsize = 20)
ax.legend()
plt.tight_layout()
plt.savefig('simulation_results.png', dpi = 900)



    



