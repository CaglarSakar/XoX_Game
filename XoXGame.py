import random
import time
class Game():
    def __init__(self, *args, **kwargs):
        self.createTable()
        self.playername = ["Player 1","Player 2"]
        self.currentplayer = 0
        
    def play(self):
        print("""
Welcome to XoX game. Please select game mod:
1- Player vs PC
2- Player vs Player""")
        while True:
            try:
                self.mode = int(input("Mode:"))
            except ValueError:
                print("Please select valid mode:")
                continue
            
            if self.mode == 1 or self.mode == 2:
                break
            elif self.mode == 0:
                break
            else:
                print("Please select valid mode:")
        print("")
        self.show()
        if self.mode == 2:
            self.PvP()
        elif self.mode == 1:
            self.PvC()

    def createTable(self):
        self.table =[]
        for i in range(9):
            self.table.append(" ")
    
    def show(self):
        print("-------------")
        for i,grid in enumerate(self.table):
            print(f"| {grid} " , end="")
            if i % 3 == 2:
                print("|")
                print("-------------")
    
    def put(self,i,**kwargs):
        if "player" in kwargs.keys():
            player = kwargs["player"]
        else:
            player = self.currentplayer
        
        if "table" in kwargs.keys():
            table = kwargs["table"]
        else:
            table = self.table
        table[i] = "X" if player == 1 else "O"
            
    def selection(self,**kwargs):
        if "player" in kwargs.keys():
            player = kwargs["player"]
        else:
            player = self.currentplayer
        while True:
            try:
                grid = int(input(f"{self.playername[player-1]}, select grid:"))
            except ValueError:
                print("Please select valid grid:")
                continue
            
            if (grid >= 1 and grid <= 9):
                if self.table[grid-1] == " ":
                    return grid
                else:
                    print("Your selected grid is not empty")
            elif grid == 0:
                return False
            else:
                print("Please select valid grid:")
    
    def checkGame(self,**kwargs):
        if "table" in kwargs.keys():
            table = kwargs["table"]
        else:
            table = self.table

        if self.checkColumn(table = table) or self.checkCross(table = table) or self.checkLine(table = table):
            return True
        else:
            return False
    
    def checkLine(self,**kwargs):        
        if "table" in kwargs.keys():
            table = kwargs["table"]
        else:
            table = self.table

        for i in [0,3,6]:
            if table[i] == table[i+1] and table[i] == table[i+2] and table[i] != " ":
                return True
        return False

    def checkColumn(self,**kwargs): 
        if "table" in kwargs.keys():
            table = kwargs["table"]
        else:
            table = self.table

        for i in [0,1,2]:
            if table[i] == table[i+3] and table[i] == table[i+6] and table[i] != " ":
                return True
        return False
    
    def checkCross(self,**kwargs):        
        if "table" in kwargs.keys():
            table = kwargs["table"]
        else:
            table = self.table

        if table[0] == table[4] and table[0] == table[8] and table[4] != " ":
            return True
        elif table[2] == table[4] and table[2] == table[6] and table[4] != " ":
            return True
        else:
            return False
        
    def selectWhich(self):
        while True:
            try:
                player = int(input("Which player do you want to play as:"))
            except ValueError:
                print("Please select valid player:")
                continue
            
            if player == 1 or player == 2:
                self.playername[player%2]="PC"
                return player
            elif player == 0:
                return False
            else:
                print("Please select valid player:")

    def PCSelection(self):
        ihtimal = []
        for i in range(9):
            simulatetable = self.table.copy()
            if simulatetable[i] == " ":
                self.put(i,player =self.currentplayer ,table=simulatetable)
                if self.checkGame(table=simulatetable):
                    return i+1

        for i in range(9):
            simulatetable = self.table.copy()
            if simulatetable[i] == " ":
                self.put(i,player = (self.currentplayer%2)+1 ,table=simulatetable)
                if self.checkGame(table=simulatetable):
                    return i+1

        for i in range(9):
            simulatetable = self.table.copy()
            if simulatetable[i] == " ":
                self.put(i,player =self.currentplayer ,table=simulatetable)
                for j in range(9):
                    simulatetable2=simulatetable.copy()
                    if simulatetable2[j] == " ":
                        self.put(j,player =self.currentplayer ,table=simulatetable2)
                        if self.checkGame(table=simulatetable2):
                            return i+1
                ihtimal.append(i)
        return random.choice(ihtimal)+1       

    def PvP(self):
        for i in range(1,10):
            print("")
            print(f"Turn{i}")
            self.currentplayer = 1 if i%2 == 1 else 2
            selection = self.selection()
            if not selection:
                break
            self.put(selection-1)
            self.show()
            if self.checkGame():
                print(f"{self.playername[self.currentplayer-1]} won!")
                break
            if i == 9:
                print ("Draw!")

    def PvC(self):
        player = self.selectWhich()
        for i in range(1,10):
            print("")
            print(f"Turn{i}")
            self.currentplayer = 1 if i%2 == 1 else 2
            if self.currentplayer == player:
                selection = self.selection()
                if not selection:
                    break
            else:
                selection = self.PCSelection()
                time.sleep(0.8)
                print(f"{self.playername[self.currentplayer-1]} select grid:{selection}")            
            self.put(selection-1)
            self.show()
            if self.checkGame():
                print("")
                print(f"{self.playername[self.currentplayer-1]} won!")
                break
            if i == 9:
                print ("Draw!")

if __name__ == "__main__":
    game = Game()
    game.play()

