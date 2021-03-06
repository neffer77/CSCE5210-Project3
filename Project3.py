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

#now we need to propogate those values up when a terminal state is reached.


import copy

class board:
    def __init__(self, board = [["","|","","|",""],["-","-","-","-"],["","|","","|",""],["-","-","-","-"],["","|","","|",""]]):
        self.board = board
        
                    
    def printBoard(self):
        for i in self.board:
            print("")
            for j in i:
                print(j, end =" ") 
                
    def printUserBoard(self):
        count = 1
        for i in self.board:
            print("")
            for j in i:
                if j == "":
                    print(str(count), end = " ")
                    count = count +1
                else:
                    print( j, end = " ")
                    
    def moveCount(self):
        count = 0
        for i in self.board:
            for j in i:
                if j == "X" or j == "O":
                    count = count + 1
        return count
    
                
class node:
    def __init__(self,value,name, board):
        self.value = value
        self.name = name
        self.board = board
        self.endStateCombos = [[[0,0],[0,2],[0,4]],[[2,0],[2,2],[2,4]],[[4,0],[4,2],[4,4]],[[0,0],[2,0],[4,0]],[[0,2],[2,2],[4,2]],[[0,4],[2,4],[4,4]],[[0,0],[2,2],[4,4]],[[0,4],[2,2],[4,0]]]
        self.parent = ""
        self.alphabeta = alphabeta()
        
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
                    if k== 0:
                        self.value = 1
                    elif k == 1:
                        self.value = -1
                    return True
        
        count = 0
        for i in [[0,0],[0,2],[0,4],[2,0],[2,2],[2,4],[4,0],[4,2],[4,4]]:
            if self.board.board[i[0]][i[1]] == '':
                count = count + 1
        if count == 0:
            self.value = 0
            return True
        return False
        
    
    

class tree:
       def __init__(self,n):
           self.root = n
           
           
       def generateNodes(self, n, turn):
            currentState = int(n.name)
            spots = self.getOpenSpots(n)
            nodes = []
            b = copy.deepcopy(board(n.board.board))
            for i in spots:
                newNode = copy.deepcopy(node(-2,str(currentState + 1) , b))
                newNode.board = self.addMove(newNode.board,turn, i)
                newNode.parent = n
                nodes.append(newNode)
                currentState = currentState + 1
            return nodes
    
       def getOpenSpots(self,n):
            spots = []
            for i in [0,2,4]:
                for j in range(5):
                    if (n.board.board[i][j] == ""):
                        spots.append([i,j])
            return spots
         
       def addMove(self,board,turn, spot):
            if turn == 'X':
                board.board[spot[0]][spot[1]] = 'X'
            elif turn == 'O':
                board.board[spot[0]][spot[1]] = 'O'
            else:
                print("Error: addMove")
            return board
        
class agentFunction:
    def __init__(self):
        self.userInput = userInput()
        self.currentNode = node(-2,"1",board())
        self.tree = tree(self.currentNode)
        
    def minimax(self):
        depth = 0
        n = self.getmax(self.currentNode,0, depth)
        return n
        
        
        
    def getmax(self,n,mvalue, depth):
        maxlist = []
        highval = -1
        if n.isEndState():
            return n.value
        nodes =  self.tree.generateNodes(n,'X')
        for q in nodes:
           
           q.alphabeta.alpha = n.alphabeta.alpha
           q.alphabeta.beta = n.alphabeta.beta
           if n.alphabeta.beta != "inf":
               if n.alphabeta.alpha != "-inf":
                   if n.alphabeta.alpha >= n.alphabeta.beta:
                       highval = n.alphabeta.alpha
                       return highval
           mvalue = self.getmin(q, mvalue, depth+1)
           maxlist.append(mvalue)
           n.alphabeta.determineAlpha(mvalue)
           
        for i in maxlist:
            if i > highval:
                highval = i
    
        n.value = highval
        if depth == 0:
            for i in nodes:
                if i.value == highval:
                    return i
            
           #self.alphabeta.determineAlpha(nd)
           
           #if self.alphabeta.beta != "inf":
            #   if nd.value >= self.alphabeta.beta:
             #      mvalue = nd.value
              #     return nd,mvalue
        return n.value
        
    def getmin(self,n, mvalue, depth):
        minlist = []
        lowval = 1
        if n.isEndState():
            return n.value;
        nodes = self.tree.generateNodes(n,'O')
        for q in nodes:
           q.alphabeta.alpha = n.alphabeta.alpha
           q.alphabeta.beta = n.alphabeta.beta
           if n.alphabeta.alpha != "-inf":
               if n.alphabeta.beta != "inf":
                   if n.alphabeta.alpha >= n.alphabeta.beta:
                       highval = n.alphabeta.alpha
                       return highval
           mvalue = self.getmax(q, mvalue, depth+1)
           minlist.append(mvalue)
           n.alphabeta.determineBeta(mvalue)
        for i in minlist:
            if i < lowval:
                lowval = i
                
        n.value = lowval          
           #self.alphabeta.determineBeta(minlist)
           #if self.alphabeta.alpha != "-inf":
            #   if nd.value <= self.alphabeta.alpha:
             #      mvalue = nd.value
              #     return nd, mvalue
        return n.value
        

class alphabeta:
    def __init__(self):
        self.beta = "inf"
        self.alpha = "-inf"
    
    def getBetaValue(self):
        return self.beta
    
    def getAlphaValue(self):
        return self.alpha
    
    def determineBeta(self,mvalue):
        if self.beta == 'inf':
            self.beta = mvalue
            return
        elif self.beta > mvalue:
            self.beta = mvalue
            return
        else:
            return
        
    def determineAlpha(self,mvalue):
        if self.alpha == '-inf':
            self.alpha = mvalue
            return
        elif self.alpha < mvalue:
           self.alpha = mvalue
           return
        else:
           return
        

class userInput:
    def __init__(self):
        self.input = ""
        
    def getInput(self, n):
        n.board.printUserBoard()
        self.input = input("Select Input Number: ")
        return self.input
    
    def makeMove(self,inpt,n):
        b = self.makeBoard(copy.deepcopy(n.board.board))
        for i in [0,2,4]:
            for j in [0,2,4]:
                if b[i][j] == inpt:
                    n.board.board[i][j] = 'O'
        return n
    
    def makeBoard(self, board):
        count = 1
        for i in [0,2,4]:
            for j in [0,2,4]:
                if board[i][j] == "":
                    board[i][j] = count
                    count = count + 1
        return board
        
class action:
    def __init__(self):
        print("a")
    
        
def main():
  brd = board()
  brd.printBoard()
  print("")
  agtFunc = agentFunction()
  winner = False
  player2 = userInput()
  turns = 1
  move = False
  while not winner:
      player1 = agtFunc.minimax()
      player1Move = player1
      while not move:
          if player1Move.board.moveCount() == turns:
              move = True
          else:
              player1Move = player1Move.parent
      move = False
      print("")
      print("Player 1 Move:")
      player1Move.board.printBoard()
      print("")
      if (player1Move.isEndState()):
          winner = True
          return
      turns = turns + 2
      i = player2.getInput(player1Move)
      player2Move = player2.makeMove(int(i),copy.deepcopy(player1Move))
      print("")
      print("Player 2 Move:")
      player2Move.board.printBoard()
      print("")
      if (player2Move.isEndState()):
          winner = True
          return
      agtFunc.currentNode = copy.deepcopy(player2Move)
      agtFunc.currentNode.alphabeta.alpha = "-inf"
      agtFunc.currentNode.alphabeta.beta = "inf"
  
  
  
  
if __name__ == "__main__":
    main()