class sparse_matrix():
    def __init__(self, sparse_matrix_view, matrix_setting):
        self.sparse_matrix_view = sparse_matrix_view
        self.matrix_setting = matrix_setting
        self.row = matrix_setting[0]
        self.column = matrix_setting[1]
        self.non_zero_element_count = len(sparse_matrix_view)
        self.non_zero_element_keys = self.get_sparse_matrix_tuple(sparse_matrix_view)
        self.assist_array = self.init_assist_array(self.non_zero_element_keys)
        self.matrix_view = self.init(sparse_matrix_view)

    def get_sparse_matrix_view(self):
        return self.sparse_matrix_view

    def get_non_zero_element_keys(self):
        return self.non_zero_element_keys

    def get_assist_arrays(self):
        return self.assist_array

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
        print(self.sparse_matrix_view)

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

    def init_assist_array(self, non_zero_element_keys):
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

    result_sparse_matrix_view = {}
    matrix_setting = (sparse_matrix_A.get_row(), sparse_matrix_B.get_column())
    sparse_matrix_B_T = sparse_matrix_B.sparse_matrix_T()
    print("sparse_matrix_multiply")
    #sparse_matrix_A.show()
    #sparse_matrix_B_T.show()
    for i in range(1,sparse_matrix_A.get_row()+1):
        for j in range(1,sparse_matrix_B_T.get_row() +1):
            value = sparse_matrix_row_multiply(sparse_matrix_A, i, sparse_matrix_B_T, j)
            if value != 0 :
                result_sparse_matrix_view[(i,j)] = value
    result_sparse_matrix = sparse_matrix(result_sparse_matrix_view, matrix_setting)
    return result_sparse_matrix

def sparse_matrix_row_multiply(sparse_matrix_A, i, sparse_matrix_B, j):
    if i > sparse_matrix_A.get_row() or j > sparse_matrix_B.get_row() or i < 1 or j < 1 :
        print("input parameter error ! ")
        return None
    #print("sparse_matrix_row_multiply i = " + str(i) + " j = " + str(j))
    assist_array_A = sparse_matrix_A.get_assist_arrays()[i-1]
    non_zero_element_keys_A = sparse_matrix_A.get_non_zero_element_keys()
    if assist_array_A[0] != 0:
        index_A = non_zero_element_keys_A.index((i,assist_array_A[0]))
        length_A = assist_array_A[1]
    else:
        index_A = -1
        length_A = -1
    assist_array_B = sparse_matrix_B.get_assist_arrays()[j-1]
    non_zero_element_keys_B = sparse_matrix_B.get_non_zero_element_keys()
    if assist_array_B[0] != 0:
        index_B = non_zero_element_keys_B.index((j,assist_array_B[0]))
        length_B = assist_array_B[1]
    else:
        index_B = -1
        length_B = -1

    value = 0
    #print("index a = " + str(index_A ) + " to " + str( index_A + length_A ) + " index b = " + str(index_B ) + " to " + str(index_B + length_B ))
    if index_A >=0 and length_A >=1 and index_B >=0 and length_B >=1 :
        sparse_matrix_view_A = sparse_matrix_A.get_sparse_matrix_view()
        sparse_matrix_view_B = sparse_matrix_B.get_sparse_matrix_view()
        for key_A in non_zero_element_keys_A[index_A:index_A+length_A]:
            for key_B in non_zero_element_keys_B[index_B:index_B+length_B]:
                #print("key_a " + str(key_A[1]) + " key_b " + str(key_B[1]))
                if key_A[1] == key_B[1]:
                    value = value + sparse_matrix_view_A[key_A]*sparse_matrix_view_B[key_B]
    #print("return value = " + str(value))
    return value

sparse_matrix_view = {(1,2): 12, (1,3): 19, (3,1): -3, (3,6): 14, (4,3): 24,(5,2): 18,(6,1): 15,(6,4): -7}
matrix_setting = (6,7)
my_sparse_matrix = sparse_matrix(sparse_matrix_view, matrix_setting)
my_sparse_matrix.show()
my_sparse_matrix_T = my_sparse_matrix.sparse_matrix_T()
my_sparse_matrix_T.show()
matrix_A = sparse_matrix_multiply(my_sparse_matrix, my_sparse_matrix_T)
matrix_A.show()