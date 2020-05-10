from tkinter import *
import tkinter.font as font
from bots import *
import random

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
global master
master = Tk()

global p1s
p1s = 0
global p2s
p2s=0

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
global r_mode 
r_mode = False


global board
board = [[1 for n in range(8)] for i in range(8)]

img = [ PhotoImage(file=str(i)+ ".png").subsample(2,2) for i in range(9)]
for i in range(9,12):
    img.append(0)
for i in range(12,15):
    img.append(PhotoImage(file=str(i)+ ".png").subsample(2,2))

#Making the board
labels = [[Label(master, image = img[1]) for c in range(8)] for r in range(10)]

for c in range(8):
    r = 0
    labels[r][c].destroy()
    r = 9
    labels[r][c].destroy()
for r in range(1,8):
    for c in range(8):
        labels[r][c].grid(row = r, column = c)
for r in range(1,8):
    c = 0
    labels[r][c]['image'] = img[8]
    c = 7
    labels[r][c]['image'] = img[8]
        

labels[4][0]['image'] = img[0]
labels[4][7]['image'] = img[0]
labels[9][0] = Label(master, image = img[5])
labels[9][0].grid(row = 9, column = 0, pady=10)

labels[9][5] = Label(master, image = img[5])
labels[9][5].grid(row = 9, column = 5, pady=10)

labels[9][1] = Label(master, image = img[3])
labels[9][1].grid(row = 9, column = 1, pady=10)

labels[9][6] = Label(master, image = img[3])
labels[9][6].grid(row = 9, column = 6, pady=10)

labels[9][2] = Label(master, image = img[4])
labels[9][2].grid(row = 9, column = 2, pady=10)

labels[9][7] = Label(master, image = img[4])
labels[9][7].grid(row = 9, column = 7, pady=10)

labels[9][3] = Label(master, text=p1s)
labels[9][3].grid(row=9, column=3, pady=10)
labels[9][4] = Label(master, text=p2s)
labels[9][4].grid(row=9, column=4, pady=10)


#player 1 movement
def rps_a(event):
    global p1_rps
    x = p1_rps - 5
    x = (x-1) % 3
    #switch betweent r, p, s selection first line highlights the new pic, second line unhighlights the old one
    if x == 0:
        labels[9][x]['image'] = img[5]
        labels[9][x+1]['image'] = img[3]
    elif x == 1:
        labels[9][x]['image'] = img[6]
        labels[9][x+1]['image'] = img[4]
    else:
        labels[9][x]['image'] = img[7]
        labels[9][x-2]['image'] = img[2]
    p1_rps = x+5

def rps_d(event):
    global p1_rps
    x = p1_rps - 5
    x = (x+1) % 3
    #switch betweent r, p, s selection first line highlights the new pic, second line unhighlights the old one
    if x == 0:
        labels[9][x]['image'] = img[5]
        labels[9][x+2]['image'] = img[4]
    elif x == 1:
        labels[9][x]['image'] = img[6]
        labels[9][x-1]['image'] = img[2]
    else:
        labels[9][x]['image'] = img[7]
        labels[9][x-1]['image'] = img[3]
    p1_rps = x+5

def row_w(event):
    global p1_row
    x = (p1_row - 1) % 8
    if x == 0:
        x =7
    labels[x][0]['image'] = img[0]
    labels[p1_row][0]['image'] = img[8]
    p1_row = x

def row_s(event):
    global p1_row
    x = (p1_row + 1) % 8
    if x == 0:
        x=1
    labels[x][0]['image'] = img[0]
    labels[p1_row][0]['image'] = img[8]
    p1_row = x

def rps_t(event):
    global p1_rps
    global p1_row
    global p1_bots
    global board
    if board[p1_row][1] > 1:
        return
    rps = p1_rps-3
    b = Bot(rps, p1_row, 1, board)
    board[p1_row][1] = rps
    p1_bots.append(b)
    labels[p1_row][1]['image'] = img[rps]


#player 2 movement
def rps_left(event):
    global p2_rps
    x = p2_rps - 5
    x = (x-1) % 3
    #switch betweent r, p, s selection first line highlights the new pic, second line unhighlights the old one
    if x == 0:
        labels[9][x+5]['image'] = img[5]
        labels[9][x+5+1]['image'] = img[3]
    elif x == 1:
        labels[9][x+5]['image'] = img[6]
        labels[9][x+5+1]['image'] = img[4]
    else:
        labels[9][x+5]['image'] = img[7]
        labels[9][x+5-2]['image'] = img[2]

    p2_rps = x+5

def rps_right(event):
    global p2_rps
    x = p2_rps - 5
    x = (x+1) % 3
    #switch betweent r, p, s selection first line highlights the new pic, second line unhighlights the old one
    if x == 0:
        labels[9][x+5]['image'] = img[5]
        labels[9][x+5+2]['image'] = img[4]
    elif x == 1:
        labels[9][x+5]['image'] = img[6]
        labels[9][x+5-1]['image'] = img[2]
    else:
        labels[9][x+5]['image'] = img[7]
        labels[9][x+5-1]['image'] = img[3]

    p2_rps = x+5

def row_up(event):
    global p2_row
    x = (p2_row - 1) % 8
    if x == 0:
        x = 7
    labels[x][7]['image'] = img[0]
    labels[p2_row][7]['image'] = img[8]
    p2_row = x

def row_down(event):
    global p2_row
    x = (p2_row + 1) % 8
    if x == 0:
        x = 1
    labels[x][7]['image'] = img[0]
    labels[p2_row][7]['image'] = img[8]
    p2_row = x

def rps_enter(event):
    global p2_rps
    global p2_row
    global p2_bots
    global board
    if board[p2_row][6] > 1:
        return
    rps = p2_rps-3+10
    b = Bot(rps, p2_row, 6, board)
    board[p2_row][6] = rps
    p2_bots.append(b)
    labels[p2_row][6]['image'] = img[rps] 

myfont = font.Font(size = 8)
global rand
rand = Button(master, text="Random")
rand.grid(row=0, column=4)
rand['font'] = myfont

global select
select = Button(master, text="Select")

def random_mode(event):
    global r_mode
    r_mode = True
    rand.grid_forget()
    select.grid(row=0, column=4)
def select_mode(event):
    global r_mode
    r_mode = False
    select.grid_forget()
    rand.grid(row=0, column=4)

rand.bind('<Button-1>', random_mode)
select.bind('<Button-1>', select_mode)

def play_again():
    global rematch
    global message
    rematch.grid_forget()
    message.grid_forget()
    global p2_bots
    global p1_bots
    global p1_row
    global p2_row
    global p1_rps
    global p2_rps

    for r in range(1,8):
        for c in range(1,7):
            board[r][c] = 1
            labels[r][c]['image'] = img[1]
    p1_bots = []
    p2_bots = []
    p1_row = 4
    p2_row = 4
    p1_rps = 5
    p2_rps = 5
    for r in range(1,8):
        for c in range(8):
            if c == 0 or c == 7:
                labels[r][c]['image'] = img[8]
    labels[4][0]['image'] = img[0]
    labels[4][7]['image'] = img[0]
    labels[9][0]['image'] = img[5]
    labels[9][5]['image'] = img[5]
    labels[9][1]['image'] = img[3]
    labels[9][6]['image'] = img[3]
    labels[9][2]['image'] = img[4]
    labels[9][7]['image'] = img[4]
    update()

global rematch
rematch = Button(master, text="rematch", command=play_again)
rematch['font'] = myfont
rematch.grid_forget()
global message
message = Label(master, text="")
message.grid_forget()



def update():
    global p1s
    global p2s
    global rematch
    global message
    global p1_rps
    global p2_rps
    finish = True
    if r_mode:
        x = random.randint(5,7)    
        y = random.randint(5,7)    
        master.unbind('<Left>')
        master.unbind('<Right>')
        master.unbind('a')
        master.unbind('d')
        labels[9][p1_rps-5]['image'] = img[p1_rps-5+2]
        labels[9][p2_rps]['image'] = img[p2_rps-5+2]
        p1_rps = x
        p2_rps = y
        labels[9][p1_rps-5]['image'] = img[p1_rps]
        labels[9][p2_rps]['image'] = img[p2_rps]
    else:
        master.bind('<Left>', rps_left)
        master.bind('<Right>', rps_right)
        master.bind('a', rps_a)
        master.bind('d', rps_d)
    for b in p1_bots:
        r = b.r
        c = b.c
        if b.alive and board[r][c] == b.rps:
           # print(board, b.rps,'\n') 
            if c == 6:
                finish = False
                message['text'] = "P1 wins!"
                rematch.grid(row=0, column= 2)
                message.grid(row=0, column=0)
                
                p1s += 1
                labels[9][3]['text'] = p1s
                return
            rps = board[r][c+1]
            
            if rps > 1:
                bb = Bot(rps, r, c+1, board)
                b.comp(bb)
            else:
                b.c = c+1
                board[r][c] = 1
                board[r][c+1] = b.rps
        

    for b in p2_bots:
        r = b.r
        c = b.c
        if board[r][c] == b.rps and b.alive:
           # print(board, b.rps, '\n')
            if c == 1:
                finish = False   
                p2s += 1
                message['text'] = "P2 wins!"
                rematch.grid(row=0, column= 2)
                message.grid(row=0, column=0)
                labels[9][4]['text'] = p2s
                return
            
            rps = board[r][c-1]
            if rps > 1:
                bb = Bot(rps, r, c-1, board)
                b.comp(bb)
            else:
                board[r][c] = 1
                board[r][c-1] = b.rps
                b.c = c-1

        else:
            b.alive = False
       
    
    for r in range(1,8):
        for c in range(1,7):
            labels[r][c]['image'] = img[board[r][c]]
    
    
    if finish:
        master.after(1000, update)
           
    
            
def destroy():
    master.destroy()

def restart():
    global p1s
    global p2s
    p1s = 0
    p2s = 0
    play_again()

Button(master, text='Exit',command=destroy).grid(row= 0, column = 7)
Button(master, text="Restart", command=restart).grid(row=0, column= 6)


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
