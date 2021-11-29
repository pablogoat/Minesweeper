import pygame
import random

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Minesweeper")

val = []

icon = pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\bomb.png")
cursor = pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\target.png")
gameover = pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\game-over.png")
winner = pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\winner.png")
square = pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\square.png")
squarev = pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\squarev.png")
square0 = pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\square0.png")
val.append(pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\1.png"))
val.append(pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\2.png"))
val.append(pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\3.png"))
val.append(pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\4.png"))
val.append(pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\5.png"))
val.append(pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\6.png"))
val.append(pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\7.png"))
val.append(pygame.image.load(r"D:\dziwne_rzeczy\VScode\Minesweeperpy\8.png"))

pygame.display.set_icon(icon)
pygame.mouse.set_visible(False)

run = True
over = False

class cell:
    def __init__(self,imag):
        self.rev = False
        self.value = 0
        self.paint = imag

    def set_image(self,imag):
        self.paint = imag

def reveal(x, y):

    if not cells[x][y].rev:
        if cells[x][y].value > 8:
            return True
        elif not cells[x][y].value == 0:
            cells[x][y].rev = True
            cells[x][y].set_image(val[cells[x][y].value-1])
            return False
        else:
            cells[x][y].rev = True
            cells[x][y].set_image(square0)
            for i in range(x-1,x+2,1):
                for j in range(y-1,y+2,1):
                    if (i >= 0 and i <= 14 and j >= 0 and j <= 14):
                        reveal(i,j)
            return False
    else:
        return False
        
cells = [[cell(square) for x in range(15)] for i in range(15)]

bob = 0
over = False
lol = 0

while bob < 25:
    a = random.randint(0,14)
    b = random.randint(0,14)

    if cells[a][b].value < 9:
        cells[a][b].value += 9
        for i in range(a-1, a+2, 1):
            for j in range(b-1, b+2, 1):
                if i >= 0 and i <= 14 and j >= 0 and j <= 14:
                    cells[i][j].value += 1
        bob += 1


while run:
    screen.fill((192,192,192))
    ccoord = pygame.mouse.get_pos()

    space = 0

    for i in range(15):
        for j in range(15):
            screen.blit(cells[i][j].paint,(i*32+10,j*32+10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if over:
                pass
            else:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                over = reveal(int((x-(x%32))/32), int((y-(y%32))/32))
    
    for i in range(15):
        for j in range(15):
            if(not cells[i][j].rev):
                space +=1

    if over or space == 25:
        lol = 3

    while lol:
        if space == 25:
            screen.fill((0,255,0))
            screen.blit(winner,(125,125))
        else:
            screen.fill((255,0,0))
            screen.blit(gameover,(125,125))
        lol -= 1


    screen.blit(cursor,(ccoord[0]-10,ccoord[1]-10))

    pygame.display.update()