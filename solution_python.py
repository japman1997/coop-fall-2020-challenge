class EventSourcer():
    # Do not change the signature of any functions

    def __init__(self):
        self.value = 0
        self.index = 0
        self.travlist = [0]
        self.tindex = 0
        self.check = False
        self.dict1 = []
        self.dc = 0
        

    def add(self, num: int):
        self.value +=num
        
        # if self.index == None:
        #     self.index = 0
        if self.index != self.tindex:
            self.index = self.tindex+1
            del self.travlist[self.index:]
        else:
            self.index+=1
            
        self.travlist.insert(self.index, self.value) 
        
        self.tindex = self.index
        self.dict1.append(num)
        self.dc+=1
        print(self.travlist,self.value,self.index,self.tindex,self.dict1)
        

    def subtract(self, num: int):
        self.value-=num
        
        # if self.index == None:
        #     self.index = 0
        if self.index != self.tindex:
            self.index = self.tindex+1
            del self.travlist[self.index:]
        else:
            self.index+=1
            
        self.travlist.insert(self.index, self.value) 
        
        self.tindex = self.index
        self.dict1.append(-num)
        self.dc+=1
        print(self.travlist,self.value,self.index,self.tindex,self.dict1)

    def undo(self):
        if self.index > 0:
            if self.tindex-1<0:
                self.tindex = 0
                print("Out of Range Undo, Undo at First Value")
            else:
                self.tindex = self.tindex-1     
            self.value = self.travlist[self.tindex]
            self.check=True
            
            self.dc+=1
            print(self.travlist,self.value,self.index,self.tindex)

    def redo(self):
        if self.index > 0:
            if self.check == True:
                if self.tindex+1>self.index:
                    self.tindex = self.index
                    self.value +=self.dict1[self.tindex-1]
                    self.travlist.append(self.value)
                    self.index=len(self.travlist)-1
                else:
                    self.tindex = self.tindex+1
                    self.value = self.travlist[self.tindex]
                
            self.dc+=1
            print(self.travlist,self.value,self.index,self.tindex)
            
            if self.tindex == self.index:
                self.check = False

    def bulk_undo(self, steps: int):
        if self.index >0:
            if self.tindex-steps<0:
                self.tindex = 0
                print("Out of Range Undo, Undo at First Value")
            else:
                self.tindex = self.tindex-steps
            self.value = self.travlist[self.tindex]
            
            self.check=True
            self.dc+=1
            print(self.travlist,self.value,self.index,self.tindex)

    def bulk_redo(self, steps: int):
        if self.index >0:
            if self.check == True:
                if self.tindex+steps>self.index:
                    self.tindex = self.index
                    self.value +=self.dict1[self.tindex-1]
                    self.travlist.append(self.value)
                    self.index=len(self.travlist)-1
                else:
                    self.tindex = self.tindex+steps
                self.value = self.travlist[self.tindex]
                
                self.dc+=1
                print(self.travlist,self.value,self.index,self.tindex)
                
            if self.tindex == self.index:
                self.check = False
        # for i in range(steps):
        #     self.redo()
    
    def clear(self):
        self.value=0
        # if self.index == None:
        #     self.index = 0
        if self.index != self.tindex:
            self.index = self.tindex+1
            del self.travlist[self.index:]
        else:
            self.index+=1
            
        self.travlist.insert(self.index, self.value) 
        
        self.tindex = self.index
        self.dc+=1
        print(self.travlist,self.value,self.index,self.tindex)
