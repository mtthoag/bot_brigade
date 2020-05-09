from tkinter import *
from bots import *

"""
0 is the selected dropping cell
1 is the basic cell
2 is a rock
3 is a paper
4 scissor
5 is selected rock
6 is selected papper
7 is selected scissor   
8 is a blank square
"""
global finish
finish = True

global p1_rps 
p1_rps = 5
global p1_row
p1_row = 4
global p1_bots
p1_bots = []

global p2_row
p2_row = 4
global p2_rps
p2_rps = 5
global p2_bots
p2_bots = []

global board
board = [[1 for n in range(8)] for i in range(8)]
master = Tk()
img = [ PhotoImage(file=str(i)+ ".png").subsample(2,2) for i in range(9)]

#player 1 movement
def rps_a(event):
    global p1_rps
    x = p1_rps - 5
    x = (x-1) % 3
    #switch betweent r, p, s selection first line highlights the new pic, second line unhighlights the old one
    if x == 0:
        Label(master, image = img[5]).grid(row = 9, column = x, pady=10)
        Label(master, image = img[3]).grid(row = 9, column = x+1, pady=10)
    elif x == 1:
        Label(master, image = img[6]).grid(row = 9, column = x, pady=10)
        Label(master, image = img[4]).grid(row = 9, column = x+1, pady=10)
    else:
        Label(master, image = img[7]).grid(row = 9, column = x, pady=10)
        Label(master, image = img[2]).grid(row = 9, column = x-2, pady=10)

    p1_rps = x+5

def rps_d(event):
    global p1_rps
    x = p1_rps - 5
    x = (x+1) % 3
    #switch betweent r, p, s selection first line highlights the new pic, second line unhighlights the old one
    if x == 0:
        Label(master, image = img[5]).grid(row = 9, column = x, pady=10)
        Label(master, image = img[4]).grid(row = 9, column = x+2, pady=10)
    elif x == 1:
        Label(master, image = img[6]).grid(row = 9, column = x, pady=10)
        Label(master, image = img[2]).grid(row = 9, column = x-1, pady=10)
    else:
        Label(master, image = img[7]).grid(row = 9, column = x, pady=10)
        Label(master, image = img[3]).grid(row = 9, column = x-1, pady=10)

    p1_rps = x+5

def row_w(event):
    global p1_row
    x = (p1_row - 1) % 8
    Label(master, image = img[0]).grid(row = x, column = 0)
    Label(master, image = img[8]).grid(row = p1_row, column = 0)
    p1_row = x

def row_s(event):
    global p1_row
    x = (p1_row + 1) % 8
    Label(master, image = img[0]).grid(row = x, column = 0)
    Label(master, image = img[8]).grid(row = p1_row, column = 0)
    p1_row = x

def rps_t(event):
    global p1_rps
    global p1_row
    global p1_bots
    global board
    if board[p1_row][1] > 1:
        return
    rps = p1_rps-3
    b = Bot(rps, p1_row, 1)
    board[p1_row][1] = rps
    p1_bots.append(b)
    Label(master, image = img[rps]).grid(row =p1_row, column = 1)

#player 2 movement
def rps_left(event):
    global p2_rps
    x = p2_rps - 5
    x = (x-1) % 3
    #switch betweent r, p, s selection first line highlights the new pic, second line unhighlights the old one
    if x == 0:
        Label(master, image = img[5]).grid(row = 9, column = x+5, pady=10)
        Label(master, image = img[3]).grid(row = 9, column = x+5+1, pady=10)
    elif x == 1:
        Label(master, image = img[6]).grid(row = 9, column = x+5, pady=10)
        Label(master, image = img[4]).grid(row = 9, column = x+5+1, pady=10)
    else:
        Label(master, image = img[7]).grid(row = 9, column = x+5, pady=10)
        Label(master, image = img[2]).grid(row = 9, column = x+5-2, pady=10)

    p2_rps = x+5

def rps_right(event):
    global p2_rps
    x = p2_rps - 5
    x = (x+1) % 3
    #switch betweent r, p, s selection first line highlights the new pic, second line unhighlights the old one
    if x == 0:
        Label(master, image = img[5]).grid(row = 9, column = x+5, pady=10)
        Label(master, image = img[4]).grid(row = 9, column = x+5+2, pady=10)
    elif x == 1:
        Label(master, image = img[6]).grid(row = 9, column = x+5, pady=10)
        Label(master, image = img[2]).grid(row = 9, column = x+5-1, pady=10)
    else:
        Label(master, image = img[7]).grid(row = 9, column = x+5, pady=10)
        Label(master, image = img[3]).grid(row = 9, column = x+5-1, pady=10)

    p2_rps = x+5

def row_up(event):
    global p2_row
    x = (p2_row - 1) % 8
    Label(master, image = img[0]).grid(row = x, column = 7)
    Label(master, image = img[8]).grid(row = p2_row, column = 7)
    p2_row = x

def row_down(event):
    global p2_row
    x = (p2_row + 1) % 8
    Label(master, image = img[0]).grid(row = x, column = 7)
    Label(master, image = img[8]).grid(row = p2_row, column = 7)
    p2_row = x

def rps_enter(event):
    global p2_rps
    global p2_row
    global p2_bots
    global board
    if board[p2_row][1] > 1:
        return
    rps = p2_rps-3
    b = Bot(rps, p2_row, 6)
    board[p2_row][6] = rps
    p2_bots.append(b)
    Label(master, image = img[rps]).grid(row =p2_row, column = 6)
    
def update():
    p1_death = []
    p2_death = []
    p1w = False
    p2w = False
    global finish

    for b in p1_bots:
        r = b.r
        c = b.c
        if c == 6:
            p1w = True
            finish = False
        board[r][c] = 1
        rps = board[r][c+1]
        
        if rps > 1:
            bb = Bot(rps, r, c+1)
            x = b.comp(bb)
            if x == 1:
                board[r][c+1] = b.rps
                b.c = c+1
                p2_death.append(bb)
            elif x == 0:
                board[r][c+1] = 1
                p1_death.append(b)
                p2_death.append(bb)
            else:
                p1_death.append(b)
        else:
            b.c = c+1
            board[r][c+1] = b.rps
    
    for b in p1_death:    
        p1_bots.remove(b)
    p1_death = []
    for b in p2_death:
        x = 0
        while x ==0:
            i = 0
            if p2_bots[i].r == b.r and p2_bots[i].c == b.c:
                p2_bots.pop(i)
                x = 1
            i += 1
    p2_death = []
    for b in p2_bots:
        r = b.r
        c = b.c
        if c == 1:
            finish = False
        board[r][c] = 1
        rps = board[r][c-1]
        if rps == 1:
            board[r][c-1] = b.rps
            b.c = c-1
        else:
            bb = Bot(rps, r, c-1)
            x = b.comp(bb)
            if x == 1:
                board[r][c-1] = b.rps
                b.c = c-1
                p1_death.append(bb)
            elif x == 0:
                board[r][c-1] = 1
                p2_death.append(b)
                p1_death.append(bb)
            else:
                p2_death.append(b)


    for b in p2_death:    
        p2_bots.remove(b)
    for b in p1_death:
        x = 0
        while x ==0:
            i = 0
            if p1_bots[i].r == b.r and p1_bots[i].c == b.c:
                p1_bots.pop(i)
                x = 1
            i += 1
       
    
    for r in range(1,8):
        for c in range(1,7):
            Label(master, image = img[board[r][c]]).grid(row=r,column=c)
    if finish:
        master.after(1000, update)
           
    else:
        #master._grid_configure()
        master.destroy()
        works = Tk()
        if p1w:
            Label(works, text="Player 1 wins!").grid(row=0)
        else:
            Label(works, text="Player 2 wins!").grid(row=0)
   
       

    


  
#making the board
for r in range(1,8):
    for c in range(8):
        if c == 0 or c == 7:
            Label(master, image = img[8]).grid(row = r, column = c)
        else:
            Label(master, image = img[1]).grid(row = r, column = c)

Label(master, image = img[0]).grid(row = 4, column = 0)
Label(master, image = img[0]).grid(row = 4, column = 7)
Label(master, image = img[5]).grid(row = 9, column = 0, pady=10)
Label(master, image = img[5]).grid(row = 9, column = 5, pady=10)
Label(master, image = img[3]).grid(row = 9, column = 1, pady=10)
Label(master, image = img[3]).grid(row = 9, column = 6, pady=10)
Label(master, image = img[4]).grid(row = 9, column = 2, pady=10)
Label(master, image = img[4]).grid(row = 9, column = 7, pady=10)


master.bind('<Up>', row_up)
master.bind('<Down>', row_down)
master.bind('<Left>', rps_left)
master.bind('<Right>', rps_right)
master.bind('<Return>', rps_enter)

master.bind('w', row_w)
master.bind('s', row_s)
master.bind('a', rps_a)
master.bind('d', rps_d)
master.bind('t', rps_t)


        
master.after(1000, update)
master.mainloop()
