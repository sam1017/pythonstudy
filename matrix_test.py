class matrix():
    def __init__(self, matrix_view):
        self.matrix_view = matrix_view
        self.row = len(matrix_view)
        self.column = len(matrix_view[0])

    def show(self):
        print("this matrix is " + str(self.row) + " * " + str(self.column))
        for rows in self.matrix_view:
            print(rows)

    def matrix_T(self):
        matrix_view_T = []
        for i in range(0, self.column):
            rows = []
            for j in range(0, self.row):
                rows.append(matrix_view[j][i])
            matrix_view_T.append(rows)
        return matrix_view_T

    def get_matrix(self):
        return self.matrix_view

    def get_matrix_row(self):
        return self.row

    def get_matrix_column(self):
        return self.column

def multiply(matrix_A, matrix_B):
    matrix_view = []
    matrix_A_view = matrix_A.get_matrix();
    matrix_B_view = matrix_B.get_matrix();
    for i in range(0,matrix_A.get_matrix_row()):
        rows = []
        for j in range(0, matrix_B.get_matrix_column()):
            value = 0
            for k in range(0,matrix_A.get_matrix_column()):
                value = value + matrix_A_view[i][k]*matrix_B_view[k][j]
            rows.append(value)
        matrix_view.append(rows)
    return matrix(matrix_view)

matrix_view = [[0, 12, 19, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0],[-3, 0, 0, 0, 0, 14, 0],[0, 0, 24, 0, 0, 0, 0],[0, 18, 0, 0, 0, 0, 0],[15, 0, 0, -7, 0, 0, 0]]
my_matrix = matrix(matrix_view)
my_matrix.show()
matrix_view_T = my_matrix.matrix_T()
if matrix_view_T != None:
    my_matrix_T = matrix(matrix_view_T)
    my_matrix_T.show()

matrix_A = multiply(my_matrix, my_matrix_T)
matrix_A.show()