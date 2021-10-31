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
        self.endStateCombos = [[[0,0],[0,3],[0,5]],[[2,0],[2,3],[2,5]],[[4,0],[4,3],[4,5]],[[0,0],[3,0],[5,0]],[[0,2],[3,2],[5,2]],[[0,4],[3,4],[5,4]],[[0,0],[2,2],[5,5]],[0,5],[2,2],[5,0]]]
        self.board = board()    
    
    def isEndState(self):
        value = ["X","O"]
        for k in range(2):
            for i in self.endStateCombos:
                count = 0 
                for j in range(3):
                    coords = i[j]
                    if self.board[coords[0],coords[1]] == value[k]:
                        count = count +1
                if count == 3:
                    return True
        return False
    
    def generateNodes(self):
        

class agentFunction:
    def __init__(self):
        self.currentNode = node("","1")
        self.userInput = userInput()
        self.alphabeta = alphabeta()
        self.tree = tree()
        
    def minimax(self):
        n = self.getmax(self.currentNode)
        winner = n.value()
        return winner
        
        
    def getmax(self,n):
        if self.tree.isEndState():
            return n
        nodes =  self.tree.generateNodes()
        for n in nodes:
            getmax(n,getmin(n))
        if v > self.alphabeta.getValue():
            return n
        
    def getmin(self,n):
        
        if self.tree.isEndState():
            return state;
        input = self.userInput.getInput()
        return state
        
        

class alphabeta:
    def __init__(self):
        self.beta = ""
    
    def getValue(self):
        return self.beta
    
    def determineBeta():
        
        

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