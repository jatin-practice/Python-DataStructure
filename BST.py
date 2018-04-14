class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add_node(self, data):
        if (self.root == None):
            self.root = Node(data)
            temp = self.root
        elif (data > self.root.data):

            if (self.root.right == None):
                self.root.right = Node(data)
                self.rightchild = self.root.right
            elif (data > self.rightchild.data):
                self.rightchild.right = Node(data)
                self.rightchild = self.rightchild.right
            else:
                self.rightchild.left = Node(data)
                self.rightchild.left = self.rightchild.left



        elif (self.root.data > data):
            if (self.root.left == None):
                self.root.left = Node(data)
                self.leftchild = self.root.left
            elif (data < self.leftchild.data):
                self.leftchild.left = Node(data)
                self.leftchild = self.leftchild.left
            else:
                self.leftchild.right = Node(data)
                self.leftchild.right = self.leftchild.right

    def inorder(self, root):
        if (root):
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)

    def preorder(self, root):
        if (root):
            print("preorder" + str(root.data))
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root):
        if (root):
            self.preorder(root.left)
            self.preorder(root.right)
            print("postorder" + str(root.data))

    def depth_BST(self, root):
        if (root is None):
            return 0
        else:
            return 1 + max(self.depth_BST(root.left), self.depth_BST(root.right))


if __name__ == '__main__':
    bst = BST()
    list1 = [10, 20, 5, 14, 26, 23, 34, 45, 78]
    for i in list1:
        bst.add_node(i)
    bst.inorder(bst.root)
    bst.preorder(bst.root)
    bst.postorder(bst.root)
    print("Deptth of BST="+str(bst.depth_BST(bst.root)))
