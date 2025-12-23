class Person: 
     def __init__(self): 
          self.__age = 0
       
     # using property decorator 
     # a getter function 
     @property
     def age(self): 
         print("getter method called") 
         return self.__age 
       
     # a setter function 
     @age.setter 
     def age(self, a): 
         if(a < 18): 
            raise ValueError("Sorry you age is below eligibility criteria") 
         print("setter method called") 
         self.__age = a 
  
mark = Person() # will throw err
  
mark.age = 18 # will also throw err
  
print(mark.age)