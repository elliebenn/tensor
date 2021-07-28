from tensor_helper import all_numbers_in_shape_are_integers_and_positive
from tensor_helper import is_numeric

class Tensor:

    # Ensure data is the correct size
    def fix_data_size(self):
        product = 1
        for num in self.shape:
            product *= num
        
        if len(self.data) < product:
            for _ in range(0, product - len(self.data)):
                self.data.append(0)
        elif len(self.data) > product:
            data = self.data[:product]


    def is_valid_data(self):
        for num in self.data:
            if not is_numeric(num):
                return False
        return True
            

    def __init__(self, data, shape):
        self.data = data
        self.shape = shape

        if not self.is_valid_data():
            ValueError("Data has a non-numeric value.")

        # Ensure data is of the right size
        self.fix_data_size()

        # Ensure shape is correct
        if not all_numbers_in_shape_are_integers_and_positive(shape):
            ValueError("Shape is not of the correct format.")

        if len(shape) >= 2:
            start_index = 0
            step_size = int(len(data)/shape[0])
            end_index = step_size

            self.children = []

            for i in range(0, shape[0]):
                self.children.append(
                    Tensor(data[start_index:end_index], shape[1:])
                )
                start_index += step_size
                end_index += step_size

        # no children -- base case
        elif len(shape) == 1:
            self.lst = data
            self.children = None
        
        # shape is empty list
        elif len(shape) == 0:
            self.lst = []
            self.children = None


    def print_tree(self):
        if self.children:
            result = "["
            for child in self.children:
                result += child.print_tree() + ", "
            
            # Trim "]," from the end
            result = result[0:-2]

            return result + "]"
        else:
            return str(self.lst)