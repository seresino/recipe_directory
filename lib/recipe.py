class Recipe:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, title, avg_time, rating):
        self.id = id
        self.title = title
        self.avg_time = avg_time
        self.rating = rating

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print a Recipe
    def __repr__(self):
        return f"Recipe({self.id}, {self.title}, {self.avg_time}, {self.rating})"
