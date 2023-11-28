from lib.recipe import Recipe

class RecipeRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all recipes
    def all(self):
        rows = self._connection.execute('SELECT * from recipes')
        recipes = []
        for row in rows:
            item = Recipe(row["id"], row["title"], row["avg_time"], row["rating"])
            recipes.append(item)
        return recipes

    # Find a single recipe by their id
    def find(self, recipe_id):
        rows = self._connection.execute(
            'SELECT * from recipes WHERE id = %s', [recipe_id])
        row = rows[0]
        return Recipe(row["id"], row["title"], row["avg_time"], row["rating"])
