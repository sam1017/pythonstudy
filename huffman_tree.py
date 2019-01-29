
class huffman_tree():
    def __init__(self, value):
        self.value = value
        self.item_path= []
        self.left_tree = None
        self.right_tree = None

    def if_have_son_tree(self):
        if (self.left_tree != None) and (self.right_tree != None) :
            return True
        else:
            return False

    def get_value(self):
        return self.value

    def get_item_path(self):
        return self.item_path

    def add_path(self, path):
        item_path = self.get_item_path()
        item_path.insert(0, path)
        if self.if_have_son_tree():
            self.left_tree.add_path(path)
            self.right_tree.add_path(path)

    def show(self):
        if self.if_have_son_tree():
            self.left_tree.show()
            self.right_tree.show()
        else:
            print("value = " + str(self.get_value()))
            print(self.get_item_path())

def produce_new_huffman_tree(ascending_binary_forest):
    if len(ascending_binary_forest) == 1:
        return ascending_binary_forest[0]
    elif len(ascending_binary_forest) > 1:
        left_tree = ascending_binary_forest.pop(0)
        left_tree.add_path(0)
        right_tree = ascending_binary_forest.pop(0)
        right_tree.add_path(1)
        new_tree_value = left_tree.get_value() + right_tree.get_value()
        new_tree = huffman_tree(new_tree_value)
        new_tree.left_tree = left_tree
        new_tree.right_tree = right_tree
        for i in range(0, len(ascending_binary_forest)):
            if ascending_binary_forest[i].get_value() > new_tree.get_value():
                ascending_binary_forest.insert(i, new_tree)
                break
        if(new_tree not in ascending_binary_forest):
            ascending_binary_forest.append(new_tree)
        print("ascending_binary_forest len " + str(len(ascending_binary_forest)))
        return produce_new_huffman_tree(ascending_binary_forest)

list_value = [5,29,7,8,14,23,3,11]
list_value.sort()
ascending_binary_forest = []
for value in list_value:
    ascending_binary_forest.append(huffman_tree(value))

my_huffman_tree = produce_new_huffman_tree(ascending_binary_forest)
#my_huffman_tree = ascending_binary_forest[0]
print("my_huffman_tree show")
my_huffman_tree.show()
