"""
Program: Balanced Binary Search Tree
---------
Description:
-----------
    First, this program creates a binary search tree of randomly generated numbers
    from the random library. Then it tests the tree to see if it is balanced.
    If it already balanced a message prints. if not it balances the tree. 
    Once tree is balanced, a message is displayed.
    
Name: Christine Mounce
Date: 10 March 2016
"""

import random

class BalancedSearch(object):
#constructor
    def __init__(self,size=16):
        self.tree = [-1 for x in range(size)]
        self.size = size
        self.root = 1
        self.items = 0
        self.rightHeight = 0
        self.leftHeight = 0
      
     
    #balances the binary search tree   
    #recursive
    def balance(self):
        balanceFactor = self.leftHeight - self.rightHeight
        #check to see if tree is already balanced
        #balanceFactor is considered balanced if in range -1 to 1
        # 0 is perfectly balanced
        if balanceFactor == 0
            print("tree is balanced") 
        elif (balanceFactor > 1 )
            #if left heavy, rotate right
            self.rotateRight()
            
        elif (balanceFactor < -1)   
            #else it is right heavy, rotate left
            self.rotateLeft()
    
    
    #rotates tree to the right by one node
    #helper function to balance tree
    def rotateRight(self):
        temp = self.tree[self.root]
        i = self.root
        i = leftChild(i) 
       self.tree[self.root] =  self.tree[i]
       self.insert(temp)
       self.balance()
       
    #changes root to right child then pushes old root to left
    
    #rotates tree to the left by one node
    #helper function to balance tree
    def rotateLeft(self):
         #change root to its left child, then push old root to right
        temp = self.tree[self.root]
        i = self.root
        i = rightChild(i) 
       self.tree[self.root] =  self.tree[i]
       self.insert(temp)
       self.balance()
        
    #inserts value into binary search tree
    def insert(self,val):
        # If list (tree) is empty, put value at root
        if self.tree[self.root] == -1:
            self.tree[self.root] = val
        # loop until you find the location to insert
        # even if you have to extend this list
        else:
            i = self.root
            loop = True
            while loop:
                if val > self.tree[i]:
                    i = self.rightChild(i)
                    self.rightHeight += 1
                else:
                    i = self.leftChild(i)
                    self.leftHeight += 1
                
                if i >= self.size:
                    self.extend()
                
                if self.tree[i] == -1:
                    self.tree[i] = val
                    self.items += 1
                    loop = False
            
     #extends the list to make room for more children/leaves   
    def extend(self):
        temp = [-1 for x in range(self.size)]
        self.tree.extend(temp)
        self.size *= 2
        print(self.items)
    
    #searches tree for the key value    
    def find(self,key):
        #counter of the number of comparisons
        self.comparisons = 1
        #if key is the root, you found it!
        if key == self.tree[self.root]:
            return True
        else:
            i = self.root
            while True:
                if key < self.tree[i]:
                    i = self.leftChild(i)
                else:
                    i = self.rightChild(i)
                    
                if i >= self.size:
                    return False
                
                if self.tree[i] == -1:
                    return False   
                    
                if self.tree[i] == key:
                    return True
                    
                self.comparisons += 1
                
    #calculates index of left child            
    def leftChild(self,i):
        return 2 * i
    
    #calculates index of right child    
    def rightChild(self,i):
        return 2 * i + 1
        
        
random.seed(342345)
bs = BalancedSearch(4096)
for x in range(1000):
    bs.insert(random.randint(0,99999))