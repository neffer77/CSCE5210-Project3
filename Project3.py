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
import copy

class board:
    def __init__(self, board = [["","|","","|",""],["-","-","-","-"],["","|","","|",""],["-","-","-","-"],["","|","","|",""]]):
        self.board = board
        
                    
    def printBoard(self):
        for i in self.board:
            print("")
            for j in i:
                print(j, end =" ") 
                
class node:
    def __init__(self,value,name, board):
        self.value = value
        self.name = name
        self.board = board
        self.endStateCombos = [[[0,0],[0,2],[0,4]],[[2,0],[2,2],[2,4]],[[4,0],[4,2],[4,4]],[[0,0],[2,0],[4,0]],[[0,2],[2,2],[4,2]],[[0,4],[2,4],[4,4]],[[0,0],[2,2],[4,4]],[[0,4],[2,2],[4,0]]]
        
    def isEndState(self):
        value = ["X","O"]
        for k in range(2):
            for i in self.endStateCombos:
                count = 0 
                
                for j in range(3):
                    coords = i[j]
                    if self.board.board[coords[0]][coords[1]] == value[k]:
                        count = count +1
                if count == 3:
                    return True
        return False
        
    
    

class tree:
       def __init__(self,value,name, board):
           
           
       def generateNodes(self, turn):
        currentState = int(self.name)
        spots = self.getOpenSpots()
        nodes = []
        b = board(self.board.board)
        for i in spots:
            n = node(-1,str(currentState + 1) , b)
            n.board.board = self.addMove(n.board.board,turn, i)
            
            nodes.append(n)
            currentState = currentState + 1
        return nodes
    
    def getOpenSpots(self):
        spots = []
        for i in [0,2,4]:
            for j in range(5):
                if (self.board.board[i][j] == ""):
                    spots.append([i,j])
        return spots
     
    def addMove(self,board,turn, spot):
        if turn == 'X':
            board[spot[0]][spot[1]] = 'X'
        elif turn == 'O':
            board[spot[0]][spot[1]] = 'O'
        else:
            print("Error: addMove")
        return board
class agentFunction:
    def __init__(self):
        self.userInput = userInput()
        self.alphabeta = alphabeta()
        self.currentNode = node(-1,"1",board())
        self.alpha = "inf"
        self.beta = "-inf"
        
    def minimax(self):
        n = self.getmax(self.currentNode)
        winner = n.value()
        return winner
        
        
    def getmax(self,n):
        if n.isEndState():
            return n
        nodes =  n.generateNodes('X')
        for n in nodes:
            self.getmax(n,self.getmin(n))
       # if self.alpha > self.alphabeta.getValue():
        #    return n
        
    def getmin(self,n):
        
        if n.isEndState():
            return n;
        nodes = n.generateNodes('O')
        for n in nodes:
            self.getmin(n,self.getmax(n))
            
        #if self.beta < self.alphabeta.getValue():
         #   return n
        
        

class alphabeta:
    def __init__(self):
        self.beta = ""
    
    def getValue(self):
        return self.beta
    
    def determineBeta():
        print("a")
        
    def determineAlpha():
        print("a")
        

class userInput:
    def __init__(self):
        self.input = ""
        
    def getInput(self):
        self.input = input("Select Input Number: ")
        return self.getInput()
        
class action:
    def __init__(self):
        print("a")
    
        
def main():
  brd = board()
  brd.printBoard()
  agtFunc = agentFunction()
  agtFunc.minimax()
   
if __name__ == "__main__":
    main()