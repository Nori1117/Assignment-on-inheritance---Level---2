'''

An apparel shop wants to manage the items which it sells. 25 min

Write a python program to implement the class diagram given below.



Class Description:

Apparel class:

Initialize static variable counter to 100

In the constructor, auto-generate item_id starting from 101 prefixed by "C" for cotton apparels and "S" for silk apparels. Example – C101, S102, S103, C104 etc.

calculate_price(): Add 5% service tax on the price of the apparel and update attribute, price with the new value

Cotton class:

While invoking parent constructor from child constructor, pass "Cotton" as item_type

calculate_price(): Update attribute, price of Apparel class based on rules given below

Add service tax on price by invoking appropriate method of Apparel class

Apply discount on price

Add 5% VAT on final price

Silk class:

While invoking parent constructor from child constructor, pass "Silk" as item_type

calculate_price(): Update attribute, price of Apparel class based on rules given below

Add service tax on price by invoking appropriate method of Apparel class

Identify points earned based on rules given below:

Silk apparels with price more than Rs. 10000, earn 10 points and anything less than or equal to that earn 3 points

Initialize attribute, points with the identified points

Add 10% VAT on price

Note: Perform case sensitive string comparison  

'''

#lex_auth_012753087522512896330
#Start writing your code here
class Apparel:
    counter=100
    def __init__(self, price, item_type):
        apparel+=1
        self.__item_id=item_type[0]+str(apparel.counter)
        self.__price=price
        self.__item_type=item_type
        
    def calculate_price(self):
        self.__price+=self.__price*0.05
        
        
    def get_item_id(self):
        return self.__item_id
        
    def get_price(self):
        return self.__price
        
    def get_item_type(self):
        return self.__item_type
        
    def set_price(self, price):
        self.__price=price
        
        
        
class Cotton(Apparel):
    def __init__(self, price, discount):
        super().__init__(price, "cotton")
        self.__discount=discount
    
    def calculate_price(self):
        super().calculate_price()
        price=self.get_price()
        price-=price*(self.__discount/100)
        price+=price*0.05
        self.set_price(price)
        
    def get_discount(self):
         return self.__discount
         
         
class Silk(Apparel):

    def __init__(self,price):

        super().__init__(price,"Silk")

        self.__points=None

        
    def calculate_price(self):

        super().calculate_price()

        if self.get_price()>10000:

            self.__points=10 

        else:

            self.__points=3 

        self.set_price(self.get_price()+(self.get_price()*0.1))

        

        

    def get_points(self):

        return self.__points
        
        
        
        
    
    
        
        
