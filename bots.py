class Bot:
    #r =2, p= 3, s=4
    def __init__(self, rps, r, c):
        self.rps = rps
        self.r = r
        self.c = c
    #return 1 if win, 0 if tie, -1 if lose
    def comp(self, other):
        #self is rock and tie or lose
        if self.rps == 2:
            if other.rps == 2:
                return 0
            elif other.rps == 3:
                return -1
        #self is paper and tie or lose
        if self.rps == 3:
            if other.rps == 3:
                return 0
            elif other.rps == 4:
                return -1
        #self is sci and tie or lose
        if self.rps == 4:
            if other.rps == 4:
                return 0
            elif other.rps == 2:
                return -1
        #self wins
        return 1

    def __str__(self):
        s = str(self.rps) + ', ' + str(self.r) + ', ' +  str(self.c)
        return s
