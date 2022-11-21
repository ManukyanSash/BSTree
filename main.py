from bst import BSTree

ml = [5,8,1,2,6,10,7,13,16]
tree = BSTree()
ml2 = [7,14,6,18,20,4,0,6]
tree2 = BSTree()
if __name__ == "__main__":
    for el in ml:
        tree.insert(el)
    
    for el in ml2:
        tree2.insert(el)
    
    