# - types of quantities -
#
# number
# weight
# size in bag
# non measurable

class Food:
    def __init__(self, name, quantity, quantity_type):
        self.name = name
        self.quantity = quantity
        self.quantity_type = quantity_type

    def __repr__(self):
        return f"Food(name={self.name}, quantity={self.quantity}, quantity_type={self.quantity_type})"