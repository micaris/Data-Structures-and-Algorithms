class BinaryTree:

    def __init__(self, root):
        self.key = root
        self.left_child = None 
        self.right_child = None 

    def insert_left(self, new_node) :
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            #push current node down and add new_node to the top
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child  = t

    def insert_right(self, new_node):
        #check for symmetry
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def get_root_value(self):
        return self.key

    def set_root_val(self, obj):
        self.key = obj

        
r = BinaryTree('a')
print(r.get_root_value())
print(r.get_left_child())
r.insert_left('b')
r.insert_right('c')
print(r.get_left_child().get_root_value())
print(r.get_right_child().get_root_value())


# Priority Queues with Binary Heaps

class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def perc_up(self, i):
        while  i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                    tmp = self.heap_list[i // 2]
                    self.heap_list[ i // 2] = self.heap_list[i]
                    self.heap_list[i] = temp
            i = i // 2

    def perc_down(self, i):
        while (i*2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                tmp = self.heap_list[i]
                self.heap_list[i] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            i = mc

    def min_child (self, i):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i*2
            else:
                return i * 2 + 1

    def del_min(self):
        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size -1
        self.heap_list.pop()
        self.perc_down(1)
        return ret_val

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.perc_up(self.current_size)

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

class Node(object):
	def __init__(self, d):
		self.data = d
		self.left = None
		self.right = None
	def insert(self, d):
		if self.data == d:
			return False
		elif d < self.data:
			if self.left:
				return self.left.insert(d)
			else:
				self.left = Node(d)
				return True
		else:
			if self.right:
				return self.right.insert(d)
			else:
				self.right = Node(d)
				return True
	def find(self, d):
		if self.data == d:
			return True
		elif d < self.data and self.left:
			return self.left.find(d)
		elif d > self.data and self.right:
			return self.right.find(d)
		return False
	def preorder(self, l):
		l.append(self.data)
		if self.left:
			self.left.preorder(l)
		if self.right:
			self.right.preorder(l)
		return l
	def postorder(self, l):
		if self.left:
			self.left.postorder(l)
		if self.right:
			self.right.postorder(l)
		l.append(self.data)
		return l
	def inorder(self, l):
		if self.left:
			self.left.inorder(l)
		l.append(self.data)
		if self.right:
			self.right.inorder(l)
		return l
		
class BST(object):
	def __init__(self):
		self.root = None
	# return True if successfully inserted, false if exists
	def insert(self, d):
		if self.root:
			return self.root.insert(d)
		else:
			self.root = Node(d)
			return True
	# return True if d is found in tree, false otherwise
	def find(self, d):
		if self.root:
			return self.root.find(d)
		else:
			return False
	# return True if node successfully removed, False if not removed
	def remove(self, d):
		# Case 1: Empty Tree?
		if self.root == None:
			return False
		
		# Case 2: Deleting root node
		if self.root.data == d:
			# Case 2.1: Root node has no children
			if self.root.left is None and self.root.right is None:
				self.root = None
				return True
			# Case 2.2: Root node has left child
			elif self.root.left and self.root.right is None:
				self.root = self.root.left
				return True
			# Case 2.3: Root node has right child
			elif self.root.left is None and self.root.right:
				self.root = self.root.right
				return True
			# Case 2.4: Root node has two children
			else:
				moveNode = self.root.right
				moveNodeParent = None
				while moveNode.left:
					moveNodeParent = moveNode
					moveNode = moveNode.left
				self.root.data = moveNode.data
				if moveNode.data < moveNodeParent.data:
					moveNodeParent.left = None
				else:
					moveNodeParent.right = None
				return True		
		# Find node to remove
		parent = None
		node = self.root
		while node and node.data != d:
			parent = node
			if d < node.data:
				node = node.left
			elif d > node.data:
				node = node.right
		# Case 3: Node not found
		if node == None or node.data != d:
			return False
		# Case 4: Node has no children
		elif node.left is None and node.right is None:
			if d < parent.data:
				parent.left = None
			else:
				parent.right = None
			return True
		# Case 5: Node has left child only
		elif node.left and node.right is None:
			if d < parent.data:
				parent.left = node.left
			else:
				parent.right = node.left
			return True
		# Case 6: Node has right child only
		elif node.left is None and node.right:
			if d < parent.data:
				parent.left = node.right
			else:
				parent.right = node.right
			return True
		# Case 7: Node has left and right child
		else:
			moveNodeParent = node
			moveNode = node.right
			while moveNode.left:
				moveNodeParent = moveNode
				moveNode = moveNode.left
			node.data = moveNode.data
			if moveNode.right:
				if moveNode.data < moveNodeParent.data:
					moveNodeParent.left = moveNode.right
				else:
					moveNodeParent.right = moveNode.right
			else:
				if moveNode.data < moveNodeParent.data:
					moveNodeParent.left = None
				else:
					moveNodeParent.right = None
			return True
	# return list of data elements resulting from preorder tree traversal
	def preorder(self):
		if self.root:
			return self.root.preorder([])
		else:
			return []
	# return list of postorder elements
	def postorder(self):
		if self.root:
			return self.root.postorder([])
		else:
			return []
	# return list of inorder elements
	def inorder(self):
		if self.root:
			return self.root.inorder([])
		else:
			return []