from colorama import Fore, Style
import math
class calculator:
    def __init__ (self , x , y):
        self.x =x 
        self.y=y
    def add(self):
        return self.x +self.y 
    def subtract (self):
        return self.x - self.y
    def multiply (self):
        return self.x * self.y
    def divide (self):
        if self.x == 0 :
            return "Error : can not divide by zero."
        return self.x / self.y
    def power (self):
        return self.x ** self.y
    def sqrt (self):
        return math.sqrt(self.x)
while True:

    num_1 = float(input("Enter your first number : "))
    act = str(input("Enter your action (+ , - , * , / , ** , sqrt) : "))
    

    if act == "+" : 
        num_2 = float(input("Enter your second number : "))
        c= calculator(num_1,num_2) 
        print (num_1, "+", num_2, "=",c.add())
        
    elif act == "-":  
        num_2 = float(input("Enter your second number : "))
        c= calculator(num_1,num_2) 
        print (num_1, "-", num_2, "=",c.subtract())
        
    elif act == "*" :  
        num_2 = float(input("Enter your second number : "))
        c= calculator(num_1,num_2) 
        print (num_1, "*", num_2, "=",c.multiply())
        

    elif act == "/": 
        num_2 = float(input("Enter your second number : "))
        c= calculator(num_1,num_2)  
        print (num_1, "/", num_2, "=",c.divide())
        

    elif act == "**": 
        num_2 = float(input("Enter your second number : "))
        
        c= calculator(num_1,num_2)  
        print (num_1, "**", num_2, "=",c.power())
    elif act == "sqrt":
        c= calculator(num_1,None)
        print ("sqrt [num_1] : ", c.sqrt())

    else:
        print (Style.BRIGHT + Fore.RED + "DO it again")
        print(Style.RESET_ALL)