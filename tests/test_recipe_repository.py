from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe

"""
When we call RecipeRepository#all
We get a list of Recipe objects reflecting the seed data.
"""
def test_get_all_recipes(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/recipes.sql") # Seed our database with some test data
    repository = RecipeRepository(db_connection) # Create a new RecipeRepository

    recipes = repository.all() # Get all recipes

    # Assert on the results
    assert recipes == [
        Recipe(1, 'Shepherds Pie', 60, 4),
        Recipe(2, 'Mushroom Noodle Soup', 30, 5),
        Recipe(3, 'Polenta Cake', 45, 2),
        Recipe(4, 'Salmon Stir Fry', 35, 4),
        Recipe(5, 'Pesto Pasta', 15, 3)
    ]

"""
When we call RecipeRepository#find
We get a single Recipe object reflecting the seed data.
"""
def test_get_single_recipe(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)

    recipe = repository.find(1)
    assert recipe == Recipe(1, 'Shepherds Pie', 60, 4)