"""
currently, the preformance of the ai's are at:
-"basic" level: undetermined
-"good" level: 1/2 of attempts reach 1024, the rest are below
-"advanced" level:


"""


print("This is the option menu of 2048.")
print("make sure pygame is installed")
print("Choose your game mode from:\n1: classic 2048\n2: classic 2048 with AI move reccomendations\n3: AI plays 2048")
while True:
    ans = input("input: ")
    try:
        ans = int(ans)
        if 4>ans>0:
            break
        print('input is not a valid choice')
    except:
        print('input is not a integer')
    print('try again')
if ans>1:
    print("----------------------------")
    print('you have chosen an option that utilizes AI.\n How advanced to you want the AI to be:')
    print('1 : basic \n2: good \n3: advanced (takes around 7 seconds to make a move)')

while ans>1:
    m = input("input: ")
    try:
        m = int(m)
        if 4>m>0:
            break
        print('input is not a valid choice')
    except:
        print('input is not a integer')
    print('try again')
print("----------------------------")
print("RUNNING")
import gui2048
game = gui2048.GUI2048()
if ans == 1:
    game.run_using_fct(game.get_move_from_input)
from evaluation_function import function as fct
from board_evaluation import function as fct2
#from ai2048 import basic_fct as fct
#from ai2048 import basic_fct2 as fct2
import ai2048 as ai

if ans == 2:                
    game.game.spawn_tile()
    game.game.spawn_tile()
    while True:
        print("reccomended move: ", game.move_dict[ai.find_move(game.game,m,fct,fct2)])
        k = game.get_move_from_input()
        while k == -1:
            game.update_display()
            k = game.get_move_from_input()
        if game.game.move(k):
            game.game.spawn_tile()
        game.update_display()
            
else:
    def computer_move():
        k = ai.find_move(game.game,m,fct,fct2,2-(m//3))
        return k
    game.run_using_fct(computer_move)
        
    

    
    
        
