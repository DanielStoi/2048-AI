import pygame
import game2048
import ai2048 as ai
from time import sleep
def color_of_tile(a):
    k={'0':(188, 183, 180),'2':(255, 255, 204),'4':(255, 204, 255),'8':(255, 153, 102),'16':(255, 102, 0),'32':(225,75,75),'64':(255, 0, 0),'128':(255, 255, 150),'256':(255,255,100),'512':(255,255,75),'1024':(255,255,75),'2048':(255,255,0)}
    if a in k:
        return k[a]
    else:
        return (0,0,0)
def color_of_text(a):
    if a=='0':
        return (188, 183, 180)
    if int(a)>2048:
        return (255,255,255)
    else:
        return (0,0,0)

class GUI2048():

    def __init__(self):
        self.move_dict = {1:"up",2:"right",3:"down",4:"left"}
        pygame.init() 
        self.game = game2048.Game()
        display_surface = pygame.display.set_mode((400, 400))
        self.display_surface = display_surface
        pygame.display.set_caption('2048')
        
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        
                
        
    def get_move_from_input(self):
        l = pygame.key.get_pressed()[pygame.K_LEFT]
        r = pygame.key.get_pressed()[pygame.K_RIGHT]
        u = pygame.key.get_pressed()[pygame.K_UP]
        d = pygame.key.get_pressed()[pygame.K_DOWN]
        pressed = [u,r,d,l]
        for i in range(4):
            if pressed[i] and not self.delta_press[i]:
                ans = i
                break
        else:
            self.delta_press = pressed
            return -1
        self.delta_press = pressed
        print(ans+1)
        return ans+1
        
        
    def update_display(self):
        
        self.display_surface.fill((167, 172, 145))
        for y in range(4):
            for x in range(4):
                val = str(self.game.board[y][x])
                pygame.draw.rect(self.display_surface,color_of_tile(val),(100*x+10,100*y+10, 80,80))
                text = self.font.render(val, True, color_of_text(val)) 
                # create a rectangular object for the 
                # text surface object 
                textRect = text.get_rect()  
                  
                # set the center of the rectangular object. 
                textRect.center = (100*x+50, 100*y+50)
                self.display_surface.blit(text, textRect)
      
        
        for event in pygame.event.get() : 
      

            if event.type == pygame.QUIT : 
      
                # deactivates the pygame library 
                pygame.quit() 
      
                # quit the program. 
                quit() 
      
            # Draws the surface object to the screen.
        pygame.display.update()

    def run_using_fct(self,fct):
        self.game.spawn_tile()
        self.game.spawn_tile()
        cont = True
        while cont:
            k = fct()
            if k != -1:
                if self.game.move(k):
                    self.game.spawn_tile()
                self.update_display()
            if k == 0:
                print("score: ", ai.score(self.game.board))
                break

if __name__ == '__main__':
    print("RUNNING GUI")
    print(color_of_text('408'))
    g = GUI2048()
    g.run_using_fct(g.get_move_from_input)
