import collections

class Node:
    def __init__(self, value=None):
        self.value = value
        self.left=None
        self.right=None
        
class BSTree:
    def __init__(self):
        self.root = None
    
    def __del__(self):
        ...
    
         
    def __iadd__(self, __o):
        if type(__o) == BSTree:
            self.merge(__o)
        
        elif type(__o) == int: 
            self.insert(__o)
        
        else:
            raise Exception("Can't add this value to the BSTree")    
        return self
            
        
    def __add__(self, __o):
        _new_val = BSTree()
        if type(__o) == BSTree:
            _new_val.merge(self)
            _new_val.merge(__o)
            return _new_val
        elif type(__o) == int:
            _new_val.merge(self)
            _new_val.insert(__o)
            return _new_val
        else:
            raise Exception("Can't add this value to the BSTree") 
        
    def __eq__(self, __o: object):
        if type(__o) != BSTree:
            raise Exception("Please mention BSTree")
            
        
        ml1 = self.inorder()
        ml2 = __o.inorder()
        if len(ml1) != len(ml2):
            return False
        else:
            for i in range(len(ml1)):
                if ml1[i] != ml2[i]:
                    return False
        return True        
    
    def __ne__(self, __o: object):
        if type(__o) != BSTree:
            raise Exception("Please mention BSTree")
        
        ml1 = self.inorder()
        ml2 = __o.inorder()
        if len(ml1) != len(ml2):
            return True
        else:
            for i in range(len(ml1)):
                if ml1[i] != ml2[i]:
                    return True
        return False 
        
    def insert(self, value):
        if self.root == None:
            self.root = Node(value)                
        else:
            self._insert(value, self.root)    
    
    def _insert(self, value, node):        
        if value < node.value:
            if node.left == None:
                node.left = Node(value)        
            else:
                self._insert(value, node.left)    
        elif value > node.value:
            if node.right == None:
                node.right = Node(value)            
            else:
                self._insert(value, node.right)    
        else:
            print("Value already in tree!")        
            
    def clear(self):
        if self.root:
            del self.root
                 
        
    def get_height(self):
        if self.root:
            return self._get_height(self.root, 0)             
        else:
            return 0
        
    def _get_height(self, node, height):
        if node==None:
            return height   
        l_height = self._get_height(node.left, height+1)
        r_height = self._get_height(node.right, height+1)
        return max(l_height, r_height)
    
    def erase(self, value):
        if not self.root: return None
        return self._erase(self.root, value) 
    
    def _erase(self, root, value):
        if not root: return None
        
        if root.value == value:
            if not root.left and not root.right: return None
            if not root.left and root.right: return root.right
            if not root.right and root.left: return root.left
            pnt = root.right
            while pnt.left: pnt = pnt.left
            root.value = pnt.value
            root.right = self._erase(root.right, root.value)
        elif root.value > value:
            root.left = self._erase(root.left, value)
        else:
            root.right = self._erase(root.right, value)    
    
        return root
    
    def preorder(self):
        ml = []
        try:
            self._preorder(self.root, ml)    
        except AttributeError:
            return "There is no root element" 
        return ml
    
    def _preorder(self, node, ml):
        if node:
            ml.append(node.value)
            self._preorder(node.left, ml)     
            self._preorder(node.right, ml)
            
    def inorder(self):
        ml = []
        try:
            self._inorder(self.root, ml)
        except AttributeError:
            return "There is no root element" 
        return ml
    
    def _inorder(self, node, ml):        
        if node:
            self._inorder(node.left, ml)  
            ml.append(node.value)
            self._inorder(node.right, ml)
        
                 
    def postorder(self):
        ml = []
        try:
            self._postorder(self.root, ml)
        except AttributeError:
            return "There is no root element"  
        return ml    
    
    def _postorder(self, node, ml):
        if node:
            self._postorder(node.left, ml)  
            self._postorder(node.right, ml) 
            ml.append(node.value) 

            
    def levelorder(self):
        try:
            return self._levelorder(self.root)
        except AttributeError:
            return "There is no root element"
        
    def _levelorder(self, root):
        ans = []
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            currSize = len(queue)
            currList = []
            while currSize > 0:
                currNode = queue.popleft()
                currList.append(currNode.value)
                currSize -= 1    
                if currNode.left is not None:
                    queue.append(currNode.left)
                if currNode.right is not None:
                    queue.append(currNode.right)
            for el in currList:        
                ans.append(el)
        return ans   
        
    def get_root_data(self):    
        try:
            return self.root.value
        except AttributeError:
            return "There is no root data"
        
    def find(self, value):
        if not self.root:
            return False
        else:
            return self._find(self.root, value)
    
    def _find(self, node, value):
        if value == node.value:
            return True   
        
        elif value > node.value:
            if node.right == None:
                return False
            else:
                return self._find(node.right, value)
        
        else:
            if node.left == None:
                return False
            else:
                return self._find(node.left, value)
        
    def get_number_of_nodes(self):    
        if not self.root:
            return 0
        return self._get_number_of_nodes(self.root)
        
    def _get_number_of_nodes(self, node):
        if node == None:
            return 0
        return 1 + self._get_number_of_nodes(node.left) + self._get_number_of_nodes(node.right)
    
    def merge(self, new_tree):
        if not new_tree.root:
            return
        ml = new_tree.preorder()
        for el in ml:
            self.insert(el)
    
    def contains(self, value):
        if not self.root: return None
        return self._contains(self.root, value)
    
    def _contains(self, root, value):
        if root.value == value:
            return root
        elif root.value > value:
            if root.left:
                return self._contains(root.left, value)
            else:
                return None
        else:
            if root.right:
                return self._contains(root.right, value)
            else:
                return None