from lib.recipe import Recipe

"""
Recipe constructs with an id, name, avg_time and rating
"""
def test_recipe_constructs():
    recipe = Recipe(1, 'Shepherds Pie', 60, 4)
    assert recipe.id == 1
    assert recipe.title == 'Shepherds Pie'
    assert recipe.avg_time == 60
    assert recipe.rating == 4

"""
We can format recipes to strings nicely
"""
def test_recipes_format_nicely():
    recipe = Recipe(1, "Shepherds Pie", 60, 4)
    assert str(recipe) == "Recipe(1, Shepherds Pie, 60, 4)"
    # Try commenting out the `__repr__` method in lib/recipe.py
    # And see what happens when you run this test again.

"""
We can compare two identical recipes
And have them be equal
"""
def test_recipes_are_equal():
    recipe1 = Recipe(1, "Shepherds Pie", 60, 4)
    recipe2 = Recipe(1, "Shepherds Pie", 60, 4)
    assert recipe1 == recipe2
    # Try commenting out the `__eq__` method in lib/recipe.py
    # And see what happens when you run this test again.
