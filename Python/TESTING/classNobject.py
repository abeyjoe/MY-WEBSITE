class Person:
    def __init__(self, first_name, second_name):
        self.first_name = first_name
        self.second_name = second_name


user = Person("Tony", "Moore")

print(user.first_name, user.second_name)
