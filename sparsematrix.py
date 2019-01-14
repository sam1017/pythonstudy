class sparse_matrix():
    def __init__(self, sparse_matrix_view, matrix_setting):
        self.sparse_matrix_view = sparse_matrix_view
        self.matrix_setting = matrix_setting
        self.row = matrix_setting[0]
        self.column = matrix_setting[1]
        self.matrix_view = self.init(sparse_matrix_view)

    def init(self, sparse_matrix_view):
        if self.check_valid(sparse_matrix_view) == False:
            return None
        matrix_view = []
        for i in range(0, self.row):
            rows = []
            for j in range(0, self.column):
                item_key = (i+1,j+1)
                #print(item_key)
                if item_key in sparse_matrix_view.keys():
                    rows.append(sparse_matrix_view[item_key])
                else:
                    rows.append(0)
            matrix_view.append(rows)
        return matrix_view

    def check_valid(self, sparse_matrix_view):
        for key in sparse_matrix_view.keys():
            if key[0] > self.row or key[1] > self.column or key[0] < 1 or key[1] < 1:
                return False
        return True

    def show(self):
        print("this matrix is " + str(self.row) + " * " + str(self.column))
        for rows in self.matrix_view:
            print(rows)

    def matrix_T(self):
        if self.row != self.column:
            print("this matrix have no matrix_T ")
            return None
        matrix_view_T = []
        for i in range(0, self.column):
            rows = []
            for j in range(0, self.row):
                rows.append(matrix_view[j][i])
            matrix_view_T.append(rows)
        return matrix_view_T

    def sparse_matrix_T(self):
        if self.row != self.column:
            print("this matrix have no matrix_T ")
            return None
        sparse_matrix_view_T = {}
        for key in self.sparse_matrix_view.keys():
            new_key = (key[1], key[0])
            sparse_matrix_view_T[new_key] = self.sparse_matrix_view[key]
        return sparse_matrix(sparse_matrix_view_T, self.matrix_setting)


sparse_matrix_view = {(1,2): 12, (1,3): 19, (3,1): -3, (3,6): 14, (4,3): 24,(5,2): 18,(6,1): 15,(6,4): -7}
matrix_setting = (7,7)
my_sparse_matrix = sparse_matrix(sparse_matrix_view, matrix_setting)
my_sparse_matrix.show()
my_sparse_matrix_T = my_sparse_matrix.sparse_matrix_T()
my_sparse_matrix_T.show()