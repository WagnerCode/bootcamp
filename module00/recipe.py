cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "desert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    }
}

def print_recipes_name():
    for key in cookbook.keys():
        print(key)

def print_details_of_recipe():
    i = 0
    for key in cookbook.keys():
        print(key)
        print(cookbook[list(cookbook.keys())[i]])
        i += 1

def delete_recipe(name):
    del cookbook[f'{name}']

def add_recipe():
    print("Enter a name: ")
    name = input()
    cookbook[f"{name}"] = {}
    print("Enter ingredients: ")
    ingredients = []
    ingredients.append(input())
    i = 0
    while(ingredients[i] != ""):
        ingredients.append(input())
        i += 1
    cookbook[f"{name}"]["ingredients"] = f"{ingredients}"
    print("Enter a meal type: ")
    meal = input()
    cookbook[f"{name}"]["meal"] = f"{meal}"
    print("Enter a preparation time: ")
    time = input()
    cookbook[f"{name}"]["time"] = time

print("Welcome to the Python Cookbook ! \n \
List of available options: \n "
"1: Add a recipe \n \
2: Delete a recipe \n \
3: Print a recipe \n \
4: Print the cookbook \n \
5: Quit \n ")

var = 0
while var != 5:
    print("Please select an option: ")
    var = int(input())
    if var == 1:
        add_recipe()
    elif var == 2:
        print("Please print recipe name to delete it: ")
        name = input()
        delete_recipe(f"{name}")
    elif var == 3:
        print("Please print recipe name to print it: ")
        detail = input()
        print("Ingredients list: ", cookbook[f"{detail}"]["ingredients"])
        print("To be eaten for: ", cookbook[f"{detail}"]["meal"])
        print("Takes ", cookbook[f"{detail}"]["prep_time"], "minutes of cooking")
    elif var == 4:
        print_recipes_name()
    elif var == 5:
        print("Cookbook closed. Goodbye !")
        break