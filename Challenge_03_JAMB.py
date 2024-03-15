class MenuItem:
    def __init__(self):
        pass
    def calculate_total_price(self):
        return 0


class Beverage(MenuItem):
    def __init__(self, size):
        self.size = size
    def calculate_total_price(self):
        total = 0
        if self.size == "Small": total *= 0.75
        if self.size == "Regular": total *= 1
        if self.size == "Large": total *= 1.5
        return total 

class Water(Beverage):
    def __init__(self, size):
        super().__init__(size)

    def calculate_total_price(self):
        total = 1500
        if self.size == "Small": total *= 0
        if self.size == "Regular": total *= 0
        if self.size == "Large": total *= 1
        return total   

class Juice(Beverage):
    def __init__(self, size, fruit):
        super().__init__(size)
        self.fruit = fruit

    def calculate_total_price(self):
        total = 2000
        if self.size == "Small": total *= 0.75
        if self.size == "Regular": total *= 1
        if self.size == "Large": total *= 1.5
        if self.fruit == "Orange": total *= 1
        if self.fruit == "Blackberry": total *= 1.2
        if self.fruit == "Mango": total *= 1.4
        return total 
 
class Soda(Beverage):
    def __init__(self, size, flavor):
        super().__init__(size)
        self.flavor = flavor

    def calculate_total_price(self):
        total = 3000
        if self.size == "Small": total *= 0.75
        if self.size == "Regular": total *= 1
        if self.size == "Large": total *= 1.5
        if self.flavor == "Coke": total += 100
        if self.flavor == "Lemon": total += 200
        if self.flavor == "Grapefruit": total += 500
        return total 

class Beer(Beverage):
    def __init__(self, size, brand):
        super().__init__(size)
        self.brand = brand
    
    def calculate_total_price(self):
        total = 4000
        if self.brand == "Corona": total += 500
        if self.brand == "Budweiser": total += 1000
        if self.brand == "Heineken": total += 1500
        if self.size == "Small": total *= 0.75
        if self.size == "Regular": total *= 1
        if self.size == "Large": total *= 1.5
        return total



class Appetizer(MenuItem):
    def __init__(self, double):
        self.double = double

    def calculate_total_price(self):
        total = 0
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        return total

class Soup(Appetizer):
    def __init__(self, double, type):
        super().__init__(double)
        self.type = type

    def calculate_total_price(self):
        total = 4000
        if self.type == "Corn": total += 0
        if self.type == "Tomato": total += 200
        if self.type == "Chicken": total += 500
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        return total

class Egg(Appetizer):
    def __init__(self, double, preparation):
        super().__init__(double)
        self.preparation = preparation

    def calculate_total_price(self):
        total = 2000
        if self.preparation == "Boiled": total += 0
        if self.preparation == "Fried": total += 400
        if self.preparation == "Scrambled": total += 800
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        return total

class Fruit(Appetizer):
    def __init__(self, double, kind):
        super().__init__(double)
        self.kind = kind

    def calculate_total_price(self):
        total = 3000
        if self.kind == "Banana": total += 0
        if self.kind == "Apple": total += 300
        if self.kind == "Strawberry": total += 700
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        return total

class Salad(Appetizer):
    def __init__(self, double, aditive):
        super().__init__(double)
        self.aditive = aditive

    def calculate_total_price(self):
        total = 4000
        if self.double == "Simple": total *= 1
        if self.double == "Double": total *= 1.8
        if self.aditive == "No Aditive": total += 0
        if self.aditive == "Vinegar": total += 100
        if self.aditive == "Vinaigrette": total += 200
        if self.aditive == "Olive Oil": total += 300
        return total




class MainCourse(MenuItem):
    def __init__(self, addition):
        self.addition = addition

    def calculate_total_price(self):
        total = 0
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        return total     

class Rice(MainCourse):
    def __init__(self, addition, color):
        super().__init__(addition)
        self.color = color

    def calculate_total_price(self):
        total = 8000
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        if self.color == "White": total += 0
        if self.color == "Yellow": total += 100
        if self.color == "Green": total += 400
        return total        

class Meat(MainCourse):
    def __init__(self, addition, vegan):
        super().__init__(addition)
        self.vegan = vegan

    def calculate_total_price(self):
        total = 12000
        if self.vegan == "Meat": total += 0
        if self.vegan == "No Meat": total += 3000
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        return total    

class Pasta(MainCourse):
    def __init__(self, addition, variety):
        super().__init__(addition)
        self.variety = variety

    def calculate_total_price(self):
        total = 10000
        if self.variety == "Spaghetti": total += 0
        if self.variety == "Shells": total += 700
        if self.variety == "Macaroni": total += 1500
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        return total    

class Vegetables(MainCourse):
    def __init__(self, addition, making):
        super().__init__(addition)
        self.making = making

    def calculate_total_price(self):
        total = 8000
        if self.addition == "No Extra": total *= 1
        if self.addition == "Extra": total *= 1.5
        if self.making == "Boiled": total += 0
        if self.making == "Baked": total += 500
        if self.making == "Sauteed": total += 1000
        return total    



class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item=1):
        self.items.append((item))

    def calculate_total_bill(self):
        total_bill = 0
        for item in self.items:
            total_bill += item.calculate_total_price()
        return int(total_bill)
        
    def protocol(self):
        course_ini = int(input("\tMain Course" "\n" "We offer:"  "\nRice\t\tIf you want Rice,\t write 1" "\nMeat\t\tIf you want Meat,\t write 2" "\nPasta\t\tIf you want Pasta,\t write 3" "\nVegetables\tIf you want Vegetables,\t write 4" "\nIf you don't want a Main Course,\t write 5\n"))

        if course_ini < 5:
            var_1 = ""
            con_1 = int(input("\nIf you want a Regular ration,\t\t write 1" "\nIf you want an Extra ration,\t\t write 2\n"))    
            if con_1 == 1: var_1 = "No Extra"
            if con_1 == 2: var_1 = 'Extra'
            
            if course_ini == 1:
                var_2 = ""
                con_2 = int(input("\nIf you want White Rice,\t\t\t write 1" "\nIf you want Yellow Rice,\t\t write 2" "\nIf you want Green Rice,\t\t\t write 3\n"))
                if con_2 == 1: var_2 = "White"
                if con_2 == 2: var_2 = "Yellow"
                if con_2 == 3: var_2 = "Green"
                order.add_item(Rice(var_1, var_2))

            if course_ini == 2:
                var_2 = ""
                con_2 = int(input("\nIf you want Regular Meat,\t\t write 1" "\nIf you want Vegan Meat,\t\t\t write 2\n"))    
                if con_2 == 1: var_2 = "Meat"
                if con_2 == 2: var_2 = "No Meat"
                order.add_item(Meat(var_1, var_2))

            if course_ini == 3:
                var_2 = ""
                con_2 = int(input("\nIf you want Spaghetti,\t\t\t write 1" "\nIf you want Shells,\t\t\t write 2" "\nIf you want Macaroni,\t\t\t write 3\n"))  
                if con_2 == 1: var_2 = "Spaghetti"
                if con_2 == 2: var_2 = "Shells"
                if con_2 == 3: var_2 = "Macaroni"
                order.add_item(Pasta(var_1, var_2))

            if course_ini == 4:
                var_2 = ""
                con_2 = int(input("\nIf you want Boiled Vegetables,\t\t write 1" "\nIf you want Baked Vegetables,\t\t write 2" "\nIf you want Sauteed Vegetables,\t\t write 3\n"))
                if con_2 == 1: var_2 = "Boiled"
                if con_2 == 2: var_2 = "Baked"
                if con_2 == 3: var_2 = "Sauteed"
                order.add_item(Vegetables(var_1, var_2))

        if course_ini >= 5: pass



        appeti_ini = int(input("\t\tAppetizer" "\n" "We offer:"  "\nSoup\t\tIf you want Soup,\t write 1" "\nEgg\t\tIf you want Egg,\t write 2" "\nFruit\t\tIf you want Fruit,\t write 3" "\nSalad\t\tIf you want Salad,\t write 4" "\nIf you don't want a Appetizer,\t\t write 5\n"))

        if appeti_ini < 5:
            var_1 = ""
            con_1 = int(input("\nIf you want a Regular ration,\t\t write 1" "\nIf you want a Double ration,\t\t write 2\n"))    
            if con_1 == 1: var_1 = "Single"
            if con_1 == 2: var_1 = 'Double'
            
            if appeti_ini == 1:
                var_2 = ""
                con_2 = int(input("\nIf you want a Corn Soup,\t\t write 1" "\nIf you want a Tomato Soup,\t\t write 2" "\nIf you want a Chicken Soup,\t\t write 3\n"))
                if con_2 == 1: var_2 = "Corn"
                if con_2 == 2: var_2 = "Tomato"
                if con_2 == 3: var_2 = "Chicken"
                order.add_item(Soup(var_1, var_2))

            if appeti_ini == 2:
                var_2 = ""
                con_2 = int(input("\nIf you want the Egg Boiled,\t\t write 1" "\nIf you want the Egg Fried,\t\t write 2" "\nIf you want the Egg Scrambled,\t\t write 3\n"))
                if con_2 == 1: var_2 = "Boiled"
                if con_2 == 2: var_2 = "Fried"
                if con_2 == 3: var_2 = "Scrambled"
                order.add_item(Egg(var_1, var_2))

            if appeti_ini == 3:
                var_2 = ""
                con_2 = int(input("\nIf you want Banana,\t\t\t write 1" "\nIf you want Apple,\t\t\t write 2" "\nIf you want Strawberry,\t\t\t write 3\n"))
                if con_2 == 1: var_2 = "Banana"
                if con_2 == 2: var_2 = "Apple"
                if con_2 == 3: var_2 = "Strawberry"
                order.add_item(Fruit(var_1, var_2))

            if appeti_ini == 4:
                var_2 = ""
                con_2 = int(input("\nIf you want No Aditive in your Salad,\t write 1" "\nIf you want Vinegar in your Salad,\t write 2" "\nIf you want Vinaigrette in your Salad,\t write 3" "\nIf you want Olive Oil in your Salad,\t write 4\n"))
                if con_2 == 1: var_2 = "No Aditive"
                if con_2 == 2: var_2 = "Vinegar"
                if con_2 == 3: var_2 = "Vinaigrette"
                if con_2 == 4: var_2 = "Olive Oil"
                order.add_item(Salad(var_1, var_2))

        if appeti_ini >= 5: pass



        bevera_ini = int(input("\t\tBeverage" "\n" "We offer:" "\nWater\t\tIf you want Water,\t write 1" "\nJuice\t\tIf you want Juice,\t write 2" "\nSoda\t\tIf you want Soda,\t write 3" "\nBeer\t\tIf you want Beer,\t write 4" "\nIf you don't want a Beverage,\t\t write 5\n"))

        if bevera_ini < 5:
            var_1 = ""
            con_1 = int(input("\nIf you want a Small Drink,\t\t write 1" "\nIf you want a Regular Drink,\t\t write 2" "\nIf you want a Large Drink,\t\t write 3\n"))    
            if con_1 == 1: var_1 = "Small"
            if con_1 == 2: var_1 = 'Regular'
            if con_1 == 3: var_1 = 'Large'
            
            if bevera_ini == 1:
                order.add_item(Water(var_1))

            if bevera_ini == 2:
                var_2 = ""
                con_2 = int(input("\nIf you want Orange Juice,\t\t write 1" "\nIf you want Blackberry Juice,\t\t write 2" "\nIf you want Mango Juice,\t\t write 3\n"))
                if con_2 == 1: var_2 = "Orange"
                if con_2 == 2: var_2 = "Blackberry"
                if con_2 == 3: var_2 = "Mango"
                order.add_item(Juice(var_1, var_2))

            if bevera_ini == 3:
                var_2 = ""
                con_2 = int(input("\nIf you want Coca-Cola,\t\t\t write 1" "\nIf you want Sprite,\t\t\t write 2" "\nIf you want Quatro,\t\t\t write 3\n"))
                if con_2 == 1: var_2 = "Coke"
                if con_2 == 2: var_2 = "Lemon"
                if con_2 == 3: var_2 = "Grapefruit"
                order.add_item(Soda(var_1, var_2))

            if bevera_ini == 4:
                var_2 = ""
                con_2 = int(input("\nIf you want Corona,\t\t\t write 1" "\nIf you want Budweiser,\t\t\t write 2" "\nIf you want Heineken,\t\t\t write 3\n"))
                if con_2 == 1: var_2 = "Corona"
                if con_2 == 2: var_2 = "Budweiser"
                if con_2 == 3: var_2 = "Heineken"
                order.add_item(Beer(var_1, var_2))

        if bevera_ini >= 5: pass

class Exercise(Order):
    def __init__(self, program, iterations):
        self.program = program
        self.iterations = iterations

    def execute(self):
        challenge = self.program
        counter = self.iterations
        while counter > 0:
            challenge.protocol()
            counter -=1
        return challenge.calculate_total_bill()
            
       


if __name__ == "__main__": 
    counter = int(input("Welcome to this establishment\nHow many people?\n"))
    order = Order()
    challenge_03 = Exercise(order, counter)
    print(f"\nThe total bill is:     ${challenge_03.execute()} \nThanks for coming!")

    