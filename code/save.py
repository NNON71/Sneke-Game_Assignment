import pygame

class Save:
    def __init__(self,name,score):
        self.player_name = name
        self.player_score = score
    
    def write(self):
        with open("data.txt","a") as f:
            print("bB")
            f.write(self.player_name+self.player_score+'\n')
            f.close()

    def find_int(self,text):
        return int(''.join(t for t in text if t.isdigit()))
    
    def sort(self):
        self.new = []
        with open("data.txt","r") as f:
            print("ed")
            self.new = f.read().splitlines()
            f.close()
        
        self.new.sort(key=self.find_int,reverse=True)
        #print(self.new)
        self.replace()

    def replace(self):
        with open("data.txt","w") as f:
            for line in self.new:
                yee = line
                f.write(yee+'\n')
            f.close()