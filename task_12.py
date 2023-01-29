from task_11 import Dessert


class JellyBean(Dessert):
    def __init__(self, name=None, calories=None, flavor=None):
        Dessert.__init__(self, name, calories)
        self.__flavor = flavor

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, new_flavor):
        self.__flavor = new_flavor

    def is_delicious(self):
        if str(self.__flavor) == 'black licorice':
            return False
        return True


dessert1 = JellyBean('pavlova', 500, 'black licorice')
dessert2 = JellyBean()
dessert2.name = 'napoleon'
dessert2.calories = 199
dessert2.flavor = 'strawberry'
print("Dessert1 is " + str(dessert1.name))
print("Its calories is " + str(dessert1.calories))
print("Its flavor is " + str(dessert1.flavor))
print("Is it healthy? " + str(dessert1.is_healthy()))
print("Is it delicious? " + str(dessert1.is_delicious()))
print()
print("Dessert2 is " + str(dessert2.name))
print("Its calories is " + str(dessert2.calories))
print("Its flavor is " + str(dessert2.flavor))
print("Is it healthy? " + str(dessert2.is_healthy()))
print("Is it delicious? " + str(dessert2.is_delicious()))
