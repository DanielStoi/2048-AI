from random import randint

ODDS_OF_SPAWNING_4 = 10 #1/x is the prob of spawning 4 tile 

class Game:
    board : list

    def __init__(self):
        self.board = []
        for i in range(4):
            self.board.append([0]*4)
            
    def move_right(self, board):
        t=False
        for line in board:
            #print("********")
            i=3
            while i>0:
                #print(line)
                #print("-----")
                if line[i]==0:
                    if line[:i]==[0]*(i):
                        break
                    line[0:i+1]=[0]+line[0:i]
                    t=True
                else:
                    #print(str(line[i])+"encountered")
                    
                    k=i-1
                    #print(k)
                    while(line[k]!=line[i]):
                        #print("k iter")
                        if k <= 0 or line[k] != 0:
                            #print("k false")
                            break
                        k-=1
                        
                    else:
                        #print("two equal numbs encountered"+str(k))
                        line[i]*=2
                        line[k]=0
                        t=True
                    i-=1
        return t

    def rotate(self,board, a):
        a=a%4
        if a==0:
            return board
        b = [[],[],[],[]]
        for k in range(4):
            for w in range(4):
                b[k].append(board[w][k])

        for i in range(4):
            b[i]=b[i][::-1]
            
        self.board = b
        return self.rotate(b,a-1)

        
    def move(self, a: int):
        board = self.board
        board = self.rotate(board,a)
        if a%2 == 0:
            board = self.rotate(board,2)
                    
        t= self.move_right(board)

        board = self.rotate(board,-a)
        if a%2 == 0:
            board = self.rotate(board,2)
        
        return t
            
        
        

    def spawn_tile(self, pos = -1, val = -1, type2 = False) -> bool:
        if pos == -1 or type2: # choose random location
            
            c=0
            for line in self.board:
                for i in range(4):
                    if line[i]== 0:
                        if type2 and pos==c:
                            line[i]=val
                            return True
                        c+=1
            if c == 0:
                
                return False
            c = randint(0,c-1)
            for line in self.board:
                for i in range(4):
                    if line[i] == 0:
                        c-=1
                        if c == -1:
                            line[i] = int(randint(0,ODDS_OF_SPAWNING_4)//ODDS_OF_SPAWNING_4)*2+2
                            return True
            print("ERROOOOOOOOOOOOOOOREROROROR")


        # choose a specific tile to spawn
        if self.board[pos//4][pos%4] != 0:
            return False
        if val == -1:
            self.board[pos//4][pos%4] = randint(0,1)*2+2
        else:
            self.board[pos//4][pos%4] = val
        return True



    def pb(self):
        print("-------")
        for i in self.board:
            print(" ".join(map(str,i)))
        
              
    def run_textbased(self):
        print("you are playing the text version of 2024")
        print("---")
        print("write 1,2,3,4 to shift tiles up,right,down,left")
        c=True
        self.spawn_tile()
        self.spawn_tile()
        while c:
            self.pb()
            print("---")
            try:
                move = int(input("your move: "))
            except:
                print("---INVALID INPUT---")
                continue
            if 4 < move or move < 1:
                print("---INVALID INPUT---")
                continue
            if self.move(move):
                if not self.spawn_tile():
                    print("---GAME OVER---")
                    break

if __name__ == '__main__':
    print("THIS MODULE IS NOT MEANT TO BE RUN, UNLESS FOR TESTING.")
    print("RUN \"run2048.py\" TO PLAY AND ai2048 FOR THE AI TO PLAY")
    game = Game()
    game.spawn_tile(4,2)
    
    
