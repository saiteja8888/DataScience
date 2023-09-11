class dictonary_parsing:
    def __init__(self,dic):
        self.dic=dic
    def mykeys(self):
        print(self.dic.keys())
        
    def myvalues(self):
        print(self.dic.values())
        
    def correct_input(self,a):
        if type(a)==dict:
            print("you have entered correct input type")
        else:
            print("You have entered incorrect input")
    
    def user_input(self,a):
        if a in self.dic.keys():
            print("found the value",self.dic[a])
        else:
            print("unable to find the requested value")
    
    def inser_new(self,a):
        for i in a:
            self.dic[i]=a[i]
        for i in self.dic:
            print(i,self.dic[i])
