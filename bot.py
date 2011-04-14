import autopy, sys

Column1 = [0,0,0,0,0,0,0,0] 
Column2 = [0,0,0,0,0,0,0,0] 
Column3 = [0,0,0,0,0,0,0,0] 
Column4 = [0,0,0,0,0,0,0,0] 
Column5 = [0,0,0,0,0,0,0,0] 
Column6 = [0,0,0,0,0,0,0,0] 
Column7 = [0,0,0,0,0,0,0,0] 
Column8 = [0,0,0,0,0,0,0,0] 
Rows = [Column1,Column2,Column3,Column4,Column5,Column6,Column7,Column8]
C1 = [0,0,0,0,0,0,0,0] 
C2 = [0,0,0,0,0,0,0,0] 
C3 = [0,0,0,0,0,0,0,0] 
C4 = [0,0,0,0,0,0,0,0] 
C5 = [0,0,0,0,0,0,0,0] 
C6 = [0,0,0,0,0,0,0,0] 
C7 = [0,0,0,0,0,0,0,0] 
C8 = [0,0,0,0,0,0,0,0] 
R = [C1,C2,C3,C4,C5,C6,C7,C8]

gameOverCounter = 0
moveCounter = 0

def printboard():
  print(Column1)
  print(C1)
  print(Column2)
  print(C2)
  print(Column3)
  print(C3)
  #print(Column4)
  #print(Column5)
  #print(Column6)
  #print(Column7)
  #print(Column8)

def delay(length):
  for x in range(length):
    for y in range(length):
      pass

def getScreen():
  for y in reversed(range(8)):
    for x in reversed(range(8)):
      R[x][y] = autopy.screen.get_color((400+(x*40)),(480+(y*40)))
      #yellows
      if((R[x][y] > 16700000) and (R[x][y] < 16800000)):
        Rows[x][y] = 1
        #break
      #blues
      if((R[x][y] > 680000) and (R[x][y] < 700000)):
        Rows[x][y] = 2
        #break
      #whites  
      if((R[x][y] > 13600000) and (R[x][y] < 13900000)):
        Rows[x][y] = 3
        #break
      #purple 
      if((R[x][y] > 15900000) and (R[x][y] < 16200000)):
        Rows[x][y] = 4
        #break    
      #oranges 
      if((R[x][y] > 16500000) and (R[x][y] < 16700000)):
        Rows[x][y] = 5
        #break  
      #greens 
      if((R[x][y] > 640000) and (R[x][y] < 660000)):
        Rows[x][y] = 6
        #break       
      #reds 
      if((R[x][y] > 16200000) and (R[x][y] < 16400000)):
        Rows[x][y] = 7
        #break     
      
def findMove():
  foundMove = False
  for x in range(8):
    for y in range(8):
      #move up
      #check up
      x1 = x
      y1 = y-2
      x2 = x
      y2 = y-3
      if(y2 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving up up')
          makeMove((x,y),(x,y-1))
          break
      #check left
      x1 = x-1
      x2 = x-2
      y1 = y-1
      y2 = y-1
      if(x2 >= 0 and y2 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving up left')
          makeMove((x,y),(x,y-1))
          break
      #check right
      x1 = x+1
      x2 = x+2
      y1 = y-1
      y2 = y-1
      if(x2 <= 7 and y2 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving up right')
          makeMove((x,y),(x,y-1))
          break
      #check around
      x1 = x+1
      x2 = x-1
      y1 = y-1
      y2 = y-1
      if(x1 <= 7 and x2 >= 0 and y2 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving up around')
          makeMove((x,y),(x,y-1))
          break
      #move left
      #check up
      x1 = x-1
      y1 = y-1
      x2 = x-1
      y2 = y-2
      if(y2 >= 0 and x1 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving left up')
          makeMove((x,y),(x-1,y))
          break
      #check left
      x1 = x-2
      x2 = x-3
      y1 = y
      y2 = y
      if(x2 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving left left')
          makeMove((x,y),(x-1,y))
          break
      #check down
      x1 = x-1
      x2 = x-1
      y1 = y+1
      y2 = y+2
      if(x2 >= 0 and y2 <= 7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving left down')
          makeMove((x,y),(x-1,y))
          break 
      #check around
      x1 = x-1
      x2 = x-1
      y1 = y+1
      y2 = y-1
      if(x2 >= 0 and y1 <= 7 and y2 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving left around')
          makeMove((x,y),(x-1,y))
          break 
      #move right
      #check up
      x1 = x+1
      y1 = y-1
      x2 = x+1
      y2 = y-2
      if(y2 >= 0 and x1 <= 7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving right up')
          makeMove((x,y),(x+1,y))
          break
      #check right
      x1 = x+2
      x2 = x+3
      y1 = y
      y2 = y
      if(x2 <= 7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving right right')
          makeMove((x,y),(x+1,y))
          break
      #check down
      x1 = x+1
      x2 = x+1
      y1 = y+1
      y2 = y+2
      if(x2 <= 7 and y2 <= 7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving right down')
          makeMove((x,y),(x+1,y))
          break
      #check around
      x1 = x+1
      x2 = x+1
      y1 = y+1
      y2 = y-1
      if(x2 <= 7 and y1 <= 7 and y2 >= 0):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving right around')
          makeMove((x,y),(x+1,y))
          break
      #move down
      #check down
      x1 = x
      y1 = y+2
      x2 = x
      y2 = y+3
      if(y2 <= 7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving up up')
          makeMove((x,y),(x,y+1))
          break
      #check left
      x1 = x-1
      x2 = x-2
      y1 = y+1
      y2 = y+1
      if(x2 >= 0 and y2 <=7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving up left')
          makeMove((x,y),(x,y+1))
          break
      #check right
      x1 = x+1
      x2 = x+2
      y1 = y+1
      y2 = y+1
      if(x2 <= 7 and y2 <= 7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving up right')
          makeMove((x,y),(x,y+1))
          break
      #check around
      x1 = x+1
      x2 = x-1
      y1 = y+1
      y2 = y+1
      if(x1 <= 7 and x2 >= 0 and y2 <= 7):
        if(Rows[x][y] == Rows[x1][y1] == Rows[x2][y2]):
          print('found move at',x,y,'moving up around')
          makeMove((x,y),(x,y+1))
          break
  print('found no moves')
  print(Column1)
  print(Column2)
  print(Column3)
  print(Column4)
  print(Column5)
  print(Column6)
  print(Column7)
  print(Column8)
  
def makeMove(fromLoc, toLoc):
  print(moveCounter,'from',fromLoc,'to',toLoc)
  autopy.mouse.move((fromLoc[0]*40)+400,(fromLoc[1]*40)+480)
  #delay(250)
  delay(1000)
  autopy.mouse.toggle(True)
  #delay(250)
  delay(1000)
  try:
    autopy.mouse.smooth_move(((toLoc[0]*40)+400),((toLoc[1]*40)+480))
  except ValueError:
    #print('valueerror ',((toLoc[0]*40)+400),((toLoc[1]*40)+480))
    #delay(200000)
    autopy.mouse.toggle(False)
    return
  #delay(200)
  delay(1000)
  autopy.mouse.toggle(False)
  #getScreen()
  
def main():
 #mouselocation = 400+x*40  / 480 + y*40
  mainLoopCounter = 0
  
  autopy.mouse.move(100,480)
  delay(200)
  autopy.mouse.click()
  delay(200)
  autopy.mouse.move(400,480)
  delay(200)
  
  while(True):
    print(mainLoopCounter)
    print('getscreen')
    getScreen()
    #printboard()
    print('findmove')
    findMove()
    #gameOver = autopy.screen.get_color(400,480)
    #mainLoopCounter = mainLoopCounter+1
  #print('gameover?')

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()


