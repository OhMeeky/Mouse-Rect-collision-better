import pygame as pg
import sys
import random

from Grid import Grid

CAPTION = "Gridshit"
SCREEN_SIZE = (1000, 700)
pg.init()

font = font = pg.font.SysFont('timesnewroman', 20)
c_comm = font.render("Press C to Shuffle the grid", True, pg.Color("White"))
l_comm = font.render("Press Left to empty the grid", True, pg.Color("White"))
r_comm = font.render("Press Right to add a square", True, pg.Color("White"))

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
        self.sq_count = 7


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
                if event.key == pg.K_LEFT:
                    self.remove_sq()             
                if event.key == pg.K_RIGHT:
                    self.add_sq(random.randint(0, 900), random.randint(0, 640))



    def add_sq(self, x, y):
        print("Square Added")
        grid = Grid(90, 70, self.color[0])
        grid.rect.y = y
        grid.rect.x = x 
        grid.add(self.grid_group)


    def remove_sq(self):
        for i in self.grid_group:
            self.grid_group.remove(i)


    def grid(self, num, x, y):
        if self.loop:
            for i in range(num):
                grid = Grid(90, 70, self.color[0])
                grid.rect.y = y
                grid.rect.x = x 
                grid.add(self.grid_group)

        if len(self.grid_group) >= self.sq_count:
            self.loop = False
        else:
            self.loop = True    

    


    def render(self):
        global c_comm
        global l_comm
        global r_comm
        self.screen.fill(pg.Color("darkblue"))
        self.grid(1, random.randint(0, 900), random.randint(0, 640))
        self.grid_group.draw(self.screen)
        check_hit(self.grid_group, pg.mouse.get_pos())
        self.screen.blit(c_comm, (0,0))
        self.screen.blit(l_comm, (0,25))
        self.screen.blit(r_comm, (0,50))

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