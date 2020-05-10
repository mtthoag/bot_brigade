class Bot:
    #player 1 r =2, p=3, s=4
    #player 2 r = 12, p = 13, s = 14
    def __init__(self, rps, r, c, board):
        self.rps = rps
        self.r = r
        self.c = c
        self.board = board
        self.alive = True
    
    def destroy(self):
        self.board[self.r][self.c] = 1
        self.alive = False

    #return 1 if win, 0 if tie, -1 if lose
    def comp(self, other):
        if self.rps > 4:
            rps1 = self.rps - 10
        else:
            rps1 = self.rps
        if other.rps > 4:
            rps2 = other.rps - 10
        else:
            rps2 = other.rps
        #self is rock and tie or lose
        if rps1 == 2:
            if rps2 == 2:
                self.destroy()
                other.destroy()
                return
            elif rps2 == 3:
                self.destroy()
                return
        #self is paper and tie or lose
        if rps1 == 3:
            if rps2 == 3:
                self.destroy()
                other.destroy()
                return
            elif rps2 == 4:
                self.destroy()
                return
        #self is sci and tie or lose
        if rps1 == 4:
            if rps2 == 4:
                self.destroy()
                other.destroy()
                return
            elif rps2 == 2:
                self.destroy()
                return
        #self wins
        other.destroy()

    def __str__(self):
        s = str(self.rps) + ', ' + str(self.r) + ', ' +  str(self.c)
        return s
