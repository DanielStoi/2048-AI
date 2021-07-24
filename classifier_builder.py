from ai2048 import e_effective_link as link,e_power_corner as corner,e_power_corner_stability as stab,score,entrapment
#link,entrapment, conrner,stab,score, 
from game2048 import Game
import ai2048 as ai
from board_evaluation import function as fct2

class classifier:
    weights = []
    def __init__(self, scale):
        
        self.weights = scale
        if len(scale) < 10:
            print("WARNING: too little inputs in classifier")

    def function(self, subtree):
        board = subtree.cur.board
        ans = 0
        for y in range(4):
            for x in range(4):
                coord = [x,y]
                ans+=self.weights[0]*link(board,coord)
                ans-=self.weights[1]*entrapment(board,coord)
                ans+=self.weights[2]*score(board)
                ans+=self.weights[3]*stab(board,coord)
                ans+=self.weights[4]*corner(board)
                ans+=self.weights[5]*stab(board,coord)**2
                ans+=self.weights[6]*link(board,coord)**2
                ans+=self.weights[7]*entrapment(board,coord)**2
                ans+=self.weights[8]*score(board)**2
                ans+=self.weights[9]*corner(board)**2
        
        return int(ans)

    def set(self, scale):
        scale = self



def evaluate_effectivness(n,fct): #runs 2024 game and saves score, n times
    ans = 0
    for _ in range(n):
        game = Game()
        game.spawn_tile()
        game.spawn_tile()
        cont = True
        while cont:
            k = ai.find_move(game,3,fct,fct2,1)
            if k != -1:
                if game.move(k):
                    game.spawn_tile()      
            if k == 0:
                ans+= ai.score(game.board)
                break
    return ans/n

def evaluate_expected_time():
    a = int(input("what is the expected amount of itterations you want to train the classifier: "))
    b = int(input("how much iterations of the the game should be run for each classifier to be evaluated: "))
    print("expected time is "+str(a*b)+" minutes, or "+str(a*b//60)+" hours.")


if __name__ == '__main__':
    evaluate_expected_time()
