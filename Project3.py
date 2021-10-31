# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 10:34:05 2021

@author: conno
"""

#need to make a board - lets try to be as simple as possible 2d array

#need alpha beta algorithm
    #are all end states generated or is there a heuristic evaluation function needed?
    #how is the tree generated
        #recursive tree generation exploring all states

#need user input

class board:
    def __init__(self):
        self.board = [["","|","","|",""],["-","-","-","-"],["","|","","|",""],["-","-","-","-"],["","|","","|",""]]
        
                    
    def printBoard(self):
        for i in self.board:
            print("")
            for j in i:
                print(j, end =" ") 
                
class node:
    def __init__(self,value):
        self.value = value
        self.left = ""
        self.right = ""
        
        
class tree:
    def __init__(self):
        
    def isEndState(self):
        
    def generateNodes(self):
        

def main():
  brd = board()
  brd.printBoard()
   
if __name__ == "__main__":
    main()