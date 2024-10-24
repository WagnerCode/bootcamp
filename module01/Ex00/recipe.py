class Recipe:
    flag = 0
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if name != '':
            self.name = name
        else:
            self.flag = 1
        if cooking_lvl >= 1 and cooking_lvl <= 5 and self.flag != 1:
            self.cooking_lvl = cooking_lvl
        else:
            self.flag = 2
        if cooking_time >= 0 and self.flag != 1:
            self.cooking_time = cooking_time
        else:
            self.flag = 3
        if isinstance(ingredients, list) and self.flag != 1:
            self.ingredients = ingredients
        else:
            self.flag = 4
            print("ingredients must be a list")
        self.description = description
        if (recipe_type == 'starter' or recipe_type == 'lunch' or recipe_type == "dessert") and self.flag != 1:
            self.recipe_type = recipe_type
        else:
            self.flag = 5
            print("recipe could be only starter, lunch or dessert")
        if self.flag == 1:
            print("Enter the name of recipe")
        elif self.flag == 2:
            print("Cooking lvl must be 1 to 5")
        elif self.flag == 4:
            print("Ingredients must be a list")
        elif self.flag == 3:
            print("Cooking time is negative")
    def __str__(self):
        txt = ""
        if self.flag != 0:
            "Error"
        else:
            txt = f"{self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.recipe_type}"
        return txt
    def __repr__(self):
        return self.name


