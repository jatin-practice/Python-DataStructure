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

    def inorder(self, root,inorder_list):

        if (root):
            self.inorder(root.left,inorder_list)
            inorder_list.append(root.data)
            self.inorder(root.right,inorder_list)
        return inorder_list

    def preorder(self, root,preorder_list):
        if (root):
            preorder_list.append(root.data)
            self.preorder(root.left,preorder_list)
            self.preorder(root.right,preorder_list)

        return preorder_list

    def postorder(self, root,postorder_list):
        if (root):
            self.preorder(root.left,postorder_list)
            self.preorder(root.right,postorder_list)
            postorder_list.append(root.data)
        return postorder_list

    def depth_BST(self, root):
        if (root is None):
            return 0
        else:
            return 1 + max(self.depth_BST(root.left), self.depth_BST(root.right))

    def populate_bst(self,list1):
        for i in list1:
            self.add_node(i)


if __name__ == '__main__':
    bst = BST()
    list1 = [10, 20, 5, 14, 26, 23, 34, 45, 78]
    inorder_list=[]
    preorder_list=[]
    postorder_list=[]

    bst.populate_bst(list1)
    print ("Inorderlist="+','.join(str(i) for i in bst.inorder(bst.root,inorder_list)))
    print("Preorderlist=" + ','.join(str(i) for i in bst.preorder(bst.root,preorder_list)))
    print("Postorderlist=" + ','.join(str(i) for i in bst.postorder(bst.root,postorder_list)))

    print("Deptth of BST="+str(bst.depth_BST(bst.root)))
