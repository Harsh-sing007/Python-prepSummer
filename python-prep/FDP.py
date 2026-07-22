# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

#     print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)



# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)


# def show_completed_models(completed_models):
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)


# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)


# class game:
#     def __init__(self, name, genre):
#         self.name = name
#         self.genre = genre
       

#     def describe_game(self):
#         print(f"{self.name} is a {self.genre} game.")

#     def set_players(self, number):
#         self.players = number

#     def increment_players(self, additional_players):
#         self.players += additional_players


class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't increment the odometer by a negative value!")