# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 10:34:05 2021

@author: conno
"""

#need to make a board - lets try to be as simple as possible 2d array

#need alpha beta algorithm

#need user input

class board:
    def __init__(self):
        self.board = [["","|","","|",""],["-","-","-","-"],["","|","","|",""],["-","-","-","-"],["","|","","|",""]]
        
                    
    def printBoard(self):
        for i in self.board:
            print("")
            for j in i:
                print(j, end =" ")           
    

def main():
  brd = board()
  brd.printBoard()
   
if __name__ == "__main__":
    main()