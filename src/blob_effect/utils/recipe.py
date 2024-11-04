class Recipe:

    def __init__(self, *args):
        self.recipe = list()
        for arg in args:
            self.recipe.append(arg)

    def __call__(self):
        """iterate over the recipe and call the task"""
        for task in self.recipe:
            yield task

    def add(self, task):
        self.recipe.append(task)
