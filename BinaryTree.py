def binary_tree(r):
    return [r, [], []]
def insert_left(root, new_branch):
    t  = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])

    else:
        root.insert(1, [new_branch, [], []])

    return root
def insert_left(root, new_branch):
    t  = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, t, []])

    else:
        root.insert(2, [new_branch, [], []])

    return root
def get_root_val(root):
    return root[0]
def set_root_val(root,new_val):
    root[0] = new_val
def get_left_child(root):
    return root[1]
def get_right_child(root):
    return root[2]


class BinaryTree:

    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.left_child = t

    def get_right_child(self):
        return self.get_right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.key = obj

    def get_root_val(self):
        return self.key