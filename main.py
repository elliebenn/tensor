from tensor import Tensor

if __name__ == "__main__":
    data0 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3]
    shape0 = [2, 3, 2]
    tensor0 = Tensor(data0, shape0)

    print("output: \n" + tensor0.print_tree())

    data1 = [0, 1, 2, 3, 4, 5, 0.1, 0.2, -3, -2, -1, 3, 2, 1]
    shape1 = [5, 2]
    tensor1 = Tensor(data1, shape1)
    print("output: \n" + tensor1.print_tree())