from book import Book
from recipe import Recipe


salad = Recipe('Salad', 1, 10, ['cucumber'], '', 'lunch')
Pizza = Recipe('Pizza', 2, 30, ['cheese', 'tomatoes', 'dough'], '', 'lunch')

Italiano = Book("Italiano")

Italiano.add_recipe(salad)
Italiano.add_recipe(Pizza)
Italiano.get_recipe_by_name(salad)
Italiano.get_recipe_by_name(Pizza)
Italiano.get_recipes_by_types('lunch')