class Dessert:
    def __init__(self, name=None, calories=None):
        self.__name = name
        self.__calories = calories

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, new_calories):
        self.__calories = new_calories

    def is_healthy(self):
        if type(self.calories) == int or type(self.calories) == float:
            if self.calories < 200:
                return True
        return False

    def is_delicious(self):
        return True


'''dessert1 = Dessert('pavlova', 500)
dessert2 = Dessert()
dessert2.name = 'napoleon'
dessert2.calories = 199
print("Dessert1 is " + str(dessert1.name))
print("Its calories is " + str(dessert1.calories))
print("Is it healthy? " + str(dessert1.is_healthy()))
print("Is it delicious? " + str(dessert1.is_delicious()))
print()
print("Dessert2 is " + str(dessert2.name))
print("Its calories is " + str(dessert2.calories))
print("Is it healthy? " + str(dessert2.is_healthy()))
print("Is it delicious? " + str(dessert2.is_delicious()))'''
