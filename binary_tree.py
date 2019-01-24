class binary_tree():
    def __init__(self, ascending_array, item_path):
        self.ascending_array = ascending_array
        self.item_path = item_path
        #print(self.item_path)
        length = len(self.ascending_array)
        value_index = length / 2
        self.value = ascending_array[value_index]
        if length == 1:
            self.left_binary_tree = None
            self.right_binary_tree = None
        elif length > 1:
            left_item_path = item_path[:]
            right_item_path = item_path[:]
            if value_index > 0:
                left_ascending_array = self.ascending_array[0:value_index]
                left_item_path.append(-1)
                self.left_binary_tree = binary_tree(left_ascending_array,left_item_path)
            else:
                self.left_binary_tree = None
            if length > value_index + 1:
                right_ascending_array = self.ascending_array[value_index + 1:length]
                right_item_path.append(1)
                self.right_binary_tree = binary_tree(right_ascending_array, right_item_path)
            else:
                self.right_binary_tree = None

    def show(self):
        if self.left_binary_tree != None:
            self.left_binary_tree.show()
        print(self.item_path)
        print(str(self.value))
        if self.right_binary_tree != None:
            self.right_binary_tree.show()

    def if_have_left_binary_tree(self):
        if self.left_binary_tree != None:
            return True
        else:
            return False

    def if_have_right_binary_tree(self):
        if self.right_binary_tree != None:
            return True
        else:
            return False

    def add_item(self,value):
        if self.value == value:
            print("find this item in this tree! need not to add new item! ")
        else:
            if value < self.value:
                if self.if_have_left_binary_tree():
                    self.left_binary_tree.add_item(value)
                else:
                    left_item_path = self.item_path[:]
                    left_item_path.append(-1)
                    ascending_array = []
                    ascending_array.append(value)
                    self.left_binary_tree = binary_tree(ascending_array,left_item_path)
            elif value > self.value:
                if self.if_have_right_binary_tree():
                    self.right_binary_tree.add_item(value)
                else:
                    right_item_path = self.item_path[:]
                    right_item_path.append(1)
                    ascending_array = []
                    ascending_array.append(value)
                    self.right_binary_tree = binary_tree(ascending_array,right_item_path)



ascending_array = [2, 4, 6, 9, 12, 15, 28]
item_path = [0]
my_binary_tree = binary_tree(ascending_array,item_path)
my_binary_tree.show()
my_binary_tree.add_item(18)
my_binary_tree.show()
