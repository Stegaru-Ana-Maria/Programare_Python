#EX1
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def is_empty(self):
        return self.size()== 0


    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(7)
stack.push(29)
stack.push(30)
stack.push(68)

print("Stack:", stack.items)
print("Stack size:", stack.size())
print("Pop:", stack.pop())
print("Peek:", stack.peek())

#EX2
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.size() == 0

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

queue = Queue()
queue.push(15)
queue.push(98)
queue.push(35)

print("Queue: ", queue.items)
print("Queue size: ", queue.size())
print("Pop: ", queue.pop())
print("Peek: ", queue.peek())

#EX3
class Matrix:
    def __init__(self,rows,cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]

    def set(self, row, col, value):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.data[row][col] = value
        else:
            print("Error: Index out of range")

    def get(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            return self.data[row][col]
        else:
            print("Error: Index out of range")
            return None

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def transpose(self):
        transposed_matrix = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed_matrix.set(j, i, self.get(i, j))
        return transposed_matrix

    def multiply(self, other):
        if self.cols != other.rows:
            print("Error: The dimensions are not compatible for multiplication")
        result = Matrix(self.rows, other.cols)
        for i in range(result.rows):
            for j in range(result.cols):
                element_sum = 0
                for k in range(self.cols):
                    element_sum += self.get(i, k) * other.get(k, j)
                result.set(i, j, element_sum)
        return result

    def apply_function(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.set(i, j, func(self.get(i, j)))


matrix1 = Matrix(3, 4)
matrix1.set(0, 0, 1)
matrix1.set(0, 1, 2)
matrix1.set(0, 2, 3)
matrix1.set(0, 3, 4)
matrix1.set(1, 0, 5)
matrix1.set(1, 1, 6)
matrix1.set(1, 2, 7)
matrix1.set(1, 3, 8)
matrix1.set(2, 0, 9)
matrix1.set(2, 1, 10)
matrix1.set(2, 2, 11)
matrix1.set(2, 3, 12)

print("Matrix 1:")
print(matrix1)

matrix2 = Matrix(4, 3)
matrix2.set(0, 0, 2)
matrix2.set(0, 1, 3)
matrix2.set(0, 2, 4)
matrix2.set(1, 0, 1)
matrix2.set(1, 1, 2)
matrix2.set(1, 2, 3)
matrix2.set(2, 0, 5)
matrix2.set(2, 1, 6)
matrix2.set(2, 2, 7)
matrix2.set(3, 0, 8)
matrix2.set(3, 1, 9)
matrix2.set(3, 2, 10)

print("Matrix 2:")
print(matrix2)

matrix3 = Matrix(2, 3)
matrix3.set(0, 0, 2)
matrix3.set(0, 1, 3)
matrix3.set(0, 2, 4)
matrix3.set(1, 0, 1)
matrix3.set(1, 1, 2)
matrix3.set(1, 2, 3)

print("Matrix 3:")
print(matrix3)

transposed_matrix = matrix1.transpose()
print("Transposed Matrix:")
print(transposed_matrix)

multiply_result = matrix1.multiply(matrix2)
print("Multiplication Result for Matrix1 and Matrix2:")
print(multiply_result)

function = lambda x: x + 2
matrix1.apply_function(function)
print("Matrix after Applying a Transformation:")
print(matrix1)

