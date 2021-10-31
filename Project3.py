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
    def __init__(self,value,name):
        self.value = value
        self.left = ""
        self.right = ""
        self.name = name
        
        
class tree:
    def __init__(self):
        self.root = node("")
        
        
    def isEndState(self):
        
    def generateNodes(self):
        

class agentFunction:
    def __init__(self):
        self.currentNode = ""
        self.userInput = userInput()
        self.alphabeta = alphabeta()
        self.tree = tree()
        self.board = board()
        
    def minimax(self):
        action = self.getmax()
        
        
        
    def dfs(self):
        
    def getmax(self,v):
        v = [-1,-1]
        if self.tree.isEndState():
            return v
        nodes =  self.tree.generateNodes()
        for n in nodes:
            getmax(v,getmin(v))
        if v > self.alphabeta.getValue():
            return v
        
    def getmin(self,v):
        
        if self.tree.isEndState():
            return v;
        input = self.userInput.getInput()
        
        

class alphabeta:
    def __init__(self):
        

class userInput:
    def __init__(self):
        self.input = ""
        
    def getInput(self):
        self.input = input("Select Input Number: ")
        return self.getInput()
        
class action:
    def __init__(self):
        
    
        

def main():
  brd = board()
  brd.printBoard()
   
if __name__ == "__main__":
    main()