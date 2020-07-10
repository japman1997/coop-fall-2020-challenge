class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.index = None
        self.travlist = []
        self.tindex = None
        

    def add(self, num: int):
        self.value +=num
        
        if self.index == None:
            self.index = 0
        elif self.index != self.tindex:
            self.index = self.tindex+1
            del self.travlist[self.index:]
        else:
            self.index+=1
            
        self.travlist.insert(self.index, self.value) 
        
        self.tindex = self.index
        print(self.travlist,self.value,self.index,self.tindex)
        

    def subtract(self, num: int):
        self.value-=num
        
        if self.index == None:
            self.index = 0
        elif self.index != self.tindex:
            self.index = self.tindex+1
            del self.travlist[self.index:]
        else:
            self.index+=1
            
        self.travlist.insert(self.index, self.value) 
        
        self.tindex = self.index
        print(self.travlist,self.value,self.index,self.tindex)

    def undo(self):
        self.tindex = self.tindex-1
        self.value = self.travlist[self.tindex]
        
        print(self.travlist,self.value,self.index,self.tindex)

    def redo(self):
        self.tindex = self.tindex+1
        self.value = self.travlist[self.tindex]
        
        print(self.travlist,self.value,self.index,self.tindex)

    def bulk_undo(self, steps: int):
        if self.tindex+steps<0:
            self.tindex = 0
            print("Out of Range Undo, Undo at First Value")
        else:
            self.tindex = self.tindex-steps
        self.value = self.travlist[self.tindex]
        
        print(self.travlist,self.value,self.index,self.tindex)

    def bulk_redo(self, steps: int):
        if self.tindex+steps>self.index:
            self.tindex = self.index
            print("Out of Range Redo, Redo at MAX")
        else:
            self.tindex = self.tindex+steps
        self.value = self.travlist[self.tindex]
        
        print(self.travlist,self.value,self.index,self.tindex)
    
    def clear(self):
        self.value=0
        if self.index == None:
            self.index = 0
        elif self.index != self.tindex:
            self.index = self.tindex+1
            del self.travlist[self.index:]
        else:
            self.index+=1
            
        self.travlist.insert(self.index, self.value) 
        
        self.tindex = self.index
        print(self.travlist,self.value,self.index,self.tindex)
