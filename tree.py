from re import search


class BSTree:
    def __init__(self,key):
        self.val = key
        self.left = None
        self.right = None

    def insert(root,key):
        if root is None:
            return BSTree(key)
        
            if key < root.val:
                root.left = insert(root.left,key)
            else:
                root.right = insert(root.right,key)

        return root
    
    def search(root,key):
        if root is None:
            return False
        if root.val == key:
            return True
        
        if key < root.val:
            return search(root.left,key)
        return search(root.right,key)
    

        