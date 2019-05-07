from BST import BST

def kth_smallest_element(list1,k):


    bst=BST()
    bst.populate_bst(list1)
    inorderlist=bst.inorder(bst.root,[])
    kth_min=inorderlist[k-1]
    return kth_min


if __name__=='__main__':

   list1=[5,67,78,90,45,67,90]
   print ("Kth_min_element is ="+str(kth_smallest_element(list1, 2)))

