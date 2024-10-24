import datetime
from datetime import date
from datetime import datetime

class Book:
    name = ''
    last_update = ''
    creation_date = ''
    recipes_list = {'starter': [], 'lunch': [], 'dessert': []}
    def __init__(self, name):
        self.name = name
        self.creation_date = date.today()

    def get_recipe_by_name(self, name):
        if name in self.recipes_list['lunch']:
            print(str(name))
        elif name in self.recipes_list['starter']:
            print(str(name))
        elif name in self.recipes_list['dessert']:
            print(str(name))
        else:
            print("No such name")

    def get_recipes_by_types(self, recipe_type):
        for key in self.recipes_list:
            if key == recipe_type:
                print(self.recipes_list[key])

    def add_recipe(self, recipe):
        self.last_update = datetime.now()
        self.recipes_list[f"{recipe.recipe_type}"].append(recipe)



