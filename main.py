import pygame as pg
import sys
import random

from Grid import Grid

CAPTION = "Gridshit"
SCREEN_SIZE = (1000, 700)
pg.init()

font = pg.font.Font('freesansbold.ttf', 32)
text = font.render("Press C to Shuffle the grid", True, pg.Color("White"))

ccc = bool

def check_hit(grid_group, mouse_pos):

    for grid in grid_group:
        if grid.rect.x + 90 >= mouse_pos[0] and grid.rect.x  <= mouse_pos[0] \
        and grid.rect.y + 70 >= mouse_pos[1] and grid.rect.y <= mouse_pos[1]:

            grid.image.fill(pg.Color("Tomato")) 
            
        else:
            grid.image.fill(pg.Color("cyan")) 



class App(object):

    def __init__(self):
        pg.display.set_caption(CAPTION)
        pg.display.set_mode(SCREEN_SIZE)
        self.screen = pg.display.get_surface()
        self.clock = pg.time.Clock()
        self.fps = 240
        self.grid_group = pg.sprite.Group()
        self.done = False
        self.loop = True
        self.color = [pg.Color("Black"), pg.Color("Azure")]

    def event_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_f:
                    print(pg.mouse.get_pos())
                if event.key == pg.K_ESCAPE:
                   self.done = True 
                if event.key == pg.K_c:   
                    for grid in self.grid_group:
                        grid.rect.x = random.randint(0, 900)
                        grid.rect.x = random.randint(0, 640)

                        pg.display.update()


    def grid(self, num, x, y):
        if self.loop:
            for i in range(num):
                grid = Grid(90, 70, self.color[0])
                grid.rect.y = y
                grid.rect.x += x 
                grid.add(self.grid_group)

        if len(self.grid_group) >= 10:
            self.loop = False
        else:
            self.loop = True    

       
               
                

    def render(self):
        global text
        self.screen.fill(pg.Color("darkblue"))
        self.grid(1, random.randint(0, 900), random.randint(0, 640))
        self.grid_group.draw(self.screen)
        check_hit(self.grid_group, pg.mouse.get_pos())
        self.screen.blit(text, (0,0))
        pg.display.update()


    def main_loop(self):
        while self.done == False:
            self.event_loop()
            self.render()
            self.clock.tick(self.fps)
            

def main():

    App().main_loop()
    pg.quit()
    sys.exit()

if __name__ == "__main__":
    main()