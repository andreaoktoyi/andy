class person:
   def __init__(self,name,job=None,pay=0):
         self.name=name
         self.job=job
         self.pay=pay
   def firstname(self):
        return self.name.split()[0]
        
   def lastname(self):
        return self.name.split()[-1]
        
   def giveRaise(self, percent):
       #print(self.pay)
       #return self.pay = int(self.pay*(1+ percent))
       print(self.pay)
        
        
class Manager(person):
   def __init__(self,name,pay):
        person.__init__(self,name,'Mgr',pay)
        
   def giveRaise(self,percent,bonus=0.10):
        person.giveRaise(self,percent+bonus)

if __name__ =='__main__':
    
      John = Manager('James Bond',50000)
      
      John.giveRaise(.20)
      
print (John)
