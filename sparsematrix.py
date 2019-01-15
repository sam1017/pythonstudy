class sparse_matrix():
    def __init__(self, sparse_matrix_view, matrix_setting):
        self.sparse_matrix_view = sparse_matrix_view
        self.matrix_setting = matrix_setting
        self.row = matrix_setting[0]
        self.column = matrix_setting[1]
        self.non_zero_element_count = len(sparse_matrix_view)
        self.non_zero_element_keys = self.get_sparse_matrix_tuple(sparse_matrix_view)
        self.assist_array = self.get_assist_array(self.non_zero_element_keys)
        self.matrix_view = self.init(sparse_matrix_view)

    def get_row(self):
        return self.row

    def get_column(self):
        return self.column

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
        print("this matrix have " + str(self.non_zero_element_count) + " non_zero_element" )
        for rows in self.matrix_view:
            print(rows)
        print("this matrix's non zero element keys: ")
        print(self.non_zero_element_keys)
        print("this matrix's assist array : ")
        print(self.assist_array)

    def matrix_T(self):
        matrix_view_T = []
        for i in range(0, self.column):
            rows = []
            for j in range(0, self.row):
                rows.append(matrix_view[j][i])
            matrix_view_T.append(rows)
        return matrix_view_T

    def sparse_matrix_T(self):
        sparse_matrix_view_T = {}
        for key in self.sparse_matrix_view.keys():
            new_key = (key[1], key[0])
            sparse_matrix_view_T[new_key] = self.sparse_matrix_view[key]
        matrix_setting_T = (self.matrix_setting[1],self.matrix_setting[0])
        return sparse_matrix(sparse_matrix_view_T, matrix_setting_T)

    def get_sparse_matrix_tuple(self, sparse_matrix_view):
        non_zero_element_keys = []
        for key in sorted(self.sparse_matrix_view.keys()):
            non_zero_element_keys.append(key)
        return non_zero_element_keys

    def get_assist_array(self, non_zero_element_keys):
        assist_arrays = []
        index = 0
        for i in range(0, self.row):
            assist_value = [0, 0]
            while index < len(non_zero_element_keys) and non_zero_element_keys[index][0] <= (i+1):
                if assist_value[0] == 0:
                    assist_value[0] = non_zero_element_keys[index][1]
                assist_value[1] = assist_value[1] + 1
                index = index + 1
            assist_arrays.append(assist_value)
        return assist_arrays

def sparse_matrix_multiply(sparse_matrix_A, sparse_matrix_B):
    if sparse_matrix_A.get_column() != sparse_matrix_B.get_row():
        print("This two matrix can't multiply")
        return None

    sparse_matrix_B_T = sparse_matrix_B.sparse_matrix_T()


sparse_matrix_view = {(1,2): 12, (1,3): 19, (3,1): -3, (3,6): 14, (4,3): 24,(5,2): 18,(6,1): 15,(6,4): -7}
matrix_setting = (6,7)
my_sparse_matrix = sparse_matrix(sparse_matrix_view, matrix_setting)
my_sparse_matrix.show()
my_sparse_matrix_T = my_sparse_matrix.sparse_matrix_T()
my_sparse_matrix_T.show()
