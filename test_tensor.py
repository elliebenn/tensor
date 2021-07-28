import unittest
 
from tensor import Tensor

class TestTensorMethods(unittest.TestCase):
    
    def test_Tensor_creation(self):
        root = Tensor([1], [1])
        self.assertIsNone(root.children)
        self.assertListEqual([1], root.lst)

    def test_children_Tensor(self):
        root = Tensor([ 1, 2, 3, 4, 5, 6 ], [ 2, 3 ])
        self.assertIsNotNone(root.children)
        self.assertListEqual(root.children[0].lst, [ 1, 2, 3 ])
        self.assertListEqual(root.children[1].lst, [ 4, 5, 6 ])

    def test_tree_three_levels(self):
        root = Tensor([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24 ],  [ 4, 2, 3 ])
        self.assertIsNotNone(root.children)
        self.assertListEqual(root.children[0].children[0].lst, [1, 2, 3])
        self.assertListEqual(root.children[3].children[1].lst, [22, 23, 24])

    def test_print_tree_no_children(self):
        root = Tensor([1, 2, 3], [3])
        
        actual_result = root.print_tree()
        expected_result = "[1, 2, 3]"

        self.assertEqual(expected_result, actual_result)

    def test_print_tree_one_set_of_children(self):
        root = Tensor( [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1], [5, 2])

        actual_result = root.print_tree()
        expected_result = "[[0, 1], [2, 3], [4, 5], [0.1, 0.2], [-3, -2]]"

        self.assertEqual(expected_result, actual_result)

    def test_print_tree_two_sets_of_children(self):
        root = Tensor( [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3], [2, 3, 2])
        
        actual_result = root.print_tree()
        expected_result = "[[[0, 1], [2, 3], [4, 5]], [[0.1, 0.2], [-3, 0], [0, 0]]]"

        self.assertEqual(expected_result, actual_result)

    def test_empty_shape(self):
        root = Tensor( [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3], [])
        
        actual_result = root.print_tree()
        expected_result = "[]"

        self.assertEqual(expected_result, actual_result)

    def test_shape_error_negative_value(self):
        with self.assertRaises(Exception) as context:
            root = Tensor( [1, 2, 3], [-1,2,3] )
            self.assertTrue("Shape is not of the correct format." in context.exception)

    def test_shape_error_not_integer(self):
        with self.assertRaises(Exception) as context:
            root = Tensor( [1, 2, 3], [-1,2.3,3] )
            self.assertTrue("Shape is not of the correct format." in context.exception)

    def test_data_with_nonnumeric(self):
        with self.assertRaises(Exception) as context:
            root = Tensor( "Hello", "World!", [1,2])
            self.assertTrue("Data has a non-numeric value." in context.exception)